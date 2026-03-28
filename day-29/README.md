# Day 29 & 30: Password Manager (GUI & JSON) 🔐

### This project it's a combination of days 29 and 30. In day 29 I did the main functionality and in day 30 I added the possibilty of searching existing passwords.
A secure, desktop-based Password Manager with a built-in password generator. This project is a combination of GUI design, data persistence, and professional error handling.

## What I Learned 🛠️
* **Advanced Tkinter UI:** Building a complex layout with images, multi-column grids, and interactive buttons.
* **Password Generation Logic:** Using the `random` module with list comprehensions to create strong, randomized passwords (letters, numbers, symbols).
* **Search Functionality:** Adding a feature to quickly look up existing passwords for a specific website within the JSON database.
* **Clipboard Integration:** Using the `pyperclip` module to automatically copy the generated password to the user's clipboard.

## How it Works ⚙️
1. Enter the Website, Email/Username, and generate Password.
2. Click "Add" to save the entry.
3. Try "Search" to find details for a previously saved site.

# Requirements 📦
* Install pyperclip with:
`pip install pyperclip`
