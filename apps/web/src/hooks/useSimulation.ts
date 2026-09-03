import { useState } from "react";
import { api, type Circuit, type SimulationResult } from "@/lib/api/client";

export function useSimulation() {
  const [result, setResult] = useState<SimulationResult>();
  const [isRunning, setIsRunning] = useState(false);
  const [error, setError] = useState("");

  const run = async (
    circuit: Circuit,
    mode: "shots" | "statevector" = "shots",
  ) => {
    setIsRunning(true);
    setError("");
    try {
      const nextResult = await api.simulate(circuit, mode);
      setResult(nextResult);
      return nextResult;
    } catch (cause) {
      setError(
        cause instanceof Error ? cause.message : "Simulator unavailable",
      );
      throw cause;
    } finally {
      setIsRunning(false);
    }
  };

  const reset = () => {
    setResult(undefined);
    setError("");
  };

  return { result, isRunning, error, run, reset };
}
