# Bookbot - Backend Development Capstone

BookBot is one of the capstone [Boot.dev](https://www.boot.dev) projects!

## Overview
**Bookbot** is a Python script that parses `.txt` files, counts the words, and hashes characters to their occurrences. At the end, it generates a report displaying the total number of words and the frequency of each character in the text. This project was built as a **capstone** for the backend development course on [Boot.dev](https://boot.dev/).

### 🔹 Key Features:
- 📖 Parses `.txt` files from a book repository
- 🔢 Counts the total number of words in a book
- 🔍 Calculates character occurrences in the text
- 📊 Generates a formatted report
- ⚡ Includes a **Makefile** to automate book downloads and cleanup

---

## 🚀 Installation
To set up the project locally:

```bash
git clone https://github.com/dancikmad/bookbot
cd bookbot
```

Ensure you have Python installed (Python 3.x recommended).

---

## 📌 Usage

### 1️⃣ Populate the Book Repository
The project includes a **Makefile** that automates the process of fetching books from [Project Gutenberg](https://www.gutenberg.org/).
Run the following command to download `.txt` files into the `books/` directory:

```bash
make load
```

### 2️⃣ Run Bookbot
After downloading a `.txt` file, analyze a book by running:

```bash
python3 main.py books/frankenstein.txt
```

This will output:
- 📜 The total number of words in the book
- 🔢 A breakdown of character occurrences

### 3️⃣ Cleanup
Once finished, remove the downloaded `.txt` files by running:

```bash
make clean
```

---

## 📊 Example Output
```
75767 words found in the document
Character occurrences:
- 'a': 25421
- 'b': 4605
- 'c': 8814
- 'd': 16158
- ...
```

---

## 📁 Project Structure
```
bookbot/
├── 📂 books/               # Directory for storing downloaded .txt files
├── 📜 main.py              # Bookbot script
├── ⚙️  Makefile             # Automation script for fetching and cleaning books
├── 📄 README.md            # Project documentation
└── 📊 stats.py             # Helper functions for counting words and characters
```

---

## 📦 Dependencies
- 🐍 Python 3.x
- 🌐 `wget` (for downloading books via Makefile)

---

## 📜 License
This project is for educational purposes and follows open-source guidelines.

---

## 👤 Author
Created as part of the **Boot.dev Backend Development Course**.

---

### 📝 Notes
- The `Makefile` simplifies the process of setting up the book repository.
- The script can analyze any `.txt` book, not just *Frankenstein*.
- Future improvements may include support for additional text processing features.


