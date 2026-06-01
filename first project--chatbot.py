print("Welcome!")
print("Hello! I am a chatbot. How can I assist you today?")
print("I can help you with various tasks. Just let me know what you need!")
print("Type 'exit' anytime to stop the chatbot.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['hi', 'hello', 'hey']:
        print("Chatbot: Hello! How can I help you today?")

    elif user_input in ['how are you?']:
        print("Chatbot: I'm just a chatbot, but I'm here to help you! How can I assist you today?")
   
    elif user_input in ['who created you?']:
        print("Chatbot: I was created by OpenAI, a research organization focused on developing and promoting friendly AI.")
    
    elif user_input in ['what can you do?']:
        print("Chatbot: I can assist you with a variety of tasks, such as answering questions, providing information, and engaging in conversation. Just let me know what you need!")
    
    elif user_input in ['thanks']:
        print("Chatbot: You're welcome!")
        break
   
    else:
        print(f"Chatbot: Sorry, I don't recognise that command.Please try again or type 'exit' to stop the chatbot.")
