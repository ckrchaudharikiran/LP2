# Define a dictionary of predefined customer responses
customer_responses = {
    "hello": "Hello! How can I assist you today?",
    "bye": "Goodbye! Have a nice day!",
    "thank you": "You're welcome!",
    "default": "I'm sorry, I didn't understand. Can you please rephrase your question?"
}


# Function to handle customer interactions
def chatbot():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        customer_input = input("Customer: ")
        customer_input = customer_input.lower()

        if customer_input in customer_responses:
            print("Chatbot:", customer_responses[customer_input])
        else:
            print("Chatbot:", customer_responses["default"])

        if customer_input == "bye":
            break


# Run the chatbot
chatbot()
