export default async function DetailPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return <main className="p-10"><h1 className="text-3xl font-semibold">Experiments: {slug}</h1></main>;
}
