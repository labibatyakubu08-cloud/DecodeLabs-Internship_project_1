Project 3-Artificial Intelligence Internship
AI RECOMMENDATION LOGIC

DEVELOPED BY:
YAKUBU LABIBAT

# AI Recommendation System

## Project Overview

This project is an **AI Recommendation System** that provides personalized recommendations based on user interests. The system uses a logic-based approach to analyze user preferences and suggest relevant content across multiple categories.

## Features

- **Interactive User Interface**: Simple command-line interface for easy user interaction
- **Multiple Categories**: Supports 6 distinct interest categories:
  - **Action**: Movie recommendations with high-energy, adventure-packed content
  - **Science**: Educational content and documentaries about scientific concepts
  - **Sports**: Sports highlights and athletic competitions
  - **Technology**: Modern tech topics including AI, cybersecurity, and web development
  - **Comedy**: Humor-based entertainment options
  - **Music**: Various music genres for different tastes

- Smart Input Handling: Accepts both number (1-6) and text input for flexibility
- Contextual Recommendations: Provides tailored suggestions with explanations for why each recommendation matches the user's interest
- Loop Functionality: Allows users to request multiple recommendations in one session
- Error Handling: Validates user input and provides guidance for invalid entries

## How It Works

1. User Selection: The system displays a list of interest categories and prompts the user to select one
2. Preference Analysis: Once a category is chosen, the system analyzes the selection
3. Recommendation Generation: Based on the selected category, the system provides:
   - Specific content recommendations (movies, shows, topics, etc.)
   - A reason explaining why these recommendations fit the user's interest
4. Continue or Exit: Users can choose to get more recommendations or exit the program

## Technical Details

- Language: Python
- Type: Logic-based recommendation system
- User Input: Command-line based
- Logic Structure: If-elif-else conditional statements for category matching

## Recommendations by Category

### Action
- John Wick
- The Dark Knight
- Avengers: Endgame

### Science
- Cosmos
- Interstellar
- The Martian
- National Geographic
- Discovery Science

### Sports
- FIFA World Cup Highlights
- NBA Top Plays
- Formula 1 Racing
- Olympic Games Documentary
- Sports Science

### Technology
- Artificial Intelligence
- Cybersecurity
- Web Development
- Mobile App Development
- Data Science

### Music
- Pop
- Rock
- Jazz
- Classical
- Hip-Hop

## Future Enhancements

- Add more categories for expanded recommendations
- Implement machine learning for smarter, adaptive recommendations
- Add user profile system to track preferences over time
- Create a database of recommendations for scalability
- Integrate with real APIs to fetch live content recommendations
- Add rating and feedback system to improve recommendations

## Installation & Running

```bash
python "project 3-AI Recommendation.py"
