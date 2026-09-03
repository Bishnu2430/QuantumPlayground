"use client";

import { useSearchParams } from "next/navigation";
import { LabWorkspace } from "./LabWorkspace";
import type { Circuit } from "@/lib/api/client";

export function SimulatorRoute() {
  const params = useSearchParams();
  let circuit: Circuit | undefined;
  try {
    const value = params.get("circuit");
    if (value) circuit = JSON.parse(value) as Circuit;
  } catch {
    circuit = undefined;
  }
  return <LabWorkspace initialCircuit={circuit} />;
}
