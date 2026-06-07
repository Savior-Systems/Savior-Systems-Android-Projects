# Savior Systems: App Idea Matrix

This document provides a consolidated reference overview mapping the categories, tech requirements, monetization profiles, and keywords for all 30 applications in the portfolio.

---

## 1. General Portfolio Overview

| # | App Name | Primary Category | Target Market | Competition Level | Primary Value Proposition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | FocusPulse Timer | Productivity | Tier-1 Global | Medium-High | Minimalist Pomodoro with built-in custom sound profiles |
| **02** | BD Varsity CGPA Pro | Education | South Asia (BD) | Low | Custom GPA mapping preset library for all top BD universities |
| **03** | MicroHabit Tracker | Health & Fitness | Tier-1 Global | High | Micro-habit streaks with custom dashboard home widgets |
| **04** | Expense Diary Local | Finance | Tier-1 Global | High | Zero-network, offline-first encrypted CSV logging sheets |
| **05** | Prayer Time Helper | Lifestyle | South Asia / Global | Medium | Offline geographic astronomical prayer alerts and Qibla indicator |
| **06** | Water Log & Remind | Health & Fitness | Tier-1 Global | High | Clean notification cycle with smart weight-based volume intake |
| **07** | Smart Age & BD Date | Utilities | South Asia / Global | Low | Age calculator coupled with Bengali historical calendar conversions |
| **08** | Resume PDF Maker | Productivity | Global | Medium-High | Fast input forms that compile directly into standard templates |
| **09** | PDF Compress Lite | Productivity | Global | Medium | Local on-device image/PDF rendering compression engine |
| **10** | Routine Widget | Productivity | Tier-1 Global | Medium | Customizable dynamic task lists that update inside widgets |
| **11** | BD Tax & VAT Calc | Finance | South Asia (BD) | Low | Offline calculator updating FY 2025/2026 local tax rules |
| **12** | Minimalist To-Do | Productivity | Tier-1 Global | High | Gesture-based todo checkoff list featuring zero network sync |
| **13** | Fuel Mileage Log | Finance / Auto | Global | Low-Medium | Quick logs for fuel usage tracking average distance over time |
| **14** | English-Bangla Vocab | Education | South Asia (BD) | Medium | Offline dictionary database featuring gamified memory flashcards |
| **15** | Breathing Pacer | Health & Fitness | Tier-1 Global | Medium | Guided rhythmic breathing visualizations for anxiety relief |
| **16** | WiFi QR Sharer | Tools | Global | Medium | Generates clear local scan codes for network sharing |
| **17** | Exam Countdown BD | Education | South Asia (BD) | Low | Countdown timelines for BCS, HSC, and varsity admissions |
| **18** | Daily Quotes Maker | Entertainment | Global | High | Generates sharing formats for social updates |
| **19** | Device Info Specs | Tools | Global | Medium | Full diagnostic metrics dashboard reporting local hardware levels |
| **20** | Outfit Canvas | Lifestyle | Global | Low | Digital wardrobe planner helping users plan out daily colors |
| **21** | ScanMaster Offline | Tools | Global | High | Fast camera scans converting documents to clean PDFs |
| **22** | Color Hex Picker | Tools | Global | Medium | Visual color wheel and screen color sampler for developers |
| **23** | BMI & BMR Target | Health & Fitness | Global | High | Instant caloric baseline calculation showing ideal target goals |
| **24** | Tip & Split Pro | Utilities | Tier-1 Global | Medium | Easy split logs including pre-calculated local service tax ranges |
| **25** | InstaGrid Splitter | Tools | Global | Medium | Splits single photos into clean multiple grid ratios |
| **26** | Offline Vault & Pass | Tools | Global | High | Local encrypted database storing credential keys offline |
| **27** | Offline Voice Note | Productivity | Global | Medium | On-device microphone logging saving files directly to local storage |
| **28** | Social Bio Captions | Entertainment | Global | High | Index of bio ideas grouped by categories for copy-paste use |
| **29** | Auto Text Spammer | Tools | Global | Medium | Loops draft template formats for rapid text input |
| **30** | Fake Call Rescue | Tools | Global | Medium | Trigger simulated incoming phone layouts with timers |

---

## 2. Technical Profile & Requirements

