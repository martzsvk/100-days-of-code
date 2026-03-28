# Day 24: Mail Merge Project ✉️

This project takes a single letter template and a list of names to automatically generate personalized invitations for dozens of people in milliseconds.

## What I Learned 🛠️
* **File System Navigation:** Working with complex folder structures and understanding Relative File Paths
* **The `with` Keyword:** Learned the Pythonic way to open and close files automatically, ensuring no data corruption or memory leaks.
* **Read, Write & Mode:** Differentiating between read (`r`) and write (`w`) modes.

## How it Works ⚙️
1. The script reads a list of names from a text file
2. It opens a template letter containing a placeholder: `Dear [name]`
3. For every name in the list, it creates a brand new `.txt` file in the `Output` folder with the personalized content
