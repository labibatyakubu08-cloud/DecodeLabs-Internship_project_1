print("AI RECOMMENDATION SYSTEM")
while True:
    print("Choose a category from the list below:")
    print("1. Action")
    print("2. Comedy")
    print("3. Science")
    print("4. Sports")
    print("5. Technology")
    print("6. Music")
    print()

    interest = input("Enter your interest: ").lower()
    
    print("Analyzing your preference...")
    print()

    if interest == "action" or interest == "1":
        print("You selected ACTION.")
        print()
        print("Recommended Movies:")
        print("- John Wick")
        print("- The Dark Knight")
        print("- Avengers: Endgame")
        print()
        print("Reason:")
        print("These movies contain exciting scenes, fast-paced storytelling, and adventure.")

    elif interest == "science" or interest == "3":

        print("You selected SCIENCE.")
        print()
        print("Recommended Content:")
        print("- Cosmos")
        print("- Interstellar")
        print("- The Martian")
        print("- National Geographic")
        print("- Discovery Science")
        print()
        print("Reason:")
        print("These recommendations focus on")
        print("scientific concepts and discoveries.")

    elif interest == "sports" or interest == "4":

        print("You selected SPORTS.")
        print()
        print("Recommended Content:")
        print("- FIFA World Cup Highlights")
        print("- NBA Top Plays")
        print("- Formula 1 Racing")
        print("- Olympic Games Documentary")
        print("- Sports Science")
        print()
        print("Reason:")
        print("These options are ideal for sports fans.")

    elif interest == "music" or interest == "5":

        print("You selected MUSIC.")
        print()
        print("Recommended Genres:")
        print("- Pop")
        print("- Rock")
        print("- Jazz")
        print("- Classical")
        print("- Hip-Hop")
        print()
        print("Reason:")
        print("These genres are popular among music lovers.")

    elif interest == "technology" or interest == "6":

        print("You selected TECHNOLOGY.")
        print()
        print("Recommended Topics:")
        print("- Artificial Intelligence")
        print("- Cybersecurity")
        print("- Web Development")
        print("- Mobile App Development")
        print("- Data Science")
        print()
        print("Reason:")
        print("These areas are important in modern technology.")

    else:

        print("Invalid input.")
        print("Please choose one of the listed categories.")

    print()
    again = input("Would you like another recommendation? (yes/no): ").lower()

    if again != "yes":
        print()
        print("==========================================")
        print(" Thank you for using the AI Recommendation")
        print("               System!")
        print("==========================================")
        break

    print()


        



