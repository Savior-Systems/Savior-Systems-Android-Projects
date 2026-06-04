# Prompt: Play Store Policy Review

Use this prompt to audit codebases before submitting to Google Play Console:

```
Act as a Google Play Store Policy Analyst.
Review the following code assets, permissions, and app description copy against the guidelines in [PLAY-CONSOLE-POLICY-GUARDRAILS.md](file:///C:/Users/cibdh/Desktop/Savior-Systems-Android-Projects/PLAY-CONSOLE-POLICY-GUARDRAILS.md).
Check for:
1. Repetitive code snippets or templating signatures.
2. Extra permissions declared in AndroidManifest.xml.
3. Metadata violations or keyword stuffing in store descriptions.
4. Ad layouts violating unexpected overlay rules.
Output a strict compliance check report detailing passes, warnings, and required changes.
```
