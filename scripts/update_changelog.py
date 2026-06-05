#!/usr/bin/env python3
import subprocess
import os
import re

def get_git_output(args, cwd):
    try:
        res = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return res.stdout.strip()
    except Exception as e:
        print(f"Error running git command {' '.join(args)}: {e}")
        return ""

def update_changelog(workspace_dir, commits):
    changelog_path = os.path.join(workspace_dir, "CHANGELOG.md")
    categories = {
        "feat": "🚀 Features & Additions",
        "fix": "🐛 Bug Fixes",
        "docs": "📝 Documentation Updates",
        "style": "🎨 Style & UI",
        "refactor": "⚙️ Refactoring & Improvements",
        "chore": "🧹 Maintenance & Tasks",
        "perf": "⚡ Performance Optimizations",
        "other": "📦 Other Changes"
    }

    categorized_commits = {k: [] for k in categories.keys()}

    for commit in commits:
        if not commit:
            continue
        parts = commit.split("|", 2)
        if len(parts) < 3:
            continue
        sha, date, msg = parts
        
        match = re.match(r"^(\w+)(?:\(([^)]+)\))?:\s*(.*)$", msg)
        if match:
            ctype = match.group(1).lower()
            scope = match.group(2)
            cmsg = match.group(3)
            
            scope_prefix = f"**{scope}**: " if scope else ""
            formatted_msg = f"* {scope_prefix}{cmsg} ([`{sha}`](https://github.com/Savior-Systems/Savior-Systems-Android-Projects/commit/{sha})) — *{date}*"
            
            if ctype in categorized_commits:
                categorized_commits[ctype].append(formatted_msg)
            else:
                categorized_commits["other"].append(formatted_msg)
        else:
            formatted_msg = f"* {msg} ([`{sha}`](https://github.com/Savior-Systems/Savior-Systems-Android-Projects/commit/{sha})) — *{date}*"
            categorized_commits["other"].append(formatted_msg)

    changelog_content = [
        "# 📋 Savior Systems Android Portfolio — Project Changelog",
        "\n*This file is updated automatically on every commit.*",
        "\n---"
    ]

    for ctype, title in categories.items():
        list_commits = categorized_commits[ctype]
        if list_commits:
            changelog_content.append(f"\n## {title}")
            changelog_content.extend(list_commits)

    with open(changelog_path, "w", encoding="utf-8") as f:
        f.write("\n".join(changelog_content) + "\n")

def update_contributors(workspace_dir):
    contributors_path = os.path.join(workspace_dir, "CONTRIBUTORS.md")
    # Get sorted unique list of contributors (Name <email>)
    raw_contribs = get_git_output(["git", "log", "--pretty=format:%an <%ae>"], workspace_dir)
    contribs = sorted(list(set(raw_contribs.split("\n")))) if raw_contribs else []

    contribs_content = [
        "# 👥 Project Contributors — Savior Systems Android Portfolio",
        "\nThe following list details all developers, designers, and maintainers who have contributed commits to Savior Systems Android projects.",
        "\n*This file is updated automatically based on git commits.*",
        "\n---",
        "\n## 🛠️ Developer Contributions Ledger"
    ]

    for c in contribs:
        if c:
            # Mask email address slightly to prevent scraping spam
            masked = re.sub(r"<([^>]+)@([^>]+)>", r"(\1 at \2)", c)
            contribs_content.append(f"*   **{masked}**")

    with open(contributors_path, "w", encoding="utf-8") as f:
        f.write("\n".join(contribs_content) + "\n")

def update_activity(workspace_dir, commits):
    activity_path = os.path.join(workspace_dir, "ACTIVITY.md")
    
    total_commits = len(commits)
    last_commit_date = "N/A"
    if commits and commits[0]:
        parts = commits[0].split("|", 2)
        if len(parts) >= 2:
            last_commit_date = parts[1]

    activity_content = [
        "# 📈 Repository Commit Activity Ledger",
        "\n*This report details development activity logs and metrics for Savior Systems portfolio.*",
        "\n*Updated automatically on every commit.*",
        "\n---",
        "\n## 📊 Repository Health Metrics",
        f"*   **Total Commits**: `{total_commits}`",
        f"*   **Last Development Activity**: `{last_commit_date}`",
        "\n## 📝 Recent Activity Logs"
    ]

    for i, commit in enumerate(commits[:25]): # Show top 25 recent commits
        if not commit:
            continue
        parts = commit.split("|", 2)
        if len(parts) < 3:
            continue
        sha, date, msg = parts
        activity_content.append(f"*   `{sha}` — **{date}** : {msg}")

    with open(activity_path, "w", encoding="utf-8") as f:
        f.write("\n".join(activity_content) + "\n")

def main():
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Get git log commits
    raw_log = get_git_output(["git", "log", "--pretty=format:%h|%ad|%s", "--date=short"], workspace_dir)
    commits = raw_log.split("\n") if raw_log else []

    update_changelog(workspace_dir, commits)
    update_contributors(workspace_dir)
    update_activity(workspace_dir, commits)
    
    # Auto-run the progress tracker
    try:
        import update_progress
        update_progress.main()
        print("Progress tracker successfully updated!")
    except Exception as e:
        print(f"Error running progress tracker: {e}")
    
    # Auto-stage generated files if we are inside a pre-commit context
    subprocess.run(["git", "add", "CHANGELOG.md", "CONTRIBUTORS.md", "ACTIVITY.md", "PROGRESS.md", "README.md"], cwd=workspace_dir)
    
    print("Documentation ledger files synced successfully!")

if __name__ == "__main__":
    main()

