#!/usr/bin/env python3
import subprocess
import os
import re

def get_git_output(args, cwd):
    try:
        res = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return res.stdout.decode('utf-8', errors='ignore').strip()
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
    print(f"Changelog updated successfully at: {changelog_path}")

def main():
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Get git log commits
    raw_log = get_git_output(["git", "log", "--pretty=format:%h|%ad|%s", "--date=short"], workspace_dir)
    commits = raw_log.split("\n") if raw_log else []

    update_changelog(workspace_dir, commits)

if __name__ == "__main__":
    main()
