"use client";
import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";
function preferredDark() { return typeof window !== "undefined" && (localStorage.theme === "dark" || (!localStorage.theme && matchMedia("(prefers-color-scheme: dark)").matches)); }
export function ThemeToggle() {
 const [dark, setDark] = useState(preferredDark);
 useEffect(() => { document.documentElement.classList.toggle("dark", dark); }, [dark]);
 const toggle = () => { setDark(value => { const next = !value; localStorage.theme = next ? "dark" : "light"; return next; }); };
 return <button className="icon-button" onClick={toggle} aria-label="Toggle color theme">{dark ? <Sun size={18} /> : <Moon size={18} />}</button>;
}
