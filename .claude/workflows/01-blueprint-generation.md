# Workflow: 01. App Blueprint Generation

This workflow defines the standard operating procedure for documenting a new app in the Savior Systems portfolio.

1. **Research Phase**: Conduct deep research into the app category, ASO keywords, Play Store policies, and required offline calculation math or architecture. Do not skip this step.
2. **Implementation Plan Artifact**: Propose an `implementation_plan` artifact outlining the strategy for the 14 documents to be created. Wait for auto-approval if operating aggressively.
3. **Drafting (Batch 1)**: Generate `01.PRD-REQUIREMENTS.md`, `02.UI-UX-DESIGN-SYSTEM.md`, `03.FUNCTIONAL-FLOWS.md`, `04.TECHNICAL-ARCHITECTURE.md`.
4. **Drafting (Batch 2)**: Generate `05.DATABASE-SCHEMA.md`, `06.ADMOB-MONETIZATION-MAP.md`, `07.ASO-PLAY-STORE-LISTING.md`, `08.PLAY-POLICY-SAFETY.md`.
5. **Drafting (Batch 3)**: Generate `09.TESTING-ASSURANCE-PLAN.md`, `10.TRANSLATIONS-LOCALIZATION.md`, `11.GRAPHIC-ASSETS-MANIFEST.md`, `12.LOGGING-ANALYTICS.md`, `13.BACKLOG-TASKS.md`, and the root `README.md`.
6. **Asset Generation**: Use the `generate_image` tool to create a premium, minimalist app icon matching the UI/UX spec. Save it to the app's directory.
7. **Git Operations**: Stage all changes (`git add -A`), commit with conventional commit format (`feat: ...`), and push to `main`.
8. **Walkthrough Artifact**: Generate a `walkthrough` artifact summarizing the deep research and documenting completion.
