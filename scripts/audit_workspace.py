import os
import sys
import re

ROOT_DIR = r'.'
REQUIRED_BLUEPRINTS = [
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

def audit():
    errors_found = False
    print("=========================================================")
    print(" Savior Systems: Workspace Audit")
    print("=========================================================")
    
    # 1. Check for missing blueprints in Project folders
    for item in os.listdir(ROOT_DIR):
        if os.path.isdir(item) and re.match(r'^\d{2}\.', item):
            project_path = os.path.join(ROOT_DIR, item)
            for bp in REQUIRED_BLUEPRINTS:
                bp_path = os.path.join(project_path, bp)
                if not os.path.exists(bp_path):
                    print(f"[!] ERROR: Missing required blueprint: {bp_path}")
                    errors_found = True

    # 2. Check for empty files, mojibake, and bad backticks
    for root, dirs, files in os.walk(ROOT_DIR):
        if '.git' in root or '.claude' in root or 'scratch' in root:
            continue
            
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                
                # Check empty / BOM only
                size = os.path.getsize(path)
                if size < 50:
                    print(f"[!] ERROR: File is empty or mostly empty: {path} ({size} bytes)")
                    errors_found = True
                    continue
                
                try:
                    with open(path, 'rb') as f:
                        data = f.read()
                    
                    # Check Mojibake
                    if b'\xc3\xa2' in data or b'\x00x' in data:
                        print(f"[!] ERROR: Suspected mojibake or null byte corruption found in: {path}")
                        errors_found = True
                        
                    # Check bad backticks
                    text = data.decode('utf-8', errors='ignore')
                    if re.search(r'(?m)^`([a-z]*)\s*$', text):
                        print(f"[!] ERROR: Multiline code block bounded by single backticks in: {path}")
                        errors_found = True
                        
                except Exception as e:
                    print(f"[!] ERROR: Could not read {path}: {e}")
                    errors_found = True
                    
    if errors_found:
        print("\n[X] AUDIT FAILED: Please fix the errors above.")
        sys.exit(1)
    else:
        print("\n[OK] AUDIT PASSED: All documentation is structurally sound.")
        sys.exit(0)

if __name__ == '__main__':
    audit()
