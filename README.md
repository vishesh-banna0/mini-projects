# 🛠️ Mini Projects Collection

This repository contains **three Python mini-projects** that cover different concepts and functionalities, helping to enhance coding skills through practical applications.

---

## 🧠 1. Python Trivia Quiz Game
A fun **Python Trivia Quiz Game** that tests your knowledge of Python programming concepts. The game randomly selects 5 questions and evaluates the user's answers.

### 🔧 Functions Used:
- `random.sample()` - Selects a random set of questions.
- `lower().strip()` - Normalizes user input for accurate answer comparison.
- `enumerate()` - Iterates over questions with an index for numbering.

### 💡 Approach:
1. Store a dictionary of Python-related questions and their correct answers.
2. Randomly select 5 questions from the dictionary.
3. Prompt the user for an answer, normalize input, and compare it with the correct answer.
4. Keep track of the score and display the final result.

---

## 🔐 2. Python Password Generator
A simple **Python Password Generator** that allows users to generate secure passwords with customizable options for uppercase letters, lowercase letters, special characters, and digits. The generated passwords ensure at least one of each selected type for maximum security.

### 🔧 Functions Used:
- `random.choices()` - Selects a random set of characters based on user preferences.
- `random.shuffle()` - Ensures randomness by shuffling the generated password.
- `string` module - Provides predefined sets of characters (letters, digits, punctuation).

### 💡 Approach:
1. Allow the user to choose password criteria (uppercase, lowercase, numbers, special characters).
2. Ensure at least one character from each selected category is included.
3. Generate a random password of the desired length using the selected character sets.
4. Shuffle the password to ensure randomness and display the result.

---

## 📋 3. Python To-Do List Manager
A simple **To-Do List Manager** that allows users to add, view, mark complete/incomplete, and delete tasks. The tasks are stored in a JSON file to retain data across sessions.

### 🔧 Functions Used:
- `json.load()` - Reads tasks from a JSON file.
- `json.dump()` - Saves tasks to a JSON file.
- `strip()` - Cleans up user input.
- `enumerate()` - Iterates over tasks with an index for displaying the task list.

### 💾 JSON File Usage:
- The to-do list is stored in a `todo_list.json` file.
- When the program starts, it loads the tasks from the JSON file.
- Any changes (adding, updating, deleting tasks) are saved to the file to maintain persistence.

### 💡 Approach:
1. Load tasks from the JSON file at the start of the program.
2. Provide options to **add, view, mark complete/incomplete, and delete** tasks.
3. Save tasks to the JSON file after every operation.
4. Display the list of tasks dynamically with status updates.

---

## 🤝 Contributing
Feel free to fork this repository and improve any of the projects! If you find a bug or have a feature request, open an issue.

---

