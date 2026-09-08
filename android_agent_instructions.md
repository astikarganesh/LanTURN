# Android Application Implementation Guide (LanTURN)

**ATTENTION AI AGENT:** You are responsible for implementing the entire Android application. Do not ask the user to write Kotlin code. Inspect the project, implement the feature, build it, test it, and fix errors yourself.

## Project Overview

**LanTURN** is a placement platform connecting students looking for jobs and internships with employers looking to hire. It includes AI-powered career assistance using Google Gemini.

The project currently consists of a monorepo with:
- **Backend (`/backend`)**: Node.js + Express API.
- **Frontend (`/frontend`)**: React + Vite web app.

Your task is to build the **Native Android Application** using **Kotlin**. 

## Architecture & Integration Points

The Android app must not implement any complex backend business logic. It should function as a client for the existing Express REST API.

1. **API Base URL**: The backend runs locally at `http://localhost:8080/api` (or whichever URL is configured in the environment).
2. **Authentication**: 
   - Uses **Firebase Authentication**.
   - The Android app should use the Firebase Android SDK for Google Sign-In and standard email/password auth.
   - Once authenticated, the app must pass the Firebase ID Token in the `Authorization: Bearer <token>` header to all backend API calls.
3. **Database**: The backend uses **Firebase / Supabase**. The Android app must *never* connect to the database directly. Always use the REST API.
4. **Storage**: Resumes and profile images might be uploaded via Firebase Storage or Supabase Storage. The API provides endpoints to handle file uploads.
5. **Roles**: There are three user roles: `Student`, `Employer`, and `Admin`. The UI should adapt based on the authenticated user's role profile fetched from the API.

## Core Features to Implement

- **Authentication Flow**: Login/Signup using Firebase Auth.
- **Student Flow**:
  - Profile completion (Personal, Academic, Professional data).
  - Browse, search, and apply for jobs.
  - Track application status.
  - Interface for chatting with the AI Career Assistant (calls backend `/api/ai/*` endpoints).
- **Employer Flow**:
  - Company profile management.
  - Job posting and management.
  - Reviewing and accepting/rejecting applications.
- **Notifications**: Handle push notifications (Firebase Cloud Messaging) and in-app alerts.

## Workflow Instructions for the Agent

1. **Inspect**: Read the backend API routes (`backend/src/routes`) and API documentation in the `docs/` folder (like `API_SPECIFICATION.md`) to understand the exact endpoints, request bodies, and responses.
2. **Setup**: Initialize a standard Android Kotlin project using Gradle. Set up Retrofit for API calls, Firebase SDK for Auth, and a modern architecture (e.g., MVVM with Coroutines/Flow, Jetpack Compose for UI).
3. **Implement**: Build out the application screens and connect them to the backend API.
4. **Build & Test**: Compile the APK. If there are compilation or runtime errors, debug and fix them autonomously. 
5. **Autonomy**: Do not halt to ask the user to write code snippets. Deliver a fully working Android codebase that can run and build into an APK without breaking.
