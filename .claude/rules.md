# Savior Systems Coding Rules

- **Zero Unchecked Permissions**: Any permission requests must be explicitly justified in `08.PLAY-POLICY-SAFETY.md`. Avoid background location or invasive sensors completely unless strictly required and justified.
- **Unique Style Schemes**: Base themes must use unique accent and background colors across different apps. Never reuse a single color file layout blindly.
- **Compose Preview Support**: Every composable screen must define a `@Preview` composable parameter.
- **Coroutines Best Practices**: Run database actions on `Dispatchers.IO` and UI updates on `Dispatchers.Main`.
- **Offline First**: All user actions execute locally in Room/DataStore. There are no cloud accounts.
- **Relative Linking**: All markdown files must link to each other using relative GitHub-compatible URLs, NOT absolute local paths.
- **Use Specific Tools**: Never use bash `cat` to create files or `grep` inside bash when specific tools (`write_to_file`, `grep_search`) exist. Utilize MCP tools to their maximum potential.
- **Artifacts First**: For heavy planning or reporting, utilize proper system artifacts (`implementation_plan`, `walkthrough`) instead of dropping raw text into the chat.
