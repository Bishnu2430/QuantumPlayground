import type { Metadata } from "next";
import "./globals.css";
import { AppShell } from "@/components/app/AppShell";
export const metadata: Metadata = { title: "Quantum Lab", description: "AI-native interactive quantum computing learning environment." };
export default function RootLayout({ children }: LayoutProps<"/">) { return <html lang="en" suppressHydrationWarning><body><AppShell>{children}</AppShell></body></html>; }
