from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
Gemini_Api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=Gemini_Api_key)

def question_generator(user_prompt):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt
    )
    return response

text="Artificial Intelligence (AI) refers to the simulation of human intelligence in machines These systems can learn, reason, and improve over time. AI is used in various fieldssuch as healthcare, finance, education, and transportation."
prompt=f"Generate questions from the following content:\n{text}"
output=question_generator(prompt)
print(output.text)