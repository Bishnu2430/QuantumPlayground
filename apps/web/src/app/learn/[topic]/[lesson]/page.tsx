import { LessonReader } from "@/components/lessons/LessonReader";

export default async function LessonPage({
  params,
}: {
  params: Promise<{ topic: string; lesson: string }>;
}) {
  const { topic, lesson } = await params;
  return <LessonReader slug={`${topic}-${lesson}`} />;
}
