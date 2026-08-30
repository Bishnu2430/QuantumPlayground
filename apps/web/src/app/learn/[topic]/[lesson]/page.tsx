export default async function LessonPage({ params }: { params: Promise<{ topic: string; lesson: string }> }) {
  const { topic, lesson } = await params;
  return <main className="p-10"><h1 className="text-3xl font-semibold">{topic} / {lesson}</h1></main>;
}
