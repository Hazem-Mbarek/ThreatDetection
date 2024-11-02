from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def check_violence_threat(text):
    try:
        messages = [
            {"role": "system", "content": "You are an emergency call responder. Respond with 'Yes' if the text contains violent/threatening/dangerous language or someone is in distress,asking to be saved / rescued and 'No' if it is safe/normal situation. Dont provide an explanation.use only one word"},
            {"role": "user", "content": f"Analyze this text: {text}"}
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        answer = response.choices[0].message.content.strip()
        return answer

    except Exception as e:
        return f"Error: {str(e)}" 