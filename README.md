
---

# 🧮 MathLang Interpreter

![Python](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

**MathLang** is a tiny interpreter that lets you perform mathematical calculations using plain English instead of symbols.

🔗 **Repository:** [https://guthub.com/Okalamry254/programming_lang.git](https://guthub.com/Okalamry254/programming_lang.git)

---

## ✨ Features

* 🗣️ Natural language math expressions
* ➕ Addition, ➖ Subtraction, ✖️ Multiplication, ➗ Division
* 🔄 Word ↔ Number conversion
* 💻 Interactive REPL
* 🧪 Built-in test suite
* ⚠️ Friendly error handling

---

## 📌 Examples

```text
add three and five
=> eight (8)

subtract four from twenty
=> sixteen (16)

multiply six by seven
=> forty two (42)

divide fifteen by three
=> five (5)
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://guthub.com/Okalamry254/programming_lang.git
cd programming_lang
```

---

### 2. Run the Interpreter

```bash
python mathlang.py
```

---

### 3. Use MathLang

```text
MathLang> add ten and five
=> fifteen (15)

MathLang> multiply four by six
=> twenty four (24)
```

---

### 4. Exit

```text
quit
exit
q
```

---

## 🧪 Running Tests

Run the built-in test suite:

```bash
python mathlang.py --test
```

Example output:

```text
Running MathLang tests...

[PASS] 'add three and five' => eight (8)
[PASS] 'multiply four by six' => twenty four (24)

9/9 tests passed.
```

---

## 🧠 How It Works

### 🪵 Parsing

MathLang uses simple token-based parsing:

```text
add <number> and <number>
subtract <number> from <number>
multiply <number> by <number>
divide <number> by <number>
```

---

### 🔢 Number Conversion

* `words_to_number()` → converts words into integers
* `number_to_words()` → converts integers back to words

Example:

```text
"twenty three" → 23
42 → "forty two"
```

---

## 📁 Project Structure

```text
mathlang.py
│
├── NUMBER_WORDS
├── RESULT_WORDS
├── words_to_number()
├── number_to_words()
├── parse_and_eval()
├── run_repl()
└── run_tests()
```

---

## ⚠️ Limitations

* No decimals (`3.5`)
* No negative numbers
* No nested expressions
* Limited number range
* Strict grammar rules

---

## 🔮 Future Improvements

* Support decimals & negatives
* Larger numbers (thousands, millions)
* Flexible natural language input
* Expression chaining
* GUI or web interface

---

## 🤝 Contributing

Contributions are welcome! 🚀

### 1. Fork the Repository

Click the **Fork** button on GitHub
or use:

```bash
git clone https://github.com/Okalmary254/programming_lang.git
```

---

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

---

### 3. Make Changes

* Add features
* Fix bugs
* Improve documentation

---

### 4. Commit Changes

```bash
git commit -m "Add: your feature description"
```

---

### 5. Push to GitHub

```bash
git push origin feature/your-feature-name
```

---

### 6. Open a Pull Request

Go to the original repo and click **New Pull Request**

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🌟 Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Contribute ideas

---

## 🎯 Summary

MathLang is a fun, beginner-friendly interpreter that demonstrates:

* Parsing
* Tokenization
* Language design
* Basic NLP concepts

---

⚡ *Built for learning, experimentation, and fun.*
