"use client";
import { ThemeToggle } from "@/components/app/ThemeToggle";
export default function Settings() {
  return (
    <div className="dashboard">
      <header className="topbar">
        <div>
          <p className="eyebrow">Preferences</p>
          <h1>Workspace settings</h1>
        </div>
      </header>
      <section className="recent-card settings-card">
        <div>
          <div>
            <p className="eyebrow">Appearance</p>
            <h2>Color theme</h2>
            <p>
              Choose a light or dark interface. Your preference is saved in this
              browser.
            </p>
          </div>
          <ThemeToggle />
        </div>
      </section>
    </div>
  );
}
