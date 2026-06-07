# CLAUDE.md - Savior Systems AI Agent Guide

## Core Mission
*   **Context**: Building a portfolio of 30 isolated, high-performance, strictly offline Android utility apps for Savior Systems.
*   **Tech Stack**: Kotlin, Jetpack Compose (Material 3), Clean Architecture (MVVM), Room Database, Hilt, Jetpack Datastore, AdMob, Firebase Analytics.
*   **Compliance & Privacy**: 100% offline-first approach. Zero backend syncing of PII. Strict Play Store Data Safety compliance.

## Project Structure & Blueprint Requirements
*   Every application resides in its own numbered directory (e.g., `01. FocusPulse Timer/`).
*   **The 14-Document Standard**: Every app must have exactly 14 detailed markdown blueprints generated before implementation (PRD, UI/UX, Flows, Architecture, DB Schema, Monetization, ASO, Policy, QA, Localization, Assets, Logging, Backlog, and a master README).
*   **Dynamic UI Designs**: Interfaces must feel premium, modern, and "wow" the user (avoid basic/generic layouts). Use animations, gradients, and micro-interactions.

## Execution Rules
*   All code generated must be production-ready, compiling, and fully localized into `strings.xml`.
*   Never use placeholders for UI assets; generate them using the `generate_image` tool.
*   Links in documentation MUST use GitHub-compatible relative paths (e.g. `[PRD-REQUIREMENTS.md](01.PRD-REQUIREMENTS.md)`), NEVER absolute `file:///` paths.
*   Automate git workflows (stage, commit, push) seamlessly after completing a project milestone.
