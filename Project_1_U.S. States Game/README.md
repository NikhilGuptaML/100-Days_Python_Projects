# 🗺️ Day 1 – U.S. States Game

This is a Python-based graphical game that helps users learn the **50 U.S. states**. It was built using the `turtle` graphics module and `pandas` for data handling.

> ✅ This marks Day 1 of my 100 Days of Code challenge — focused on reinforcing core Python skills through fun, real-world projects.

---

## 🎯 How It Works

- The game opens a blank U.S. map.
- Users type in the names of states.
- Correct guesses get displayed on the map at their correct location.
- The game continues until all 50 states are guessed or the user exits.
- If exited early, a CSV of missing states is generated for review.

---

## 🛠️ Tech Stack

- Python 3.10+
- `turtle` (built-in graphics library)
- `pandas`
- CSV data for all 50 states with coordinates

---

## 📂 File Structure
Day01_USStatesGame/
├── main.py # Main game logic
├── 50_states.csv # State names and coordinates
├── blank_states_img.gif # Background map of the U.S.
├── states_to_learn.csv # (Generated) States not guessed
└── README.md # This file


---

## 🚀 How to Run

1. Install dependencies:
    ```bash
    pip install pandas
    python main.py

