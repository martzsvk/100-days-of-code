# Day 35: Rain Alert App (Twilio & API Authentication) ☔

An automated weather monitoring script that checks the 12-hour forecast for your location and sends an SMS notification if rain is expected.

## What I Learned 🛠️
* **Complex JSON Slicing:** Navigating through deeply nested data structures to extract specific weather condition codes for the next 12 hours.
* **Environment Variables (`.env`):** Learning the industry-standard practice of hiding sensitive credentials (like Twilio Auth Tokens and API Keys) from the source code using the `os` module and `python-dotenv`.
* **Twilio API:** Integrating a third-party communication platform to send real-world SMS messages from Python.

## Requirements 📦
* **Requests Library:** To fetch weather data.
* **Twilio:** To handle SMS communication.
* **python-dotenv:** To manage secret keys securely.
