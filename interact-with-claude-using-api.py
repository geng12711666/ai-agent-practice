import anthropic

# Initialize the client
client = anthropic.Anthropic(api_key="your-api-key-here")

# Define a system prompt to give Claude a permanent persona or instructions
SYSTEM_PROMPT = "You are a helpful, witty, and concise coding assistant. Keep answers brief."

# Initialize an empty list to keep track of the conversation history
chat_history = []

print("Claude Chat Initialized. Type 'quit' or 'exit' to end the conversation.\n")

while True:
    # 1. Get the user's input
    user_message = input("You: ")
    
    # Check if the user wants to exit
    if user_message.lower() in ['quit', 'exit']:
        print("Goodbye!")
        break
        
    # Skip empty inputs
    if not user_message.strip():
        continue

    # 2. Append the user's message to the ongoing history
    chat_history.append({"role": "user", "content": user_message})

    try:
        # 3. Send the entire history (plus the system prompt) to the API
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            system=SYSTEM_PROMPT,  # System prompt stays separate from history
            messages=chat_history
        )
        
        # 4. Extract Claude's response text
        claude_reply = response.content[0].text
        print(f"\nClaude: {claude_reply}\n")
        
        # 5. Append Claude's response to the history so it's remembered next turn
        chat_history.append({"role": "assistant", "content": claude_reply})
        
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
        # Remove the last user message if the request failed to keep the history clean
        chat_history.pop()
