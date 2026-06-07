# Skill: Strings.xml Localization Expander

## Purpose
Takes a completed English `strings.xml` from `10.TRANSLATIONS-LOCALIZATION.md` and generates translated versions for target locales.

## When to Use
- When preparing an app for multi-language release.
- When the user requests translations for a specific locale.

## Supported Locales

### Tier-1 (South Asian Focus)
| Locale | Language | Script | Direction |
| :--- | :--- | :--- | :--- |
| `bn` | Bengali (বাংলা) | Bengali | LTR |
| `hi` | Hindi (हिन्दी) | Devanagari | LTR |
| `ur` | Urdu (اردو) | Arabic | RTL |

### Tier-2 (Global Expansion)
| Locale | Language | Script | Direction |
| :--- | :--- | :--- | :--- |
| `es` | Spanish | Latin | LTR |
| `fr` | French | Latin | LTR |
| `de` | German | Latin | LTR |
| `ar` | Arabic | Arabic | RTL |
| `it` | Italian | Latin | LTR |

## Translation Rules
1. **Never translate**: App name, package names, route constants, or technical identifiers.
2. **Preserve placeholders**: Keep `%1$s`, `%1$d`, `\n`, and other format specifiers intact.
3. **Handle plurals**: Use Android `<plurals>` syntax with correct quantity selectors for each locale.
4. **RTL Safety**: For Urdu and Arabic, verify that string concatenation preserves reading order.
5. **Cultural Adaptation**: Adapt metaphors and idiomatic expressions. Example: "Streak" might not translate literally into Bengali — use "ধারাবাহিক" (consecutive series).

## Output Format
Generate `res/values-<locale>/strings.xml` files:
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Auto-generated translation for [LOCALE] -->
    <string name="app_name">Water Tracker</string> <!-- Do NOT translate -->
    <string name="nav_home">[Translated]</string>
    ...
</resources>
```

## Agent Instructions
1. Read the app's `10.TRANSLATIONS-LOCALIZATION.md` for the base strings.
2. Generate translations using contextual understanding (not word-by-word).
3. Save each locale file to the appropriate `res/values-<locale>/` directory.
4. Update `10.TRANSLATIONS-LOCALIZATION.md` to mark locales as completed.
