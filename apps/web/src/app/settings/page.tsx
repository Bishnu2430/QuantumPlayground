"use client";
import { ThemeToggle } from "@/components/app/ThemeToggle";
export default function Settings() { return <div className="dashboard"><header className="topbar"><div><p className="eyebrow">Preferences</p><h1>Make it yours.</h1></div></header><section className="recent-card settings-card"><div><div><p className="eyebrow">Appearance</p><h2>Color theme</h2><p>Switch between the soft Nordic light and dark palettes. Your choice is saved in this browser.</p></div><ThemeToggle/></div></section></div>; }
