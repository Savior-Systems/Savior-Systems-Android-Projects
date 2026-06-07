# Prompt: ASO Description Optimization

Use this prompt to generate or refine store listing descriptions optimized for conversion and search visibility.

---

## Input Variables
- `[APP_NAME]`: The name of the app.
- `[COUNTRY]`: The target country/region (e.g., US, BD, DE).
- `[LANGUAGE]`: The target language (e.g., English, Bengali).

## Prompt

```
Act as a senior ASO Copywriter for the Google Play Store.

Given the target country [COUNTRY] and language [LANGUAGE], write an optimized App Title, Short Description, and Full Description for [APP_NAME].

Use the keyword cluster provided in the app's `07.ASO-PLAY-STORE-LISTING.md` file.

Strict Requirements:
1. App Title: ≤ 30 characters. Must contain the primary keyword.
2. Short Description: ≤ 80 characters. Must contain the secondary keyword naturally.
3. Full Description: ≤ 4000 characters. Must:
   a. Open with the primary keyword in the first sentence.
   b. Use bullet-pointed feature lists with emoji icons.
   c. Include a call-to-action in the final paragraph.
   d. Naturally integrate at least 5 keywords from the matrix.
   e. NEVER keyword stuff. Readability and value proposition are paramount.
4. Do NOT copy descriptions from competing apps.
5. Highlight the "100% Offline & Privacy-First" angle as a differentiator.
```
