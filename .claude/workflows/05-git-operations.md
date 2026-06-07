# Workflow: 05. Git Operations Standard

Standard git operating procedure for all agents working in this repository.

---

## Commit Message Convention (Conventional Commits)

```
<type>(<scope>): <description>
```

### Types
| Type | When to Use |
| :--- | :--- |
| `feat` | Adding new documentation, features, or app blueprints. |
| `fix` | Fixing broken links, typos, or incorrect data. |
| `chore` | Updating `.claude/` configs, scripts, or infrastructure files. |
| `docs` | Updating existing documentation content (not creating new). |
| `refactor` | Restructuring files without changing content. |

### Scope
The scope should identify the app number and short name:
- `feat(06-water-log): Complete deep research & full documentation suite`
- `fix(all): Convert absolute file:/// links to relative paths`
- `chore(claude): Upgrade agent configuration`

---

## Branch Strategy
- **`main`**: The single source of truth. All work is committed directly to `main`.
- No feature branches are used during the documentation sprint phase.
- Feature branches will be introduced when code implementation begins.

---

## Push Protocol
1. Always `git add -A` to stage all changes.
2. Always `git commit` with a conventional commit message.
3. Always `git push origin main` immediately after committing.
4. Never leave uncommitted changes at the end of a work session.
