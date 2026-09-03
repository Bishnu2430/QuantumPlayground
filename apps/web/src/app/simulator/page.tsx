import { SimulatorRoute } from "@/components/workspace/SimulatorRoute";
import { Suspense } from "react";
export default function Simulator() {
  return (
    <Suspense
      fallback={
        <main className="dashboard">
          <p>Loading simulator...</p>
        </main>
      }
    >
      <SimulatorRoute />
    </Suspense>
  );
}
