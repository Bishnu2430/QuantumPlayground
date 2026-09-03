"use client";

import { useSearchParams } from "next/navigation";
import { useState } from "react";
import { api } from "@/lib/api/client";
import { Play, RotateCcw } from "lucide-react";

const starter = "";
export function PythonLab() {
  const params = useSearchParams();
  const [code, setCode] = useState(() =>
    params.get("code") ? decodeURIComponent(params.get("code")!) : starter,
  );
  const [output, setOutput] = useState("");
  const [running, setRunning] = useState(false);
  const run = async () => {
    setRunning(true);
    try {
      const result = await api.runPython(code);
      setOutput(
        `${result.stdout}${result.stderr ? `\n${result.stderr}` : ""}\nExit code: ${result.exitCode}`,
      );
    } catch (error) {
      setOutput(error instanceof Error ? error.message : "Runner unavailable");
    } finally {
      setRunning(false);
    }
  };
  return (
    <main className="dashboard lab-page">
      <header className="topbar">
        <div>
          <p className="eyebrow">Python + Qiskit</p>
          <h1>Laboratory</h1>
          <p className="catalog-copy">
            Write, run, and inspect a small quantum program. Opened directly,
            this starts with a blank-friendly example you can replace.
          </p>
        </div>
        <div className="lesson-actions">
          <button className="primary-button" onClick={run} disabled={running}>
            <Play size={16} /> {running ? "Running" : "Run code"}
          </button>
          <button
            className="secondary-button"
            onClick={() => {
              setCode(starter);
              setOutput("");
            }}
          >
            <RotateCcw size={16} /> Reset
          </button>
        </div>
      </header>
      <section className="code-lab">
        <textarea
          value={code}
          onChange={(event) => setCode(event.target.value)}
          spellCheck={false}
          aria-label="Python Qiskit code"
        />
        <pre>{output || "Output will appear here after execution."}</pre>
      </section>
    </main>
  );
}
