import { useState } from "react";
import { api, type Circuit, type CopilotDepth } from "@/lib/api/client";

export function useCopilot() {
  const [answer, setAnswer] = useState("");
  const [model, setModel] = useState("");
  const [isAsking, setIsAsking] = useState(false);
  const [error, setError] = useState("");

  const ask = async (
    message: string,
    circuit?: Circuit,
    depth: CopilotDepth = "undergraduate",
  ) => {
    setIsAsking(true);
    setError("");
    try {
      const response = await api.chat(message, circuit, depth);
      setAnswer(response.answer);
      setModel(response.model);
      return response;
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Copilot unavailable");
      throw cause;
    } finally {
      setIsAsking(false);
    }
  };

  const reset = () => {
    setAnswer("");
    setModel("");
    setError("");
  };

  return { answer, model, isAsking, error, ask, reset };
}
