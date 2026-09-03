"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Atom,
  BookOpen,
  FlaskConical,
  LayoutDashboard,
  MessageSquare,
  Orbit,
  Sparkles,
} from "lucide-react";
import { ThemeToggle } from "./ThemeToggle";
const links = [
  ["/dashboard", "Overview", LayoutDashboard],
  ["/learn", "Learn", BookOpen],
  ["/laboratory", "Laboratory", FlaskConical],
  ["/simulator", "Simulator", Orbit],
  ["/experiments", "Review", Atom],
  ["/copilot", "Copilot", MessageSquare],
] as const;
export function AppShell({ children }: { children: React.ReactNode }) {
  const path = usePathname();
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <Link href="/dashboard" className="brand">
          <span className="brand-mark">
            <Sparkles size={18} />
          </span>
          <span>
            quantum<span>lab</span>
          </span>
        </Link>
        <nav>
          {links.map(([href, label, Icon]) => (
            <Link
              className={path === href ? "nav-link active" : "nav-link"}
              href={href}
              key={href}
            >
              <Icon size={18} />
              <span>{label}</span>
            </Link>
          ))}
        </nav>
        <div className="sidebar-bottom">
          <ThemeToggle />
          <span className="status-dot" /> <small>Systems nominal</small>
        </div>
      </aside>
      <main className="page-content">{children}</main>
    </div>
  );
}
