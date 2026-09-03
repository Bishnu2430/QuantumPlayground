"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { api } from "@/lib/api/client";
import {
  ArrowUpRight,
  BookOpen,
  FlaskConical,
  LoaderCircle,
} from "lucide-react";
type Item = {
  slug: string;
  title?: string;
  description?: string;
  domain?: string;
  module?: string;
  difficulty?: number;
  qubits?: number;
};
const configs = {
  learn: {
    title: "Learn quantum computing.",
    copy: "Structured lessons with theory, mathematics, visual explanations, and runnable examples.",
    icon: BookOpen,
    load: async () => api.lessons(),
  },
  experiments: {
    title: "Review your learning.",
    copy: "Revisit concepts and practice applying them to quantum programs.",
    icon: FlaskConical,
    load: async () => (await api.experiments()).items,
  },
  algorithms: {
    title: "Algorithms, decoded.",
    copy: "See essential quantum algorithms as small, runnable systems.",
    icon: ArrowUpRight,
    load: async () => (await api.algorithms()).items,
  },
};
export function ResourceCatalog({
  kind,
}: {
  kind: "learn" | "experiments" | "algorithms";
}) {
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const config = configs[kind];
  const Icon = config.icon;
  useEffect(() => {
    config
      .load()
      .then(setItems)
      .catch(() => {
        setItems([]);
        setError(true);
      })
      .finally(() => setLoading(false));
  }, [config]);
  return (
    <div className="dashboard">
      <header className="topbar">
        <div>
          <p className="eyebrow">Quantum library</p>
          <h1>{config.title}</h1>
          <p className="catalog-copy">{config.copy}</p>
        </div>
      </header>
      <section className="catalog-grid">
        {loading ? (
          <div className="catalog-empty">
            <LoaderCircle className="spin" /> Loading from the API…
          </div>
        ) : items.length ? (
          items.map((item) => (
            <Link
              className="catalog-card"
              href={
                kind === "learn"
                  ? `/learn/${item.domain}/${item.slug.replace(`${item.domain}-`, "")}`
                  : `/${kind}/${item.slug}`
              }
              key={item.slug}
            >
              <Icon size={20} />
              <p className="eyebrow">
                {item.domain ??
                  (item.qubits ? `${item.qubits} qubits` : "Interactive study")}
              </p>
              <h2>{item.title ?? item.slug.replaceAll("-", " ")}</h2>
              <span>
                {item.description ??
                  "Open this resource and continue in the laboratory."}
              </span>
              <ArrowUpRight size={17} />
            </Link>
          ))
        ) : error ? (
          <div className="catalog-empty">
            The content service is unavailable. Start the API, then refresh this
            page.
          </div>
        ) : (
          <div className="catalog-empty">
            No items are published yet. Start the API and ingest lesson content
            to populate this view.
          </div>
        )}
      </section>
    </div>
  );
}
