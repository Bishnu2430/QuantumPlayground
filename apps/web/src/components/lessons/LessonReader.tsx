"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { api, type Lesson } from "@/lib/api/client";
import { ArrowRight, Code2, Orbit } from "lucide-react";

function codeFrom(markdown: string) {
  return (
    markdown.match(/```python\s*([\s\S]*?)```/)?.[1]?.trim() ??
    "from qiskit import QuantumCircuit\n\nqc = QuantumCircuit(1, 1)\nqc.h(0)\nqc.measure(0, 0)\nprint(qc)"
  );
}

function circuitForLesson(lesson: Lesson) {
  const key = `${lesson.slug} ${lesson.title}`.toLowerCase();
  if (key.includes("bell") || key.includes("entangl"))
    return {
      numQubits: 2,
      numClbits: 2,
      operations: [
        { gate: "h", targets: [0], moment: 0 },
        { gate: "cx", controls: [0], targets: [1], moment: 1 },
        { gate: "measure", targets: [0, 1], clbits: [0, 1], moment: 2 },
      ],
    };
  if (
    key.includes("measurement") ||
    key.includes("born") ||
    key.includes("superposition")
  )
    return {
      numQubits: 1,
      numClbits: 1,
      operations: [
        { gate: "h", targets: [0], moment: 0 },
        { gate: "measure", targets: [0], clbits: [0], moment: 1 },
      ],
    };
  if (key.includes("pauli") || key.includes("bit flip"))
    return {
      numQubits: 1,
      numClbits: 1,
      operations: [
        { gate: "x", targets: [0], moment: 0 },
        { gate: "measure", targets: [0], clbits: [0], moment: 1 },
      ],
    };
  return {
    numQubits: 1,
    numClbits: 1,
    operations: [{ gate: "h", targets: [0], moment: 0 }],
  };
}

function renderBlock(block: string, index: number) {
  const value = block.trim();
  if (value.startsWith("```"))
    return (
      <pre className="lesson-code" key={index}>
        {value.replace(/^```\w*\s*/, "").replace(/```$/, "")}
      </pre>
    );
  if (value.includes("$$"))
    return (
      <pre className="lesson-equation" key={index}>
        {value.replace(/\$\$/g, "").trim()}
      </pre>
    );
  return <p key={index}>{value.replace(/[*`]/g, "").replace(/^- /gm, "")}</p>;
}

export function LessonReader({ slug }: { slug: string }) {
  const [lesson, setLesson] = useState<Lesson>();
  useEffect(() => {
    api
      .lesson(slug)
      .then(setLesson)
      .catch(() => setLesson(undefined));
  }, [slug]);
  if (!lesson)
    return (
      <main className="dashboard detail-page">
        <p className="eyebrow">Loading lesson</p>
        <h1>{slug.replaceAll("-", " ")}</h1>
        <p>Start the API to load the curated lesson content.</p>
        <Link className="secondary-button" href="/learn">
          Back to lessons
        </Link>
      </main>
    );
  const sections = lesson.content
    .replace(/^---[\s\S]*?---\s*/, "")
    .split(/(?=^## )/m)
    .filter(
      (section) =>
        section.trim() && !section.trim().startsWith(`# ${lesson.title}`),
    );
  const code = encodeURIComponent(codeFrom(lesson.content));
  const circuit = encodeURIComponent(JSON.stringify(circuitForLesson(lesson)));
  return (
    <main className="dashboard detail-page lesson-reader">
      <p className="eyebrow">
        {lesson.domain} · {lesson.module}
      </p>
      <h1>{lesson.title}</h1>
      <p>{lesson.description}</p>
      <div className="lesson-actions">
        <Link className="primary-button" href={`/laboratory?code=${code}`}>
          <Code2 size={16} /> Open Python lab
        </Link>
        <Link
          className="secondary-button"
          href={`/simulator?circuit=${circuit}`}
        >
          <Orbit size={16} /> Run circuit simulation
        </Link>
      </div>
      {sections.map((section, index) => {
        const lines = section.trim().split("\n");
        const heading = lines.shift()?.replace(/^##\s*/, "");
        return (
          <section className="lesson-section" key={`${heading}-${index}`}>
            <h2>{heading}</h2>
            {lines.join("\n").split("\n\n").map(renderBlock)}
          </section>
        );
      })}
      <Link className="underlined-link" href="/learn">
        Explore another lesson <ArrowRight size={16} />
      </Link>
    </main>
  );
}
