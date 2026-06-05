#!/usr/bin/env python3
import os
import re

def is_project_file_complete(filepath, is_readme=False):
    if not os.path.exists(filepath):
        return False
    size = os.path.getsize(filepath)
    if size < 2000: # Completed docs are detailed and > 2000 bytes
        return False
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # If it contains unresolved template variables/placeholders
            if "$(@" in content or "TODO" in content:
                return False
            if is_readme:
                # If a project README (other than FocusPulse) still mentions "Core timer logic" or "Pomodoro"
                # it means it is copy-pasted boilerplate.
                if "timer logic" in content and "FocusPulse" not in filepath:
                    return False
            return True
    except Exception:
        return False

def get_project_folders(workspace_dir):
    folders = []
    for name in os.listdir(workspace_dir):
        path = os.path.join(workspace_dir, name)
        if os.path.isdir(path) and re.match(r"^\d{2}\.", name):
            folders.append(name)
    return sorted(folders)

def main():
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_folders = get_project_folders(workspace_dir)
    
    # 10 Root level documentation files
    root_docs = [
        "README.md",
        "UNIFIED-RESEARCH-REPORT.md",
        "PORTFOLIO-STRATEGY.md",
        "APP-IDEA-MATRIX.md",
        "PUBLISHING-ROADMAP.md",
        "ADMOB-MONETIZATION-PLAYBOOK.md",
        "PLAY-CONSOLE-POLICY-GUARDRAILS.md",
        "REUSABLE-ANDROID-COMPONENTS.md",
        "MASTER-CHECKLIST.md",
        "DEVELOPER-GUIDE.md"
    ]
    
    project_docs = [
        "README.md",
        "01.PRD-REQUIREMENTS.md",
        "02.UI-UX-DESIGN-SYSTEM.md",
        "03.FUNCTIONAL-FLOWS.md",
        "04.TECHNICAL-ARCHITECTURE.md",
        "05.DATABASE-SCHEMA.md",
        "06.ADMOB-MONETIZATION-MAP.md",
        "07.ASO-PLAY-STORE-LISTING.md",
        "08.PLAY-POLICY-SAFETY.md",
        "09.TESTING-ASSURANCE-PLAN.md",
        "10.TRANSLATIONS-LOCALIZATION.md",
        "11.GRAPHIC-ASSETS-MANIFEST.md",
        "12.LOGGING-ANALYTICS.md",
        "13.BACKLOG-TASKS.md"
    ]
    
    total_root = len(root_docs)
    completed_root = 0
    root_status = {}
    
    for doc in root_docs:
        filepath = os.path.join(workspace_dir, doc)
        # Root docs are assumed complete if they exist and are > 1000 bytes
        complete = os.path.exists(filepath) and os.path.getsize(filepath) > 1000
        if complete:
            completed_root += 1
        root_status[doc] = complete

    total_project_files = len(project_folders) * len(project_docs)
    completed_project_files = 0
    project_stats = {}
    
    for folder in project_folders:
        folder_path = os.path.join(workspace_dir, folder)
        folder_completed = 0
        file_status = {}
        for doc in project_docs:
            filepath = os.path.join(folder_path, doc)
            complete = is_project_file_complete(filepath, is_readme=(doc == "README.md"))
            if complete:
                completed_project_files += 1
                folder_completed += 1
            file_status[doc] = complete
        project_stats[folder] = {
            "completed": folder_completed,
            "total": len(project_docs),
            "percentage": (folder_completed / len(project_docs)) * 100,
            "files": file_status
        }
    
    total_all = total_root + total_project_files
    completed_all = completed_root + completed_project_files
    overall_percentage = (completed_all / total_all) * 100 if total_all > 0 else 0
    
    # Update PROGRESS.md
    update_progress_md(workspace_dir, overall_percentage, completed_all, total_all, root_status, project_stats)
    
    # Update README.md progress bar/badges
    update_readme_md(workspace_dir, overall_percentage, completed_all, total_all, project_stats)
    
    # Inject Navigation to all Project READMEs and documentation files
    update_project_navigation(workspace_dir, project_folders, project_docs)

def generate_progress_bar(percentage, width=20):
    filled = int(round(percentage / 100 * width))
    bar = "█" * filled + "░" * (width - filled)
    return f"`|{bar}|` ({percentage:.1f}%)"

