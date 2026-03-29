# Day 38: Workout Tracking 🏃‍♂️

A fitness tracking application that uses Natural Language Processing (NLP) to understand user exercise descriptions and automatically logs the data (duration, calories, date) into a Google Sheet.

## What I Learned 🛠️
* **Natural Language Processing (NLP):** Using the Nutritionix API to convert plain English sentences into structured data.
* **HTTP POST Requests:** Sending JSON data to external servers to create new rows in a database/spreadsheet.
* **Dynamic Time Formatting:** Using the `datetime` module to capture and format the exact moment of the workout (`DD.MM.YYYY` and `HH:MM:SS`).

## How it Works ⚙️
1. The code asks the user: "Which exercises did you do?"
2. The input (e.g., "I walked 5km") is sent to the Nutritionix API.
3. The API returns a JSON response containing the exercise name, duration in minutes, and estimated calories burned.
4. This structured data is then sent via a `POST` request to a Google Sheet (managed by the Sheety API), where it is saved for long-term tracking.

## Requirements 📦
* **Requests**
* **Nutritionix API**
* **Sheety API**
* **Python-Dotenv**
