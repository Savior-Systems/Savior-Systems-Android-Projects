# Skill: UI/UX Dynamic Design Generator

## Purpose
Generates high-quality, modern, dynamic UI/UX design palettes and component specifications for an app, adhering strictly to Material 3 and avoiding generic layouts.

## When to Use
- When creating `02.UI-UX-DESIGN-SYSTEM.md` for a new app.
- When the user asks to "make the app look premium" or "improve the design".

## Core Principles
1. **Dynamic Colors**: Support Light and Dark themes with full HSL/Hex mapping.
2. **Micro-interactions**: Define button press scales, ripple effects, and screen transition animations.
3. **Glassmorphism / Gradients**: Utilize modern styling instead of flat, solid backgrounds where appropriate.
4. **Typography**: Define distinct font families for headings vs body text (e.g., 'Outfit' for headers, 'Inter' for body).

## Checklist for Generation
1. Check `context/portfolio-context.md` to ensure the chosen primary color does not conflict with existing apps.
2. Generate 5-color palette (Primary, Secondary, Background, Surface, Error) for both Light and Dark modes.
3. Define Corner Radius tokens (e.g., Small = 8dp, Medium = 16dp, Large = 24dp).
4. Define at least two custom animations (e.g., "Liquid Fill Animation" for water tracking, or "Pulse Ring" for timers).

## Output Format
Produce the content structured exactly as required by the 14-document standard for `02.UI-UX-DESIGN-SYSTEM.md`.
