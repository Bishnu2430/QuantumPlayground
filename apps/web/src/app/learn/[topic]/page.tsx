import { LessonReader } from "@/components/lessons/LessonReader";
export default async function TopicPage({
  params,
}: {
  params: Promise<{ topic: string }>;
}) {
  const { topic } = await params;
  return <LessonReader slug={topic} />;
}
