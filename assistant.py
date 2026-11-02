import random
import logging
import datetime
from openai import OpenAI, OpenAIError

log = logging.getLogger("assistant")
logging.basicConfig(filename="assistant.log", level=logging.INFO)
client = OpenAI()

model="gpt-4o-mini"
instructions="You are a study partner for student who has an intermediate knowledge of technology. When you answer prompts, do so with intermediate language suitable for someone learning intermediate concepts."
phrases = ["Thinking", "Pondering", "Dotting the i's", "Achieving world peace"]

def get_reply(conversation_id, user_input):
    print(random.choice(phrases)+"...")

    try:
        response = client.responses.create(
            model = model,
            conversation=conversation.id,
            instructions=instructions,
            input=user_input,
        )
    except OpenAIError as error:
        log.error(f"{datetime.datetime.now()} API error: {error}\n")
        return "failed", "An error has occured, please try again."

    if response.status != "completed":
        log.error(f"{datetime.datetime.now()} Response {response.status}\n")
        return response.status, "An error has occurred, please try again."

    return response.status, response.output_text

conversation = client.conversations.create()

first_turn = True
while True:
    if first_turn:
        user_input = input("Assistant: Hello there! Just so you know, you can type 'exit' to end our chat. What's your name?")
        first_turn = False
    else:
        user_input = input("You: ")

    if user_input.strip().lower() == "exit":
        print("Goodbye!")
        break

    status, message = get_reply(conversation.id, user_input)
    print("\nAssistant: " + message + "\n")

#may for the first input, make sure that the model knows that i am inserting my name because when I typed it in, it asked me "It looks like you mentioned "Rikaiyah." Could you clarify what you▒d like to know about it? Are you referring to a person, a concept, or something else? Let me know how I can help you!"
#instead of immediately recognizing it as my name like in lessons past