export type Operation = {
  gate: string;
  targets: number[];
  controls?: number[];
  clbits?: number[];
  params?: number[];
  moment: number;
};
export type Circuit = {
  numQubits: number;
  numClbits: number;
  operations: Operation[];
};
export type SimulationResult = {
  backend: string;
  numQubits: number;
  shots?: number;
  counts?: Record<string, number>;
  probabilities?: Record<string, number>;
  statevector?: { real: number; imag: number }[];
  durationMs: number;
};
export type Lesson = {
  id: string;
  slug: string;
  title: string;
  description?: string;
  content: string;
  difficulty: number;
  domain: string;
  module: string;
  order: number;
  is_published: boolean;
};
export type CopilotDepth =
  | "intuitive"
  | "undergraduate"
  | "mathematical"
  | "formal";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api/v1";

export class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
  ) {
    super(message);
  }
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  let response: Response;
  try {
    response = await fetch(`${API_URL.replace(/\/$/, "")}${path}`, {
      ...init,
      headers: { "Content-Type": "application/json", ...init.headers },
      cache: "no-store",
    });
  } catch {
    throw new ApiError(
      "Quantum Lab API is unreachable. Start the backend on port 8000 and refresh.",
      0,
    );
  }
  if (!response.ok) {
    const body = await response.json().catch(() => null);
    throw new ApiError(
      body?.detail?.message ??
        body?.detail ??
        `Request failed (${response.status})`,
      response.status,
    );
  }
  return response.json() as Promise<T>;
}

export const api = {
  status: () => request<{ status: string; version: string }>("/status"),
  simulate: (circuit: Circuit, mode: "shots" | "statevector" = "shots") =>
    request<SimulationResult>("/simulation/run", {
      method: "POST",
      body: JSON.stringify({ circuit, mode, shots: 1024, seed: 42 }),
    }),
  chat: (
    message: string,
    circuit?: Circuit,
    depth: CopilotDepth = "undergraduate",
  ) =>
    request<{ answer: string; model: string }>("/copilot/chat", {
      method: "POST",
      body: JSON.stringify({ message, depth, context: { circuit } }),
    }),
  runPython: (code: string) =>
    request<{ stdout: string; stderr: string; exitCode: number }>(
      "/simulation/python",
      { method: "POST", body: JSON.stringify({ code, timeoutSeconds: 10 }) },
    ),
  lessons: () => request<Lesson[]>("/lessons?published=true"),
  lesson: (slug: string) =>
    request<Lesson>(`/lessons/${encodeURIComponent(slug)}`),
  algorithms: () =>
    request<{ items: Array<{ slug: string; title: string; qubits: number }> }>(
      "/algorithms",
    ),
  experiments: () =>
    request<{
      items: Array<{ slug: string; title?: string; description?: string }>;
    }>("/experiments"),
};
