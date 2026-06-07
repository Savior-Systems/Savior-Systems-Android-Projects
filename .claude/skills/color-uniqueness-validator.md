# Skill: Color Uniqueness Validator

## Purpose
Ensures no two apps in the portfolio share the same primary color, preventing Google Play "Repetitive Content" rejections.

## When to Use
- Before finalizing a new app's `02.UI-UX-DESIGN-SYSTEM.md`.
- During the interlinking audit workflow.
- When the user adds a new app to the portfolio.

## Execution Steps

1. **Read the color matrix** from `.claude/context/portfolio-context.md`.
2. **Extract the primary hex color** from the new app's `02.UI-UX-DESIGN-SYSTEM.md`.
3. **Compare**: If the hex code matches any existing entry in the matrix, flag a conflict.
4. **Suggest alternatives**: If a conflict is found, suggest 3 alternative hex codes that are visually distinct from all existing entries.
5. **Update the matrix**: After the new color is finalized, update `context/portfolio-context.md`.

## Conflict Resolution
If two colors are within a ΔE (CIE2000) distance of < 15, they are considered "too similar" even if the hex values differ. Use the following formula approximation:
- Convert hex to RGB.
- Compare R, G, B channels. If all three channels differ by < 30, flag as "visually similar".

## Agent Instructions
This skill is advisory. Always present the conflict and alternatives to the user before making changes.
