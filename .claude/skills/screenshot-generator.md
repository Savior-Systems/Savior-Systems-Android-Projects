# Skill: Play Store Screenshot Generator

## Purpose
Defines the exact specifications and step-by-step instructions for generating Play Store-ready screenshot assets for any app in the portfolio.

## When to Use
- After the `02.UI-UX-DESIGN-SYSTEM.md` and `07.ASO-PLAY-STORE-LISTING.md` files are finalized.
- Before submitting an app to Google Play Console.
- When generating visual marketing assets.

## Screenshot Specifications

### Dimensions & Format
- **Phone Screenshots**: 1080 × 1920 px (9:16 portrait)
- **Tablet Screenshots** (optional): 1920 × 1200 px (16:10 landscape)
- **Format**: PNG or JPEG (no alpha channel)
- **Minimum**: 4 screenshots required. **Target**: 5 screenshots.

### Visual Composition Standard
Every screenshot follows the **"Device Frame + Gradient Background + Caption"** pattern:

```
┌────────────────────────────────┐
│                                │
│   [CAPTION TEXT - Bold Font]   │
│                                │
│   ┌──────────────────────┐    │
│   │                      │    │
│   │   [APP SCREEN VIEW]  │    │
│   │                      │    │
│   │                      │    │
│   └──────────────────────┘    │
│                                │
│      [GRADIENT BACKGROUND]     │
└────────────────────────────────┘
```

### Design Rules
1. **Background**: Use the app's primary color as the gradient base (e.g., Aqua Blue → Deep Ocean for Water Tracker).
2. **Device Frame**: Use a slim-bezel modern Android phone mockup.
3. **Caption Font**: Use the app's designated font family (from `02.UI-UX`) in Bold weight, white color.
4. **Caption Position**: Centered above or below the device frame.
5. **Content**: Show actual functional screens, NOT mockups with placeholder data.

### Standard 5-Screenshot Sequence
| # | Content | Purpose |
| :--- | :--- | :--- |
| 1 | **Main Dashboard / Home Screen** | First impression — show the core value immediately. |
| 2 | **Key Feature #1** | Highlight the primary differentiator (e.g., widget, compass, calculator). |
| 3 | **Key Feature #2** | Highlight the secondary feature (e.g., history, charts, settings). |
| 4 | **Settings / Customization** | Show personalization options to convey depth. |
| 5 | **Privacy / Offline Badge** | Reinforce the "100% Offline & Private" value proposition. |

## Execution Method
Use the `generate_image` tool with a detailed prompt describing the screenshot composition.  
Save the output to the app's directory with naming: `screenshot_01_dashboard.png`, `screenshot_02_feature.png`, etc.

## Agent Instructions
1. Read the app's `07.ASO-PLAY-STORE-LISTING.md` for caption text.
2. Read the app's `02.UI-UX-DESIGN-SYSTEM.md` for color palette and font family.
3. Generate each screenshot using the `generate_image` tool.
4. Update `11.GRAPHIC-ASSETS-MANIFEST.md` with the generated file paths.
