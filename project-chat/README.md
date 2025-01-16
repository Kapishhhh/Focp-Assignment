# Chat System for University of Poppleton

This project is a simple chatbot system designed for the University of Poppleton. The chatbot interacts with users by detecting keywords in their input and responding appropriately. It can also randomly select agent names, provide default responses, and log chat interactions.

---

## Features

1. **Randomized Agent Names**: The chatbot introduces itself with a random name chosen from a pre-defined list in the configuration file.
2. **Keyword Detection**: The chatbot detects specific keywords in the user's input and provides predefined responses.
3. **Random Responses**: If no keyword matches, the chatbot responds with a random generic response.
4. **Chat Logging**: All user-chatbot interactions are logged to a file for reference.
5. **Random Disconnections**: To mimic real chat systems, there is a small chance of random disconnection during the chat.

---

## Files

- `chat_config.json`: Configuration file containing agent names, keyword-based responses, and random responses.
- `chat_log.txt`: Log file where all chat interactions are saved.
- `chatbot.py`: Python script for the chat system.

---

## Configuration (`chat_config.json`)
The `chat_config.json` file contains the following keys:

- `agent_names`: A list of agent names the chatbot can use.
- `responses`: A dictionary of keywords and their corresponding responses.
- `random_responses`: A list of default responses for unmatched keywords.

### Example `chat_config.json` File
```json
{
    "agent_names": ["Alice", "Bob", "Charlie"],
    "responses": {
        "help": "Sure, I'm here to help! What do you need assistance with?",
        "library": "The library is open from 8 AM to 10 PM daily.",
        "admissions": "For admissions information, please visit our website."
    },
    "random_responses": [
        "Can you clarify that?",
        "I'm not sure I understand, could you rephrase?",
        "That's interesting, tell me more!"
    ]
}
```

---

## How to Run

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Prepare the Configuration**: Create a `chat_config.json` file with the required structure.
3. **Run the Script**:
    ```bash
    python chatbot.py
    ```
4. **Interact**: Enter your name and start chatting with the bot.

---

## Logging
All interactions between the user and the chatbot are logged in the `chat_log.txt` file in the following format:

```
[UserName]: [UserInput]
[AgentName]: [BotResponse]
```

---

## Customization

### Adding New Responses
To add new keyword-based responses, update the `responses` section in `chat_config.json`:
```json
"new_keyword": "New response for the keyword."
```

### Modifying Agent Names
Add or remove agent names in the `agent_names` list in `chat_config.json`.

### Adjusting Random Disconnection Rate
The disconnection probability is set in the `main_chat` function:
```python
if random.random() < 0.05:  # 5% chance to disconnect
```
Modify `0.05` to a different value to change the disconnection rate.

---

## Known Limitations

1. **Keyword Matching**: The chatbot uses simple substring matching for keywords, which may lead to false positives or missed matches.
2. **No Natural Language Understanding**: The system doesn't understand user intent beyond keyword detection.
3. **Random Disconnection**: While intentional, this feature may disrupt user experience.

---

## Future Improvements

1. **Advanced NLP**: Integrate natural language processing for better intent recognition.
2. **User Authentication**: Add support for user accounts and personalized responses.
3. **Web Interface**: Develop a GUI or web-based chat interface.
4. **Error Handling**: Implement better error handling for missing or invalid configuration files.

---

## License
This project is open-source and available for educational and non-commercial use. Feel free to modify and adapt it as needed.

