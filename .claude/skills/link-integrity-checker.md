# Skill: Link Integrity Checker

## Purpose
Scans all markdown files in the repository for broken or non-GitHub-compatible links and fixes them automatically.

## When to Use
- After completing a batch of documentation files.
- After any refactoring that renames or moves files.
- As part of the `04-interlinking-audit` workflow.

## Execution Script (Python)

```python
import os, re, urllib.parse

root_dir = r'f:\Savior-Systems-Android-Projects'
pattern = re.compile(r'\(file:///[^)]+\)', re.IGNORECASE)

broken_count = 0
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.md'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            matches = pattern.findall(content)
            if matches:
                print(f"BROKEN LINKS in {filepath}:")
                for m in matches:
                    print(f"  {m}")
                broken_count += len(matches)

if broken_count == 0:
    print("✅ No broken file:/// links found.")
else:
    print(f"❌ Found {broken_count} broken links. Run the fix script.")
```

## Fix Script
The fix script converts absolute `file:///` links to relative paths. It computes the relative path from the markdown file's directory to the target file, URL-encodes spaces, and writes the corrected content back.

## Agent Instructions
When executing this skill:
1. Run the detection script first to identify problems.
2. If broken links are found, run the fix script (see `workflows/04-interlinking-audit.md`).
3. Commit fixes with message: `fix: convert absolute links to relative paths`.
