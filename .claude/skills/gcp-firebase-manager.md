# Skill: GCP & Firebase Resource Manager

## Purpose
Interacts with Google Cloud Platform and Firebase using `gcloud` CLI and MCP server tools to manage project resources.

## When to Use
- When setting up Firebase apps for new projects.
- When checking enabled APIs on the GCP project.
- When managing service accounts or credentials.

## Available GCP Operations

### List Enabled APIs
```bash
gcloud services list --enabled --project=hopeful-breaker-426606-h9
```

### Enable a New API
```bash
gcloud services enable <api-name>.googleapis.com --project=hopeful-breaker-426606-h9
```

### Common APIs for This Portfolio
| API | Purpose |
| :--- | :--- |
| `firebaseanalytics.googleapis.com` | Analytics telemetry |
| `crashlytics.googleapis.com` | Crash reporting |
| `admob.googleapis.com` | Ad monetization |
| `firebase.googleapis.com` | Core Firebase services |
| `cloudresourcemanager.googleapis.com` | Project management |

### List Firebase Apps
```bash
gcloud firebase apps list --project=hopeful-breaker-426606-h9
```

### Create a New Firebase Android App
```bash
gcloud firebase apps create android \
  --project=hopeful-breaker-426606-h9 \
  --package-name=com.saviorsystems.<appname> \
  --display-name="<App Display Name>"
```

## MCP Server Integration
The `gcloud` MCP server is available for programmatic access. Use `call_mcp_tool` with `ServerName: gcloud` and `ToolName: run_gcloud_command` for automated operations.

## Agent Instructions
Always verify the GCP project ID is `hopeful-breaker-426606-h9` before running any command. Never create resources in the wrong project.
