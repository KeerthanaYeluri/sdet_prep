# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repo contains two distinct things:

1. **GrowthPath** (`interview/`) — An adaptive technical interview preparation platform with a Flask backend + React/Vite frontend. This is the primary active project.
2. **Practice scripts** (root-level `.py` files, `top_50_questions_book/`) — Standalone Python exercises (BookMyShow automation, algorithm practice, etc.). These are unrelated to GrowthPath.

## GrowthPath Architecture

### Backend (`interview/backend/`)

- **Flask app** (`app.py`) — Monolithic REST API (~70+ endpoints) serving all routes + static frontend files via a catch-all route. CORS enabled globally.
- **Auth** — JWT tokens (24-hour expiry) via `Authorization: Bearer <token>` header. Three decorators: `@auth_required`, `@auth_optional`, `@hr_required`. User ID stored in `g.user_id` during request lifecycle.
- **Storage** (`storage.py`) — Dual-mode persistence: PostgreSQL (production via `DATABASE_URL`) or SQLite with WAL mode (local dev). SQL abstraction auto-translates `?` → `%s` for PostgreSQL. JSON fields stored as strings, parsed on read via `_parse_json_field()`. Schema migrations use a versioned `_migrate_users_v2()` pattern.
- **LLM Service** (`llm_service.py`) — Multi-provider with automatic fallback: Claude (`claude-sonnet-4-20250514`), OpenAI (`gpt-4o`), Gemini (`gemini-2.0-flash`). Provider availability detected at runtime. Unified interface: `call_llm(messages, system_prompt, max_tokens, preferred_provider)`. Also reads `.env` file.
- **ELO System** (`elo_rating.py`) — Dual rating: overall ELO + sub-ELOs per round type (phone_screen, system_design, behavioral, domain_specific, bar_raiser). K-factors vary by session type (32 full mock, 40 quick assessment, 8 targeted practice). Difficulty mapping: easy→1200, medium→1500, hard→1800, expert→2100.
- **Other modules**: `question_bank.py` / `topic_questions.py` (question catalog by role/topic/difficulty), `scorer.py` / `dual_scorer.py` (answer evaluation), `mock_engine.py` (mock interview sessions), `ai_interviewer.py` (conversational AI interviewer), `gap_map.py` (skill gap analysis), `quick_assessment.py` (rapid skill evaluation), `company_profiles.py` (company-specific interview prep)

**Key API endpoint groups:** `/api/auth/*`, `/api/config/*`, `/api/elo`, `/api/gap-map`, `/api/quick-assessment/*`, `/api/mock/*`, `/api/conversation/*`, `/api/learning/*`, `/api/assessment/topic/*`, `/api/session/*`, `/api/hr/*`

### Frontend (`interview/frontend-v2/`)

- React 19 + TypeScript + Vite + Tailwind CSS
- **Routing**: State-based (not React Router). Screen states: dashboard, learning, interview, ai-interview, mock, assessment, profile, history, review
- **Auth pattern**: JWT stored in `localStorage` as `gp_token`, user object as `gp_user`. `authHeaders()` utility injects Bearer token. `apiFetch()` wrapper auto-handles 401 by clearing auth and reloading.
- **Auth flow in App.tsx**: `checking` → `login`/`register` → `change_password` → `quick_assessment` → `authenticated`
- **Path alias**: `@/` → `./src/` (configured in tsconfig + vite)
- **Component library**: Radix UI primitives, Framer Motion animations, Lucide icons
- Legacy frontend in `interview/frontend/` (plain HTML/JS, fallback if `frontend-v2/dist/` missing)

### Data Flow

Flask serves the built frontend from `frontend-v2/dist/` (falls back to `frontend/`). Vite dev server proxies `/api` → `http://localhost:5000` during local development. All API calls go through Flask.

## Commands

### Backend
```bash
cd interview/backend
pip install -r requirements.txt
python app.py                    # Local dev server (port 5000)
gunicorn app:app --bind 0.0.0.0:5000  # Production-style
```

### Frontend (v2)
```bash
cd interview/frontend-v2
npm install
npm run dev      # Vite dev server (proxies /api to Flask)
npm run build    # Production build to dist/
npm run lint     # ESLint (flat config v9+)
```

### Tests
```bash
cd interview/backend
python -m pytest tests/                      # All tests
python -m pytest tests/test_elo.py           # Single test file
python -m pytest tests/test_elo.py -k "test_name"  # Single test
```

### Deployment

**Render** (primary, config in `interview/render.yaml`):
- Build: `cd frontend-v2 && npm install && npx vite build && cd ../backend && pip install -r requirements.txt`
- Start: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
- Node 20 + Python 3.11, persistent disk at `/opt/render/project/src/backend/data` (1GB)

**PythonAnywhere** (alternative, see `interview/DEPLOY.md`):
- WSGI entry point via `wsgi.py`, manual setup, static files served separately

## Environment Variables
- `JWT_SECRET` — JWT signing key (required in production, auto-generated on Render)
- `DATABASE_URL` — PostgreSQL connection string (omit for SQLite local dev)
- `GEMINI_API_KEY` — Google Gemini API key (or `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` — any one LLM provider suffices)

## BMAD Method Integration

When the user invokes any `/bmad-*` command, read and follow the corresponding SKILL.md file.

### Available Commands

- `/bmad-help` — Read and follow `_bmad/core/skills/bmad-help/SKILL.md`
- `/bmad-party-mode` — Read and follow `_bmad/core/skills/bmad-party-mode/SKILL.md`
- `/bmad-brainstorming` — Read and follow `_bmad/core/skills/bmad-brainstorming/SKILL.md`
- `/bmad-create-prd` — Read and follow `_bmad/core/tasks/bmad-create-prd/SKILL.md`
- `/bmad-advanced-elicitation` — Read and follow `_bmad/core/skills/bmad-advanced-elicitation/SKILL.md`
- `/bmad-distillator` — Read and follow `_bmad/core/skills/bmad-distillator/SKILL.md`
- `/bmad-editorial-review-prose` — Read and follow `_bmad/core/skills/bmad-editorial-review-prose/SKILL.md`
- `/bmad-editorial-review-structure` — Read and follow `_bmad/core/skills/bmad-editorial-review-structure/SKILL.md`
- `/bmad-index-docs` — Read and follow `_bmad/core/skills/bmad-index-docs/SKILL.md`
- `/bmad-review-adversarial-general` — Read and follow `_bmad/core/skills/bmad-review-adversarial-general/SKILL.md`
- `/bmad-review-edge-case-hunter` — Read and follow `_bmad/core/skills/bmad-review-edge-case-hunter/SKILL.md`
- `/bmad-shard-doc` — Read and follow `_bmad/core/skills/bmad-shard-doc/SKILL.md`
- `/bmad-init` — Read and follow `_bmad/core/bmad-init/SKILL.md`

### BMAD Agents

Custom agents are defined in `_bmad/_config/agents/`. The agent manifest is at `_bmad/_config/agent-manifest.csv`. When loading an agent, read its markdown file and adopt its persona, communication style, and principles.

### BMAD Configuration

- Config: `_bmad/core/config.yaml`
- User: renu
- Communication language: English
- Output folder: `_bmad-output/`