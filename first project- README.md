project 1
Rule based AI chatbot 

Developed by:
YAKUBU LABIBAT

Custom Rule-Based Chatbot
​A simple, interactive terminal-based chatbot built with Python.
This script captures user input in real-time and provides pre-programmed responses based on specified greeting phrases, questions, and conversational cues.
​
🚀 Features
​ ~ Infinite Interaction Loop: Stays active using a while True loop to continuously receive your messages.
​ ~ Case-Insensitive Greeting Matches: Automatically standardizes user inputs using .lower() to recognize variations like "Hi", "HELLO", or "hey".
​ ~ Specific Query Handling: Detects and answers common queries such as "how are you?", "who created you?", and "what can you do?".
​ ~ Smart Exit Criteria: Breaks the execution loop gracefully when a user expresses gratitude or types the shutdown command.
​ ~ Fallback Error Checking: Provides a clean default message when user text doesn't match any preconfigured rules.

​🛠️ Tech Stack & Dependencies
​Language: Python 3.x
​Dependencies: None! This script runs purely on Python's built-in input() and print() functions.

​📊 Script Architecture
​User Input Type / Phrase Chatbot Action / Response
'hi', 'hello', 'hey' Greets the user back and asks how it can help.
'how are you?' Responds with its status as an AI entity.
'who created you?' Credits OpenAI as its origin developer.
'what can you do?' Explains its capabilities to assist with a variety of tasks.
'thanks' Outputs a "You're welcome!" message and breaks the runtime loop.
Unrecognized text Triggers a fallback message stating it does not recognize the command.

