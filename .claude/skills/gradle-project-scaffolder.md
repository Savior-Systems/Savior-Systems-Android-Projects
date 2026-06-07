# Skill: Gradle Project Scaffolder

## Purpose
Generates the initial Android project structure (Gradle KTS, Version Catalog, Hilt, Room, Compose) for any app in the portfolio based on its technical architecture document.

## When to Use
- When transitioning an app from the "Documentation" phase to the "Implementation" phase.
- When the user says "start coding App XX" or "scaffold App XX".

## Pre-Requisites
- The app's `04.TECHNICAL-ARCHITECTURE.md` must exist and be finalized.
- The app's `05.DATABASE-SCHEMA.md` must exist with entity definitions.

## Scaffolding Sequence

### Step 1: Project Initialization
Use the Android CLI or manual creation:
```
com.saviorsystems.<appslug>/
├── app/
│   ├── build.gradle.kts
│   ├── src/
│   │   └── main/
│   │       ├── java/com/saviorsystems/<appslug>/
│   │       │   ├── App.kt                     # @HiltAndroidApp
│   │       │   ├── MainActivity.kt
│   │       │   ├── data/
│   │       │   ├── domain/
│   │       │   ├── ui/
│   │       │   ├── di/
│   │       │   └── background/
│   │       ├── res/
│   │       │   ├── values/
│   │       │   │   ├── strings.xml             # From 10.TRANSLATIONS
│   │       │   │   ├── colors.xml              # From 02.UI-UX
│   │       │   │   └── themes.xml
│   │       │   └── mipmap-xxxhdpi/
│   │       │       └── ic_launcher.png         # From generated icon
│   │       └── AndroidManifest.xml
│   └── google-services.json                    # From Firebase Console
├── gradle/
│   └── libs.versions.toml                      # Version Catalog
├── build.gradle.kts                            # Project-level
├── settings.gradle.kts
└── gradle.properties
```

### Step 2: Version Catalog (`libs.versions.toml`)
```toml
[versions]
kotlin = "2.0.0"
compose-bom = "2024.06.00"
hilt = "2.51.1"
room = "2.6.1"
datastore = "1.1.1"
firebase-bom = "33.1.0"
ads = "23.2.0"

[libraries]
# ... all deps from 04.TECHNICAL-ARCHITECTURE.md

[plugins]
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
ksp = { id = "com.google.devtools.ksp", version = "2.0.0-1.0.21" }
```

### Step 3: Theme from Design System
Extract hex codes from `02.UI-UX-DESIGN-SYSTEM.md` and generate:
- `Color.kt` (Compose color definitions)
- `Theme.kt` (MaterialTheme wrapper)
- `Type.kt` (Typography definitions)

### Step 4: Room Entity Stubs
Extract entity definitions from `05.DATABASE-SCHEMA.md` and generate:
- Entity data classes with `@Entity`, `@PrimaryKey`, `@ColumnInfo` annotations.
- DAO interfaces with `@Dao`, `@Query`, `@Insert` annotations.
- `AppDatabase` abstract class.

### Step 5: Navigation Graph
Extract destinations from `03.FUNCTIONAL-FLOWS.md` and generate:
- `Routes` sealed class.
- `AppNavHost` composable.
- `BottomNavBar` composable (if applicable).

## Agent Instructions
1. Read the 4 source documents (02, 03, 04, 05) before generating any code.
2. Compile and verify the project builds before committing.
3. Commit with: `feat(XX-app-name): Initial project scaffolding`
