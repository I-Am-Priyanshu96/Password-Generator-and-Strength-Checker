# 🔐 Python CLI Password Generator & Strength Checker

A lightweight, command-line password management tool built in Python. This application allows users to generate customizable passwords, evaluate password strength based on length and character variety, and save credentials locally.

---

## ✨ Features

* **Customizable Password Generation:** Choose the exact password length, batch count, and toggle the inclusion of numbers and special symbols.
* **Strength Evaluation:** Scores passwords (`Weak`, `Medium`, `Strong`) by analyzing character diversity (letters, digits, symbols) and total length.
* **Local Storage:** Saves generated passwords both in active session memory and persistently to a local `passwords.txt` file.
* **Input Validation & Testing:** Includes safe input handling to prevent crashes on invalid entries, alongside built-in `doctest` verification.

---

## 🧠 Core Concepts Demonstrated

This project is structured around fundamental Python programming concepts:
* **Recursion:** `generate_password_recursive()` builds strings one character at a time.
* **Nested Loops:** `generate_batch_nested()` demonstrates multi-password generation using outer and inner iteration.
* **Data Structures:** Uses **tuples** for immutable character groups, **sets** to track unique character types, and **dictionaries** for in-memory session storage.
* **File I/O & Exception Handling:** Safely appends credentials to `passwords.txt` using `try/except` blocks.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed on your system. *(No external third-party libraries are required; the project uses only Python's built-in `random`, `string`, and `doctest` modules).*

### Installation & Usage

1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Run the application:**
   ```bash
   python password_generator.py
   ```
   *(Note: Replace `password_generator.py` with your actual filename if different).*

---

## 💻 Example Menu Flow

```text
--- Password Generator & Checker ---
1. Generate Passwords
2. Check Password Strength
3. View Saved Passwords
4. Exit

Enter Your Choice (1-4): 1
Enter password length: 14
Include digits? (y/n): y
Include symbols? (y/n): y
How many passwords to generate?: 2

Generated Passwords:
1. k9#mP2\$vL8@qR4 (Strength: Strong, Score: 6)
2. x7!nB5&wT1*zJ9 (Strength: Strong, Score: 6)
```

---

## ⚠️ Security Disclaimer

This project is intended for **educational and portfolio purposes**. Passwords are saved in plain text inside `passwords.txt` and generated using Python's standard `random` module rather than the cryptographically secure `secrets` module. Do not use this tool to store sensitive real-world account credentials.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
