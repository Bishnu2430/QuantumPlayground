"use client";

import { Canvas } from "@react-three/fiber";

export function BlochSphere() {
  return <div className="h-64 rounded-xl border"><Canvas><ambientLight intensity={0.6} /><mesh><sphereGeometry args={[1,32,32]} /><meshStandardMaterial wireframe color="#7dd3fc" /></mesh></Canvas></div>;
}
