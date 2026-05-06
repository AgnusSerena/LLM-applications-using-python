import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

languages = {
    "Hindi": "Translate the given sentence into Hindi",
    "Telugu": "Translate the given sentence into Telugu",
    "French": "Translate the given sentence into French"
}

client = genai.Client(api_key=GEMINI_API_KEY)

def language_translator(user_prompt, language):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=languages[language],
            temperature=0.3,
            max_output_tokens=2000
        ),
        contents=user_prompt
    )

    return response.text


user_prompt = "hi i am agnus"
language = "Hindi"

output = language_translator(user_prompt, language)

print(output)