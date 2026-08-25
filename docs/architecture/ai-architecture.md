# AI Architecture

**Status:** Draft baseline  
**Purpose:** Domain-specific quantum tutoring, experimentation, debugging, generation, and personalized guidance

## 1. Design principle

The AI is an orchestration layer over trusted content and deterministic computational tools. It is not the quantum simulator and should not be treated as the authoritative calculator.

## 2. Agent capabilities

The initial agent should support:

- explain concepts;
- adjust explanation depth;
- answer follow-up questions;
- search curated quantum knowledge;
- inspect the current circuit;
- inspect code;
- run a simulation;
- compare simulation results;
- generate Qiskit code;
- propose or apply circuit edits;
- debug circuits/code;
- suggest experiments;
- create quizzes/hints;
- summarize lessons;
- generate spoken lesson narration.

## 3. Agent context

The context builder should assemble only what is relevant:

```text
User question
+ current lesson
+ selected text/equation
+ current circuit
+ current code
+ latest simulation result
+ learner skill profile
+ retrieved sources
+ tool results
```

This makes answers more precise and reduces unnecessary token use.

## 4. RAG architecture

```text
Curated sources
    ↓
Parser / cleaner
    ↓
Chunker + metadata
    ↓
Embedding
    ↓
PostgreSQL + pgvector
    ↓
Retriever
    ↓
Optional reranker
    ↓
Context builder
    ↓
LLM
```

Store citation metadata with every chunk so that the agent can produce source-aware answers.

## 5. Knowledge hierarchy

Use multiple kinds of sources:

1. canonical scientific references and textbooks licensed for use;
2. open educational resources;
3. peer-reviewed papers and preprints where legally permitted;
4. official framework documentation;
5. first-party platform explanations authored by the project team.

Popular science sources can provide intuition and historical context but should not be used as the only authority for formal claims.

## 6. Tool interface

Recommended tools:

```text
search_knowledge(query)
get_concept(id)
inspect_circuit(circuit)
validate_circuit(circuit)
run_simulation(circuit, options)
get_statevector(result_id)
get_probabilities(result_id)
generate_qiskit(circuit)
parse_qiskit(code)
modify_circuit(circuit, operations)
suggest_experiment(context)
get_learner_profile(user_id)
```

Tools should return structured data.

## 7. Guardrails

The agent should:

- distinguish scientific fact from interpretation;
- state uncertainty where appropriate;
- never fabricate simulation outcomes;
- never claim to have run code unless a tool returned a result;
- avoid presenting speculative quantum claims as established fact;
- preserve source attribution for retrieved material;
- refuse or redirect unsafe code execution requests.

## 8. Explanation depth

The agent should expose a conceptual depth control:

`Intuitive → Undergraduate → Mathematical → Formal/Research`

The same concept should be explainable at all levels.

## 9. AI-driven circuit changes

AI should propose edits as structured operations, not raw source-code diffs when working with the visual circuit. The UI should show an approval step before destructive changes.

Example:

```json
{
  "operation": "add_gate",
  "gate": "h",
  "targets": [0],
  "moment": 1
}
```

## 10. Evaluation

Build a domain test set containing:

- conceptual questions;
- mathematical derivations;
- circuit debugging tasks;
- code-generation tasks;
- result-interpretation tasks;
- hallucination traps;
- citation/grounding tasks.

Evaluate correctness separately from style and helpfulness.
