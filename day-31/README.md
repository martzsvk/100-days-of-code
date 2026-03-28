# Day 31: Flash Card App 🎴

This is a Capstone Project for the intermediate section, combining advanced Tkinter UI and Pandas data manipulation.

## What I Learned 🛠️
* **UI Design with Canvas:** Creating a "flipping card" effect using images and text overlays in Tkinter.
* **Progress Persistence:** Saving the remaining "unknown" words into a new file (`words_to_learn.csv`) so the user can pick up where they left off.

## How it Works ⚙️
1. The app shows a foreign word.
2. Click "✅" if you knew it (the word is removed from your deck).
3. Click "❌" if you didn't know it (it will be added to `words_to_learn.csv`).
4. All progress is saved automatically when you close the app.

## Requirements 📦
* Pandas: `pip install pandas`
