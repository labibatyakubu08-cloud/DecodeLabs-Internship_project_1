# Project 1: Rule-Based AI Chatbot

**Developed by:** YAKUBU LABIBAT

## Overview

A simple, interactive terminal-based chatbot built with Python. This script captures user input in real-time and provides pre-programmed responses based on specified greeting phrases, questions, and conversational cues.

---

## 🚀 Features

- **Infinite Interaction Loop** – Stays active using a `while True` loop to continuously receive messages
- **Case-Insensitive Matching** – Automatically standardizes user inputs using `.lower()` to recognize variations like "Hi", "HELLO", or "hey"
- **Specific Query Handling** – Detects and answers common queries such as "how are you?", "who created you?", and "what can you do?"
- **Smart Exit Criteria** – Breaks the execution loop gracefully when a user expresses gratitude or types the shutdown command
- **Fallback Error Checking** – Provides a clean default message when user text doesn't match any preconfigured rules

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.x
- **Dependencies:** None! This script runs purely on Python's built-in `input()` and `print()` functions

---

## 📊 Script Architecture

| User Input / Phrase | Chatbot Action / Response |
|---|---|
| `'hi'`, `'hello'`, `'hey'` | Greets the user back and asks how it can help |
| `'how are you?'` | Responds with its status as an AI entity |
| `'who created you?'` | Credits OpenAI as its origin developer |
| `'what can you do?'` | Explains its capabilities to assist with various tasks |
| `'thanks'` | Outputs a "You're welcome!" message and breaks the runtime loop |
| Unrecognized text | Triggers a fallback message stating the command is not recognized |

---

## 🎯 Getting Started

1. Ensure you have Python 3.x installed
2. Run the chatbot script in your terminal
3. Start typing to interact with the chatbot
4. Type "thanks" to exit

---

## 📝 Example Interaction

```
You: Hello
Chatbot: Hello! How can I help you today?

You: What can you do?
Chatbot: I can assist with a variety of tasks...

You: Thanks
Chatbot: You're welcome!
```

