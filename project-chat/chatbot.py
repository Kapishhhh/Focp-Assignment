import random
import json
import time

# Load configuration from a JSON file
with open("chat_config.json", "r") as config_file:
    config = json.load(config_file)

agent_names = config["agent_names"]
responses = config["responses"]
random_responses = config["random_responses"]

def get_random_agent_name():
    """Select a random agent name."""
    return random.choice(agent_names)

def detect_keywords(user_input):
    """Detect keywords in the user's input and provide an appropriate response."""
    for keyword, reply in responses.items():
        if keyword in user_input.lower():
            return reply
    return random.choice(random_responses)

def log_interaction(log_file, user_name, user_input, agent_name, response):
    """Log the interaction to a file."""
    with open(log_file, "a") as log:
        log.write(f"{user_name}: {user_input}\n{agent_name}: {response}\n")

def main_chat():
    """Main chat function."""
    # Greet the user and introduce the chat system
    user_name = input("Welcome! Please enter your name: ")
    print(f"Hello, {user_name}! Welcome to the University of Poppleton chat system.")

    # Introduce the virtual assistant
    agent_name = get_random_agent_name()
    print(f"My name is {agent_name}, and I'm here to assist you today.")

    log_file = "chat_log.txt"
    
    while True:
        # Randomly disconnect to mimic real chat systems
        if random.random() < 0.05:  # 5% chance to disconnect
            print(f"{agent_name}: Oops! It seems like I've been disconnected. Please try again later!")
            break

        user_input = input(f"{user_name}: ")
        
        if user_input.lower() in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye, {user_name}! Have a wonderful day!")
            break

        response = detect_keywords(user_input)
        print(f"{agent_name}: {response}")

        # Log the interaction
        log_interaction(log_file, user_name, user_input, agent_name, response)

# Run the chat system if the script is executed
if __name__ == "__main__":
    main_chat()
