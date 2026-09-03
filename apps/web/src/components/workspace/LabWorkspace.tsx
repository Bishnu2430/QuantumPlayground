"use client";
import { useMemo, useState } from "react";
import type { Circuit } from "@/lib/api/client";
import { useCopilot } from "@/hooks/useCopilot";
import { useSimulation } from "@/hooks/useSimulation";
import {
  Bot,
  ChevronRight,
  Play,
  Plus,
  RotateCcw,
  Send,
  Sparkles,
  X,
} from "lucide-react";
const gates = ["H", "X", "Y", "Z", "CX", "Measure"];
const gateName: Record<string, string> = {
  H: "h",
  X: "x",
  Y: "y",
  Z: "z",
  CX: "cx",
  Measure: "measure",
};
const initial: Circuit = {
  numQubits: 2,
  numClbits: 2,
  operations: [],
};
export function LabWorkspace({ initialCircuit }: { initialCircuit?: Circuit }) {
  const [circuit, setCircuit] = useState<Circuit>(initialCircuit ?? initial),
    [message, setMessage] = useState("Explain this Bell-state circuit.");
  const simulation = useSimulation();
  const copilot = useCopilot();
  const busy = simulation.isRunning || copilot.isAsking;
  const result = simulation.result;
  const answer = copilot.answer;
  const error = simulation.error || copilot.error;
  const operations = useMemo(
    () => [...circuit.operations].sort((a, b) => a.moment - b.moment),
    [circuit],
  );
  const addGate = (label: string) => {
    const gate = gateName[label];
    const moment = Math.max(-1, ...circuit.operations.map((o) => o.moment)) + 1;
    const op =
      gate === "cx"
        ? { gate, controls: [0], targets: [1], moment }
        : gate === "measure"
          ? { gate, targets: [0, 1], clbits: [0, 1], moment }
          : { gate, targets: [0], moment };
    setCircuit({ ...circuit, operations: [...circuit.operations, op] });
  };
  const run = async () => {
    await simulation.run(circuit);
  };
  const ask = async () => {
    await copilot.ask(message, circuit);
  };
  return (
    <div className="workspace-grid">
      <section className="workspace-main">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Interactive workspace</p>
            <h1>Circuit simulator</h1>
            <p>
              Assemble a quantum circuit, run it, and inspect the measured
              output.
            </p>
          </div>
          <button className="primary-button" onClick={run} disabled={busy}>
            <Play size={16} />
            {busy ? "Running" : "Run circuit"}
          </button>
        </div>
        <div className="lab-card circuit-card">
          <div className="card-top">
            <div>
              <strong>Quantum circuit</strong>
              <span>
                {circuit.numQubits} qubits · {operations.length} operations
              </span>
            </div>
            <button
              className="text-button"
              onClick={() => {
                setCircuit(initial);
                simulation.reset();
                copilot.reset();
              }}
            >
              <RotateCcw size={15} /> Reset
            </button>
          </div>
          <div className="gate-palette">
            {gates.map((g) => (
              <button key={g} onClick={() => addGate(g)}>
                <Plus size={13} />
                {g}
              </button>
            ))}
          </div>
          <div className="circuit-grid">
            {[...Array(circuit.numQubits)].map((_, qubit) => (
              <div className="qubit-row" key={qubit}>
                <span>q{qubit}</span>
                <div className="wire">
                  {operations.map((op, index) =>
                    op.targets.includes(qubit) ||
                    op.controls?.includes(qubit) ? (
                      <div
                        className={`gate ${op.gate === "measure" ? "measure" : ""}`}
                        key={index}
                      >
                        {op.controls?.includes(qubit)
                          ? "●"
                          : op.gate.toUpperCase()}
                      </div>
                    ) : (
                      <i key={index} />
                    ),
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
        <div className="results-grid">
          <div className="lab-card">
            <div className="card-top">
              <div>
                <strong>Measurement</strong>
                <span>
                  {result
                    ? `${result.shots ?? 0} shots in ${result.durationMs}ms`
                    : "Run the circuit to inspect results"}
                </span>
              </div>
            </div>
            {result?.probabilities ? (
              <div className="bars">
                {Object.entries(result.probabilities).map(([state, value]) => (
                  <div className="bar-row" key={state}>
                    <span>|{state}⟩</span>
                    <div>
                      <i style={{ width: `${value * 100}%` }} />
                    </div>
                    <b>{(value * 100).toFixed(1)}%</b>
                  </div>
                ))}
              </div>
            ) : (
              <div className="empty-state">
                Measurement probabilities will appear here.
              </div>
            )}
          </div>
          <div className="lab-card state-card">
            <p className="eyebrow">State insight</p>
            <h3>{result ? "Entanglement observed" : "Ready to simulate"}</h3>
            <p>
              {result
                ? "The simulator returned a measurement distribution for this circuit."
                : circuit.operations.length
                  ? "Add gates, then run the circuit to inspect its state and measurements."
                  : "Start with an empty circuit and add gates from the palette."}
            </p>
            <Sparkles size={22} />
          </div>
        </div>
      </section>
      <aside className="copilot-card">
        <div className="copilot-title">
          <span className="brand-mark">
            <Bot size={18} />
          </span>
          <div>
            <strong>Quantum copilot</strong>
            <p>Grounded in your circuit</p>
          </div>
        </div>
        <div className="chat-answer">
          {answer ||
            "Ask a question about the circuit, measurements, or the math behind entanglement."}
        </div>
        <div className="prompt-list">
          {[
            "Why do results match?",
            "Show the statevector",
            "What does the H gate do?",
          ].map((p) => (
            <button
              key={p}
              onClick={() => {
                setMessage(p);
                copilot.reset();
              }}
            >
              <ChevronRight size={15} />
              {p}
            </button>
          ))}
        </div>
        <label className="chat-input">
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            aria-label="Question for Quantum Copilot"
          />
          <button onClick={ask} disabled={busy} aria-label="Send question">
            <Send size={17} />
          </button>
        </label>
        {error && (
          <p className="api-error">
            <X size={14} />
            {error}. Start the API at port 8000.
          </p>
        )}
      </aside>
    </div>
  );
}
