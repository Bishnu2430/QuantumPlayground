# Media and Interactive Visuals Pipeline

Quantum Lab does not require every visual to be hand-authored frame by frame. The platform uses a layered asset strategy.

## Runtime interactive visuals

Interactive scenes should be implemented as reusable React components backed by normalized simulation data. Use Three.js through React Three Fiber for 3D scenes such as Bloch spheres, state-vector geometry, hardware topology, and quantum networks. Use regular SVG/Canvas/HTML for 2D circuit diagrams, probability charts, density matrices, timelines, and annotations.

## Declarative visualization specs

Lesson authors should reference declarative specs in `content/visualizations/`. A spec describes the concept, inputs, timeline, camera, annotations, and linked experiment. The frontend renderer turns the spec into an interactive component.

## Static images and videos

Static diagrams, illustrations, and historical media live under `content/images/` with metadata, then publishable app assets can be copied or generated into `apps/web/public/`. Videos live under `content/videos/` as scripts/storyboards/manifests first; rendered media can be added later when licensed or generated.

## Authoring rule

Create reusable templates once, then drive them from content metadata and simulation results. Manually create only the exceptional assets that need custom art direction.
