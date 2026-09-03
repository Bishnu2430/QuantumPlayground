"use client";

import { useState } from "react";
import { Bot, Send, Sparkles } from "lucide-react";
import { useCopilot } from "@/hooks/useCopilot";
import type { CopilotDepth } from "@/lib/api/client";

const suggestions = [
  "Explain superposition simply",
  "Derive the Born rule",
  "How do I reduce circuit noise?",
];
const depths: CopilotDepth[] = [
  "intuitive",
  "undergraduate",
  "mathematical",
  "formal",
];
export function CopilotWorkspace() {
  const [message, setMessage] = useState("");
  const [depth, setDepth] = useState<CopilotDepth>("undergraduate");
  const copilot = useCopilot();
  const ask = async () => {
    const question = message.trim();
    if (!question || copilot.isAsking) return;
    await copilot.ask(question, undefined, depth);
    setMessage("");
  };
  return (
    <main className="dashboard copilot-page">
      <header className="topbar">
        <div>
          <p className="eyebrow">Quantum tutor</p>
          <h1>Ask the copilot.</h1>
          <p className="catalog-copy">
            Explore concepts, equations, code, and circuit behavior with answers
            grounded in the Quantum Lab curriculum.
          </p>
        </div>
        <span className="brand-mark">
          <Bot size={20} />
        </span>
      </header>
      <section className="copilot-panel">
        <div className="copilot-response">
          <Sparkles size={18} />
          <p>
            {copilot.answer ||
              "Ask a question to begin. Include a lesson, equation, or circuit detail for a more useful answer."}
          </p>
        </div>
        <div className="prompt-list">
          {suggestions.map((prompt) => (
            <button key={prompt} onClick={() => setMessage(prompt)}>
              {prompt}
            </button>
          ))}
        </div>
        <div className="depth-picker" role="group" aria-label="Answer depth">
          {depths.map((option) => (
            <button
              className={depth === option ? "active" : ""}
              key={option}
              onClick={() => setDepth(option)}
            >
              {option}
            </button>
          ))}
        </div>
        <label className="chat-input">
          <textarea
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                void ask();
              }
            }}
            placeholder="Ask about quantum computing..."
            aria-label="Question for Quantum Copilot"
          />
          <button
            onClick={() => void ask()}
            disabled={copilot.isAsking || !message.trim()}
            aria-label="Send question"
          >
            <Send size={17} />
          </button>
        </label>
        {copilot.error && <p className="api-error">{copilot.error}</p>}
        {copilot.model && (
          <small className="copilot-model">Model: {copilot.model}</small>
        )}
      </section>
    </main>
  );
}
