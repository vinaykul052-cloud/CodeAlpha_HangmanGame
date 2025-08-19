# task4_basic_chatbot.py

def chatbot_response(user_input):
    """
    Returns predefined responses based on user input.
    """
    user_input = user_input.lower()  # case-insensitive
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "exit":
        return "exit"
    else:
        return "Sorry, I don't understand that."

def start_chat():
    """
    Starts the chatbot loop, interacting with the user until 'exit' is typed.
    """
    print("🤖 Chatbot is running! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        if response == "exit":
            print("Bot: Chat ended. Have a nice day!")
            break
        else:
            print(f"Bot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()