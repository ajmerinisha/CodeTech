
class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! How can I help you?",
            "how are you": "I'm a bot, so I don't have feelings, but I'm here to assist you!",
            "what is your name": "I'm a rule-based chatbot created to assist you.",
            "bye": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
     
        user_input = user_input.lower()

        for key in self.rules:
            if key in user_input:
                return self.rules[key]
        return "I'm sorry, I don't understand that. Can you please rephrase?"


bot = RuleBasedChatbot()
while True:
    user_input = input("You: ")
    response = bot.get_response(user_input)
    print(f"Bot: {response}")
    if "bye" in user_input.lower():
        break
