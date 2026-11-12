# LanTURN

LanTURN is a full-stack career platform built to connect students, employers, and administrators in one ecosystem. The app helps students explore job opportunities, track applications, and build a professional profile, while employers can post openings, review applicants, and manage hiring workflows. Administrators oversee the system, moderation, and operational controls.

This repository is organized as a monorepo with a separate backend and frontend, making the platform easy to develop, test, and scale.

## Why this project exists

The goal of LanTURN is to simplify the hiring lifecycle:

- Students can discover relevant job roles and internships.
- Employers can quickly find suitable candidates.
- Institutions or admins can manage users, workflows, and platform health.
- The system is designed to support rapid local development with Firebase emulators and a production-ready API structure.

## Project overview

LanTURN is designed as a modern job marketplace and talent platform with role-based access.

### Student experience
- Browse open jobs and internships
- View role details and application requirements
- Apply with profile information and resume-based workflows
- Track application status and upcoming opportunities
- Receive notifications and updates from the platform

### Employer experience
- Post and manage job listings
- Review applicants and shortlist candidates
- Manage hiring pipelines and communications
- Monitor applicant engagement and status changes

### Admin experience
- Manage platform users and system access
- Monitor application data and user activity
- Control operational workflows and moderation requirements

## Tech stack

### Backend
- Node.js
- Express.js
- Firebase Admin SDK
- Supabase
- Zod for validation
- Pino for logging
- Helmet, CORS, rate limiting, and structured middleware

### Frontend
- React 18
- Vite
- Tailwind CSS
- Firebase Auth client SDK
- React Router
- React Query
- Framer Motion

### Infrastructure and tooling
- Firebase emulators for local development
- GitHub for version control
- Vercel-friendly frontend setup
- Monorepo structure with separate app modules

## Repository structure

```text
LanTURN/
├── backend/               # Express API + Firebase Admin + Supabase integration
├── frontend/              # React + Vite + Tailwind application
├── docs/                 # Project documentation and architecture notes
├── .gitignore
├── start-dev.bat         # Windows local startup helper
├── AGENTS.md             # Development workflow and repository guidance
├── README.md             # Project overview and onboarding
├── cors.json             # Firebase Storage CORS config
└── ...
```

## Architecture

The app follows a layered backend structure:

```text
routes -> controllers -> services -> repositories/clients
```

This separation keeps the codebase organized and makes it easier to extend features without tightly coupling logic across modules.

## Authentication model

The backend expects Firebase ID tokens in the Authorization header:

```http
Authorization: Bearer <firebase-id-token>
```

This ensures protected routes validate the user identity and load role-specific profile data before processing requests.

## Role-based access

The application supports multiple user roles:

- Student
- Employer
- Admin

Each role has different permissions and workflows, allowing the platform to behave like a real-world hiring platform rather than a single-user app.

## Local development

### Prerequisites

- Node.js 18+
- Firebase CLI
- Git

### Start Firebase emulators

From the repository root:

```bash
firebase emulators:start
```

### Start the backend

```bash
cd backend
cp .env.example .env
npm install
npm run seed
npm run dev
```

The backend runs at:

```text
http://localhost:8080/api
```

Health check:

```text
http://localhost:8080/api/health
```

### Start the frontend

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

The frontend runs at:

```text
http://localhost:5173
```

### Windows shortcut

You can also use:

```bat
start-dev.bat
```

## Demo users

The project includes emulator-based demo accounts for quick testing.

| Role | Email | Notes |
|------|-------|-------|
| Admin | admin@lanturn.dev | Platform administration |
| Employer | hr@acme.dev | Employer view |
| Employer | careers@globex.dev | Employer view |
| Student | asha@lanturn.dev | Student profile |
| Student | rahul@lanturn.dev | Student profile |
| Student | neha@lanturn.dev | Student profile |

## Environment configuration

### Backend
Copy the example config and customize the environment values:

```bash
cd backend
cp .env.example .env
```

The backend validates its environment variables at startup and uses emulator defaults for local development.

### Frontend
```bash
cd frontend
cp .env.example .env
```

Set Firebase emulator mode for development when needed.

## Features in detail

### For students
- Personalized job discovery experience
- Search and filter jobs
- View company and role details
- Apply to opportunities
- Monitor application status
- Resume-related workflow support
- Notification flow for updates and follow-ups

### For employers
- Job creation and publishing
- Applicant review workflows
- Candidate filtering and shortlisting
- Communication with applicants
- Hiring pipeline visibility

### For admins
- User management and onboarding controls
- Platform oversight
- Role-based access enforcement
- Operational monitoring

## Production readiness

The project is structured for progressive deployment. In production, Firebase emulator mode is disabled and real Firebase credentials are used. The backend and frontend are designed to support a deployment flow with proper environment configuration and service setup.

## Notes for contributors

- Keep frontend and backend concerns separated.
- Use the backend layer structure: routes → controllers → services → repositories.
- Prefer environment-based configuration rather than hardcoded credentials.
- Test local behavior with Firebase emulators before deploying.

## Summary

LanTURN is a career platform that merges job discovery, hiring workflows, and role-based access into one system. It is designed to be both developer-friendly and realistic in structure, making it suitable as a portfolio project, a real-world prototype, or a scalable platform foundation.

If you want, I can also help you create a more polished GitHub landing page version of this README with badges, screenshots placeholders, quick-start command blocks, and a project architecture diagram.