| # | App Name | Est. Build | Complexity | Core Permissions | Storage Database | Offline Support |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| **01** | FocusPulse Timer | 4 Days | 2/5 | Notification | DataStore | 100% |
| **02** | BD Varsity CGPA Pro | 3 Days | 1/5 | None | Room DB | 100% |
| **03** | MicroHabit Tracker | 5 Days | 3/5 | Alarm (cooldown) | Room DB | 100% |
| **04** | Expense Diary Local | 5 Days | 3/5 | Write External (Optional) | Room DB (Encrypted) | 100% |
| **05** | Prayer Time Helper | 5 Days | 3/5 | Location (Coarse) | Location Cache | 100% (GPS) |
| **06** | Water Log & Remind | 4 Days | 2/5 | Notification, Exact Alarm | DataStore | 100% |
| **07** | Smart Age & BD Date | 3 Days | 1/5 | None | None | 100% |
| **08** | Resume PDF Maker | 6 Days | 4/5 | Write Storage | Room DB | 100% |
| **09** | PDF Compress Lite | 6 Days | 4/5 | None | Temp Cache | 100% |
| **10** | Routine Widget | 5 Days | 3/5 | None | Room DB | 100% |
| **11** | BD Tax & VAT Calc | 3 Days | 2/5 | None | DataStore | 100% |
| **12** | Minimalist To-Do | 4 Days | 2/5 | None | Room DB | 100% |
| **13** | Fuel Mileage Log | 4 Days | 2/5 | None | Room DB | 100% |
| **14** | English-Bangla Vocab | 5 Days | 3/5 | None | Pre-populated Room | 100% |
| **15** | Breathing Pacer | 4 Days | 2/5 | None | None | 100% |
| **16** | WiFi QR Sharer | 3 Days | 2/5 | Camera (for scan) | None | 100% |
| **17** | Exam Countdown BD | 3 Days | 2/5 | Notification | Room DB | 100% |
| **18** | Daily Quotes Maker | 4 Days | 2/5 | Write Storage | Room DB | 100% |
| **19** | Device Info Specs | 4 Days | 3/5 | None | None | 100% |
| **20** | Outfit Canvas | 5 Days | 3/5 | Camera, Storage | Room DB | 100% |
| **21** | ScanMaster Offline | 6 Days | 4/5 | Camera, Write Storage | Room DB | 100% |
| **22** | Color Hex Picker | 3 Days | 2/5 | None | Room DB | 100% |
| **23** | BMI & BMR Target | 3 Days | 1/5 | None | None | 100% |
| **24** | Tip & Split Pro | 3 Days | 1/5 | None | None | 100% |
| **25** | InstaGrid Splitter | 3 Days | 2/5 | Storage Write | None | 100% |
| **26** | Offline Vault & Pass | 5 Days | 4/5 | None | Room DB (SQLCipher) | 100% |
| **27** | Offline Voice Note | 5 Days | 3/5 | Record Audio | File system / Room | 100% |
| **28** | Social Bio Captions | 3 Days | 1/5 | None | Room DB | 100% |
| **29** | Auto Text Spammer | 4 Days | 2/5 | None | Room DB | 100% |
| **30** | Fake Call Rescue | 4 Days | 3/5 | None | None | 100% |

---

## 3. ASO Strategy Mapping

| # | App Name | Play Store Title (≤30 chars) | Target Category | Primary ASO Keywords |
| :--- | :--- | :--- | :--- | :--- |
| **01** | FocusPulse Timer | FocusPulse Pomodoro Timer | Productivity | pomodoro timer, focus timer, clock |
| **02** | BD Varsity CGPA Pro | BD Varsity CGPA Calculator | Education | cgpa calculator, nu cgpa, dhaka varsity |
| **03** | MicroHabit Tracker | MicroHabit Tracker Streaks | Productivity | habit tracker, micro habits, habit logs |
| **04** | Expense Diary Local | Expense Diary Offline Log | Finance | expense tracker, money manager, budget |
| **05** | Prayer Time Helper | Offline Prayer Times Qibla | Lifestyle | prayer times, namaz somoy, qibla |
| **06** | Water Log & Remind | Water Log & Hydro Reminder | Health & Fitness | water tracker, drink water, log water |
| **07** | Smart Age & BD Date | Smart Age & Bengali Date | Utilities | age calculator, birthday countdown, date |
| **08** | Resume PDF Maker | Resume Maker PDF CV Builder | Productivity | cv maker, resume builder, pdf cv |
| **09** | PDF Compress Lite | PDF Compress Resize Offline | Productivity | compress pdf, reduce pdf size, pdf tool |
| **10** | Routine Widget | Routine Widget Task Planner | Productivity | routine planner, habit widget, todo widget |
| **11** | BD Tax & VAT Calc | BD Tax & VAT Calculator | Finance | bd tax calculator, income tax bd, vat |
| **12** | Minimalist To-Do | Minimalist To-Do List Tasks | Productivity | minimalist todo, task manager, simple todo |
| **13** | Fuel Mileage Log | Fuel Mileage Log Tracker | Auto & Vehicles | fuel log, gas mileage calculator, car tracker |
| **14** | English-Bangla Vocab | English to Bangla Vocabulary | Education | bangla dictionary, english to bangla, vocab |
| **15** | Breathing Pacer | Breathing Pacer Guided | Health & Fitness | breathing exercise, box breathing, anxiety |
| **16** | WiFi QR Sharer | WiFi QR Code Generator Sharer | Tools | wifi qr code, share wifi, scan qr wifi |
| **17** | Exam Countdown BD | Exam Countdown BD Study Plan | Education | exam tracker, hsc result, bcs exam prep |
| **18** | Daily Quotes Maker | Daily Quotes Creator Editor | Art & Design | quote maker, text on photo, wallpaper maker |
| **19** | Device Info Specs | Device Info System Specs | Tools | system monitor, device hardware info, cpu z |
| **20** | Outfit Canvas | Outfit Canvas Wardrobe Plan | Lifestyle | outfit planner, style diary, clothing organizer |
| **21** | ScanMaster Offline | ScanMaster Document Scanner | Tools | scan documents, camera pdf scan, doc scanner |
| **22** | Color Hex Picker | Color Hex Picker Wheel | Tools | color picker, palette designer, hex code |
| **23** | BMI & BMR Target | BMI Calculator & BMR Tracker | Health & Fitness | bmi tracker, body fat calculator, bmr logs |
| **24** | Tip & Split Pro | Tip Calculator Split Bills | Utilities | bill splitter, tip calc, group splitter |
| **25** | InstaGrid Splitter | InstaGrid Splitter 9 Grid | Art & Design | photo splitter, grid maker, split photo |
| **26** | Offline Vault & Pass | Encrypted Password Vault | Tools | password manager, secure locker, password vault |
| **27** | Offline Voice Note | Offline Voice Note Recorder | Productivity | voice recorder, dictation logs, audio memos |
| **28** | Social Bio Captions | Bio Status Captions Creator | Entertainment | instagram bio, fb status captions, bio ideas |
| **29** | Auto Text Spammer | Auto Text Spammer Loop | Tools | text repeater, spam templates, copy paste loop |
| **30** | Fake Call Rescue | Fake Call Rescue Simulator | Utilities | mock call, emergency escape, prank call |