def update_progress_md(workspace_dir, overall_pct, completed, total, root_status, stats):
    progress_path = os.path.join(workspace_dir, "PROGRESS.md")
    
    content = [
        "# 📊 Savior Systems Android Portfolio — Documentation Progress Tracker",
        "\n*This file tracks the completion status of the documentation blueprints across all 30 applications.*",
        "\n*Updated automatically on every commit.*",
        "\n---",
        "\n## 📈 Global Documentation Progress",
        f"- **Overall Completion**: {generate_progress_bar(overall_pct, width=30)}",
        f"- **Completed Documents**: `{completed}` of `{total}` files",
        f"- **Remaining Documents**: `{total - completed}` files",
        "\n## 🔑 Root-Level Strategy Documents",
        "| Document | Status |",
        "|:---|:---:|"
    ]
    
    for doc, complete in root_status.items():
        status_emoji = "✅ Complete" if complete else "⬚ Incomplete"
        content.append(f"| [`{doc}`](file:///./{doc}) | {status_emoji} |")
        
    content.append("\n## 📂 Application Breakdown")
    content.append("| Project | Completed Docs | Progress | Status |")
    content.append("|:---|:---:|:---|:---:|")
    
    for folder, data in stats.items():
        bar = generate_progress_bar(data["percentage"], width=10)
        status = "✅ Complete" if data["percentage"] == 100 else ("🔄 In Progress" if data["percentage"] > 0 else "⬚ Not Started")
        content.append(f"| [{folder}](file:///./{folder.replace(' ', '%20')}/README.md) | `{data['completed']}/{data['total']}` | {bar} | {status} |")
        
    content.append("\n## 🔍 Detailed File Status")
    for folder, data in stats.items():
        content.append(f"\n### [{folder}](file:///./{folder.replace(' ', '%20')}/README.md)")
        for filename, complete in data["files"].items():
            status_emoji = "✅" if complete else "⬚"
            file_link = f"file:///./{folder.replace(' ', '%20')}/{filename}"
            content.append(f"- {status_emoji} [{filename}]({file_link})")
            
    with open(progress_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n")

def update_readme_md(workspace_dir, overall_pct, completed, total, stats):
    readme_path = os.path.join(workspace_dir, "README.md")
    if not os.path.exists(readme_path):
        return
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    progress_bar = generate_progress_bar(overall_pct, width=25)
    status_block = f"""<!-- PROGRESS-START -->
### 📊 Documentation Completion: {progress_bar}
*   **Total Progress**: `{completed}/{total}` documentation blueprints fully completed.
*   **Target Scope**: 10 Strategy Blueprints and 30 distinct Android apps with 14 comprehensive SOP documents each.
*   **Detailed Status**: See [`PROGRESS.md`](PROGRESS.md) for full breakdown.
<!-- PROGRESS-END -->"""

    if "<!-- PROGRESS-START -->" in content and "<!-- PROGRESS-END -->" in content:
        content = re.sub(
            r"<!-- PROGRESS-START -->.*?<!-- PROGRESS-END -->",
            status_block,
            content,
            flags=re.DOTALL
        )
    else:
        status_pattern = r"(## 📊 Project Status\s*\n)"
        if re.search(status_pattern, content):
            content = re.sub(
                status_pattern,
                f"\\1\n{status_block}\n",
                content
            )
            
    badge_pct_str = f"{overall_pct:.1f}%25"
    content = re.sub(
        r'<img src="https://img.shields.io/badge/Status-Docs_Progress_[^"]*-blue\?style=for-the-badge" />',
        f'<img src="https://img.shields.io/badge/Status-Docs_Progress_{badge_pct_str}_%7C_Research_Complete-blue?style=for-the-badge" />',
        content
    )
    content = re.sub(
        r'<img src="https://img.shields.io/badge/Status-Docs_Progress_[^"]*-blue\?style=flat-square" />',
        f'<img src="https://img.shields.io/badge/Status-Docs_Progress_{badge_pct_str}-blue?style=flat-square" />',
        content
    )
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

def update_project_navigation(workspace_dir, folders, doc_files):
    for folder in folders:
        folder_path = os.path.join(workspace_dir, folder)
        for doc in doc_files:
            filepath = os.path.join(folder_path, doc)
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            nav_footer = f"""

---

### 🌐 Navigation Panel

| [◀ Repository Root](../README.md) | [📋 Master Checklist](../MASTER-CHECKLIST.md) | [📊 Progress Tracker](../PROGRESS.md) | [🚀 Publishing Roadmap](../PUBLISHING-ROADMAP.md) |
|:---:|:---:|:---:|:---:|

*Go to Project Directory:* **[{folder}](README.md)**
"""
            if "### 🌐 Navigation Panel" in content:
                content = re.sub(
                    r"\n*\s*---\s*\n*\s*### 🌐 Navigation Panel.*$",
                    "",
                    content,
                    flags=re.DOTALL
                )
            content = content.rstrip() + nav_footer
                
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    main()
