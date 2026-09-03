import Link from "next/link";
import { ArrowUpRight, Atom, BookOpen, Play, Sparkles } from "lucide-react";
const cards = [
  {
    icon: BookOpen,
    label: "Learning path",
    value: "01",
    text: "Start with superposition",
    href: "/learn",
  },
  {
    icon: Atom,
    label: "Experiments",
    value: "12",
    text: "Ready to explore",
    href: "/experiments",
  },
  {
    icon: Sparkles,
    label: "Copilot",
    value: "AI",
    text: "Always on hand",
    href: "/copilot",
  },
];
export default function Dashboard() {
  return (
    <div className="dashboard">
      <header className="topbar">
        <div>
          <p className="eyebrow">Quantum Lab workspace</p>
          <h1>
            Make the invisible <em>observable.</em>
          </h1>
        </div>
        <Link className="primary-button" href="/laboratory">
          <Play size={16} /> Open laboratory
        </Link>
      </header>
      <section className="hero">
        <div>
          <span className="eyebrow">
            <span className="status-dot" /> Recommended focus
          </span>
          <h2>
            Entanglement,
            <br />
            made tangible.
          </h2>
          <p>
            Build a Bell-state circuit, run it, and compare the measured results
            with the mathematical prediction.
          </p>
          <Link
            href="/learn/introduction/first-qiskit-circuit"
            className="underlined-link"
          >
            Open the lesson <ArrowUpRight size={16} />
          </Link>
        </div>
        <div className="orbital">
          <div className="orbit o1" />
          <div className="orbit o2" />
          <div className="core" />
          <i className="particle p1" />
          <i className="particle p2" />
        </div>
      </section>
      <section className="metric-grid">
        {cards.map(({ icon: Icon, label, value, text, href }) => (
          <Link href={href} className="metric-card" key={label}>
            <Icon size={19} />
            <div>
              <p>{label}</p>
              <h3>{value}</h3>
              <span>{text}</span>
            </div>
            <ArrowUpRight size={17} />
          </Link>
        ))}
      </section>
      <section className="recent-card">
        <div>
          <div>
            <p className="eyebrow">Continue learning</p>
            <h2>Quantum gates and interference</h2>
            <p>
              Understand how simple operations produce measurable quantum
              behavior.
            </p>
          </div>
          <Link className="secondary-button" href="/learn">
            Browse lessons <ArrowUpRight size={16} />
          </Link>
        </div>
        <div className="progress-track">
          <i />
        </div>
      </section>
    </div>
  );
}
