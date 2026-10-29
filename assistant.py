from openai import OpenAI
client = OpenAI()

#Container for chat history - replaces client.beta.threads.create
conversation = client.conversations.create()

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit"}:
        break

    #Creates a response turn - replaces assistants.create, messages.create, runs.create, and polling
    response = client.responses.create(
        model="gpt-4o",  # Provide your model here (e.g., gpt-4o, gpt-4o-mini)
        conversation=conversation.id,
        instructions="You are a helpful assistant.",  # Replaces assistant instructions
        input=user_input  # Your user message string goes directly here
    )

    #Extract the message content directly (no loop or array matching required)
    message_for_user = response.output_text

    print("Assistant: " + message_for_user)