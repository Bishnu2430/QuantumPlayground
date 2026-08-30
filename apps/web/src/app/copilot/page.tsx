import Link from "next/link";

const sections = ["learn","laboratory","simulator","experiments","algorithms","playground","copilot","dashboard","settings"];

export default function Page() {
  return (
    <main className="min-h-screen p-10">
      <h1 className="text-4xl font-semibold">Copilot</h1>
      <p className="mt-3 max-w-2xl text-muted-foreground">Copilot workspace scaffold.</p>
      <div className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {sections.map((section) => (
          <Link className="rounded-xl border p-4 hover:bg-muted" href={`/${section}`} key={section}>{section}</Link>
        ))}
      </div>
    </main>
  );
}
