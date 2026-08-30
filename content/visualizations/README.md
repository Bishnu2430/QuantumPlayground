# Content Visualizations

This directory contains renderer-agnostic visual specifications. The frontend should consume these files and render them with reusable components rather than hand-building every visual per lesson.

## Renderer types

- `scene3d`: React Three Fiber / Three.js interactive scene.
- `diagram2d`: SVG/Canvas/HTML diagram.
- `graph`: chart or plotted mathematical/computational data.
- `equation`: KaTeX/MathJax equation panel with annotations.
- `circuit`: visual Quantum IR circuit plus simulator controls.
- `codeRunner`: Python/Qiskit code execution panel.
- `videoStoryboard`: script, shots, narration, and render notes.

All specs reference `visualizations/theme/nord-matte.yaml` for consistent light/dark styling.
