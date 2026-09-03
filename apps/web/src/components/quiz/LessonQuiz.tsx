"use client";

import { useEffect, useState } from "react";
import { api, type Lesson } from "@/lib/api/client";
import { Check, RotateCcw } from "lucide-react";

export function LessonQuiz() {
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [selected, setSelected] = useState<Record<string, string>>({});
  const [checked, setChecked] = useState(false);
  useEffect(() => {
    api
      .lessons()
      .then(setLessons)
      .catch(() => setLessons([]));
  }, []);
  const questions = lessons
    .slice(0, 12)
    .map((lesson) => ({
      lesson,
      answer: lesson.content.includes("amplitudes")
        ? "amplitudes"
        : "simulation",
    }));
  return (
    <main className="dashboard quiz-page">
      <header className="topbar">
        <div>
          <p className="eyebrow">Practice studio</p>
          <h1>Lesson review</h1>
          <p className="catalog-copy">
            Choose one answer for each lesson you have studied, then check your
            understanding.
          </p>
        </div>
        <button
          className="secondary-button"
          onClick={() => {
            setSelected({});
            setChecked(false);
          }}
        >
          <RotateCcw size={16} /> Reset
        </button>
      </header>
      <section className="quiz-list">
        {questions.length ? (
          questions.map(({ lesson, answer }, index) => (
            <article className="quiz-card" key={lesson.slug}>
              <p className="eyebrow">
                {index + 1} · {lesson.domain}
              </p>
              <h2>What should guide your understanding of {lesson.title}?</h2>
              <div className="quiz-options">
                {[
                  "intuition only",
                  "amplitudes and probabilities",
                  "a random guess",
                  "a deterministic simulator result",
                ].map((option) => (
                  <label
                    key={option}
                    className={
                      checked && selected[lesson.slug] === option
                        ? option.includes(answer)
                          ? "correct"
                          : "incorrect"
                        : ""
                    }
                  >
                    <input
                      type="radio"
                      name={lesson.slug}
                      value={option}
                      checked={selected[lesson.slug] === option}
                      onChange={() =>
                        setSelected({ ...selected, [lesson.slug]: option })
                      }
                    />
                    {option}
                  </label>
                ))}
              </div>
            </article>
          ))
        ) : (
          <div className="catalog-empty">
            Start the API to load lesson review questions.
          </div>
        )}
      </section>
      <button
        className="primary-button"
        onClick={() => setChecked(true)}
        disabled={!questions.length}
      >
        <Check size={16} /> Check answers
      </button>
    </main>
  );
}
