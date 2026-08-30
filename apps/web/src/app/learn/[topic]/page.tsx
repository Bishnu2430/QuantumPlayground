export default async function TopicPage({ params }: { params: Promise<{ topic: string }> }) {
  const { topic } = await params;
  return <main className="p-10"><h1 className="text-3xl font-semibold">Topic: {topic}</h1></main>;
}
