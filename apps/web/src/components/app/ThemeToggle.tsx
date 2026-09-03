"use client";
import { Moon, Sun } from "lucide-react";
import { useEffect, useSyncExternalStore } from "react";
function preferredDark() {
  return (
    typeof window !== "undefined" &&
    (localStorage.theme === "dark" ||
      (!localStorage.theme &&
        matchMedia("(prefers-color-scheme: dark)").matches))
  );
}
function subscribe(onChange: () => void) {
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  media.addEventListener("change", onChange);
  window.addEventListener("quantum-theme-change", onChange);
  return () => {
    media.removeEventListener("change", onChange);
    window.removeEventListener("quantum-theme-change", onChange);
  };
}
export function ThemeToggle() {
  const dark = useSyncExternalStore(subscribe, preferredDark, () => false);
  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);
  const toggle = () => {
    localStorage.theme = dark ? "light" : "dark";
    window.dispatchEvent(new Event("quantum-theme-change"));
  };
  return (
    <button
      className="icon-button"
      onClick={toggle}
      aria-label="Toggle color theme"
    >
      {dark ? <Sun size={18} /> : <Moon size={18} />}
    </button>
  );
}
