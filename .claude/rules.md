# Savior Systems Coding Rules

- **Zero Unchecked Permissions**: Any permission requests must be explicitly justified in `08.PLAY-POLICY-SAFETY.md`. Avoid background location or invasive sensors completely unless strictly required and justified.
- **Unique Style Schemes**: Base themes must use unique accent and background colors across different apps. Never reuse a single color file layout blindly.
- **Compose Preview Support**: Every composable screen must define a `@Preview` composable parameter.
- **Coroutines Best Practices**: Run database actions on `Dispatchers.IO` and UI updates on `Dispatchers.Main`.
- **Offline First**: All user actions execute locally in Room/DataStore. There are no cloud accounts.
- **Relative Linking**: All markdown files must link to each other using relative GitHub-compatible URLs, NOT absolute local paths.
- **Use Specific Tools**: Never use bash `cat` to create files or `grep` inside bash when specific tools (`write_to_file`, `grep_search`) exist. Utilize MCP tools to their maximum potential.
- **Artifacts First**: For heavy planning or reporting, utilize proper system artifacts (`implementation_plan`, `walkthrough`) instead of dropping raw text into the chat.
- **Zero Research Gaps & World-Class Documentation**: Every blueprint document must undergo deep research and analysis before generation. Documentation must be clean, highly organized, easy to navigate, and thoroughly interlinked. Technical blueprints must contain production-ready, fully-explained architectures and code structures (Kotlin, Room, Glance, etc.) so that developers can implement them immediately without skipping sections or guessing logic.
- **High-Velocity Monetization Guardrails**: Since the goal is high-yield publishing, documentations must detail robust eCPM setups, strict Google Play policy safety checklists to prevent account bans, and clear, non-disruptive AdMob placement plans (like native listing ads and 180s interstitial cooldowns).
- **Document Integrity & Markdown Formatting**: Do not produce malformed Markdown files. Specifically: 
  - Never wrap multiline code blocks (like directory trees) in single backticks (`` ` ``). Always use standard triple backticks (`` ``` ``).
  - Do not introduce `Null Bytes` (`\x00`), Byte Order Marks (BOM), or Mojibake double-encoded characters.
  - Never generate single-byte or empty blueprint files.
  - Never execute global regex search-and-replace scripts across the entire workspace to fix minor formatting issues, as it causes severe corruption. Use targeted fixes instead.
  - Always run `.\update_all_docs.ps1` to trigger `scripts/audit_workspace.py`. If the CI/CD audit fails, fix the malformed files immediately.
