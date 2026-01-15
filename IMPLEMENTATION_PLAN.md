# PRAXIS 5652 Blueprint Implementation Plan

## Phase 0 — Repository survey & spec alignment (static)
- Review `Blueprint Specification.md` to confirm required directory structure, module names, DB schema, Gemini prompt requirements, and UI rules.
- Identify reference files present in repo root: `5652_objectives.md`, `MCQs.md`, and `pseduocode_def.md`.
- **Filename normalization decision:** the spec expects `pseudocode_def.md`, but the repository provides `pseduocode_def.md` (typo). In the implementation, the file will be copied into `praxis_blueprint/praxis_data/` as `pseudocode_def.md` to match the spec and code references, while keeping the original source file untouched.
- Confirm blueprint root folder will be `praxis_blueprint/` and assets/templates will be strictly namespaced under `praxis_quiz_2/` per spec.

## Phase 1 — Blueprint skeleton + database scaffolding (non-AI)
- Create `praxis_blueprint/__init__.py` with main blueprint registration, DB init hook, and sub-blueprint registration.
- Add `praxis_blueprint/db.py` with `get_db`, `query_db`, `init_db` using sqlite3 + Flask `g`.
- Add `praxis_blueprint/schema.sql` with tables specified in the spec.
- Add `praxis_blueprint/main_routes.py` with basic dashboard/builder routes and template rendering.
- Add `praxis_blueprint/quiz_delivery/__init__.py` and `delivery_routes.py` with a minimal active quiz route.
- Copy reference files into `praxis_blueprint/praxis_data/` using the normalized `pseudocode_def.md` name.
- Add minimal templates and static assets under `templates/praxis_quiz_2/` and `static/praxis_quiz_2/`.

## Phase 2 — Quiz delivery parsing + UI basics (non-AI)
- Implement `quiz_delivery/content_parser.py` for JSON validation, markdown rendering, and code snippet wrapper.
- Implement `active_quiz.html` and `results.html` templates.
- Add `quiz_engine.js` stubs for timer/state management.
- Implement `syntax_highlighter.js` tokenizer rules based on `pseudocode_def.md`.

## Phase 3 — Gemini SDK integration (context caching)
- Implement `utils_ai.py` using `google-genai` with cached context (`praxis-context-cache`) and 1-hour TTL.
- Provide `generate_questions` and `explain_answer` helpers following the strict prompt formats.
- Initialize or refresh cache within blueprint init.

## Phase 4 — Quiz creation flow + persistence
- Builder POST creates questions via AI, validates content, stores in DB.
- Add quiz creation and attempts persistence with active quiz flow.
- Add AJAX endpoint for answer submissions and scoring.

## Phase 5 — UI polish + design system compliance
- Style updates for sharp corners, palette, buttons, and code blocks.
- Layout and typography alignment with “Blueprint Technical”.

## Phase 6 — Robustness & edge cases
- Guardrails for malformed AI responses and safe failure paths.
- Safe DB initialization (`IF NOT EXISTS`) and cache refresh strategy.

