# 🗂️ Job Application Tracker — Project Roadmap

## Overview
A full-stack job application tracking tool built with React, FastAPI, and PostgreSQL.
Designed as both a portfolio piece and a practical tool for managing a job search.

---

## Tech Stack
| Layer | Tech |
|---|---|
| Frontend | React, Tailwind CSS, Redux |
| Backend | FastAPI (Python), uv (package manager) |
| Database | PostgreSQL (hosted on Supabase) |
| Testing | Pytest (backend), Playwright (E2E) |
| Deployment | Vercel (frontend), Render (backend), Supabase (DB) |

---

## Phase 1 — Project Setup
- [x] Initialize Git repo with a clean `.gitignore`
- [x] Scaffold `frontend/` with Vite + React + **TypeScript** + Tailwind CSS
- [ ] Install `uv` and initialize backend Python project (`uv init`)
- [ ] Scaffold `backend/` with FastAPI project structure using `uv`
- [ ] Add dependencies via `uv add fastapi uvicorn sqlalchemy asyncpg python-dotenv`
- [ ] Create a Supabase project and grab the connection string
- [ ] Set up `.env` files for frontend and backend (store Supabase URL + keys)
---

## Phase 2 — Backend (FastAPI + PostgreSQL)
- [ ] Connect FastAPI to Supabase PostgreSQL using SQLAlchemy + asyncpg
- [ ] Create `applications` table migration/schema
- [ ] Define SQLAlchemy models (`Application`)
- [ ] Define Pydantic schemas for request/response validation
- [ ] Build CRUD endpoints:
  - `GET /applications` — list all applications
  - `POST /applications` — create new application
  - `GET /applications/{id}` — get single application
  - `PUT /applications/{id}` — update application
  - `DELETE /applications/{id}` — delete application
- [ ] Add filtering by status/company on list endpoint
- [ ] Write Pytest unit tests for all endpoints
- [ ] Test API manually with Swagger UI (`/docs`)
---

## Phase 3 — Frontend Shell (React)
- [ ] Set up React Router with the following pages:
  - `/` — Dashboard
  - `/kanban` — Kanban Board
  - `/applications` — Table/List View
  - `/applications/new` — Add New Application
  - `/applications/:id` — Application Detail/Edit
- [ ] Set up Redux store with `applicationsSlice`
- [ ] Set up Axios instance with base URL from `.env`
- [ ] Build reusable components:
  - `Navbar`
  - `ApplicationCard`
  - `StatusBadge`
  - `ApplicationForm`
  - `Modal`
---

## Phase 4 — Connect Frontend to Backend
- [ ] Wire up Redux thunks/actions to FastAPI endpoints
- [ ] Implement create, read, update, delete from the UI
- [ ] Handle loading states and error messages
- [ ] Add form validation on `ApplicationForm`
---

## Phase 5 — Kanban Board
- [ ] Install `@dnd-kit/core` and `@dnd-kit/sortable`
- [ ] Build 5 columns: Applied, Phone Screen, Interview, Offer, Rejected
- [ ] Render `ApplicationCard` components in each column
- [ ] Implement drag-and-drop to update status
- [ ] Persist status changes to the backend on drop
---

## Phase 6 — Table / List View
- [ ] Build sortable table (by date, company, status)
- [ ] Add filter bar (by status, date range)
- [ ] Add search by company or role name
- [ ] Add pagination or infinite scroll
---

## Phase 7 — Dashboard & Stats
- [ ] Install `Recharts`
- [ ] Build stat cards:
  - Total applications
  - Response rate (%)
  - Interview conversion rate (%)
  - Offers received
- [ ] Build charts:
  - Applications over time (line chart)
  - Applications by status (pie/donut chart)
- [ ] Show most recent activity feed
