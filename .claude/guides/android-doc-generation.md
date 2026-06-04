# Guide: High-Volume App Document Generation

This guide explains how to generate the complete 00-14 documentation set for apps 02 through 12 using the AI Agent.

## Step-by-Step Prompt Flow
1. **Target Identification**: Load target app parameters from [APP-IDEA-MATRIX.md](file:///C:/Users/cibdh/Desktop/Savior-Systems-Android-Projects/APP-IDEA-MATRIX.md).
2. **Directory Creation**: Create a new folder matching the naming scheme: `[priority]-[slug]`.
3. **Template Compilation**: Instruct the agent to run:
   ```
   Generate the complete starter packs for App [NAME] matching files 00-14.
   Inherit architecture specifications from REUSABLE-ANDROID-COMPONENTS.md and monetization capping from ADMOB-MONETIZATION-PLAYBOOK.md.
   ```
4. **Validation**: Check file counts and references before building.
