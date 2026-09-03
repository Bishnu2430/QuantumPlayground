import { PythonLab } from "@/components/workspace/PythonLab";
import { Suspense } from "react";
export default function Laboratory() {
  return (
    <Suspense
      fallback={
        <main className="dashboard">
          <p>Loading laboratory...</p>
        </main>
      }
    >
      <PythonLab />
    </Suspense>
  );
}
