import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

class AITranslator:
    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(
            api_key=api_key
        )

    def simplify_text(self, text):

        prompt = f"""
Rewrite this medical information for a normal user.

Follow this exact format:

MEDICATION:
(one line only)

USAGE:
(maximum 1 short sentence)

WARNINGS:
(maximum 3 short bullet points)

SIDE EFFECTS:
(maximum 3 short bullet points)

INSTRUCTIONS:
(maximum 3 short bullet points)

Rules:
1. Be brief.
2. Do not copy the original medical text.
3. Summarize only.
4. Do not add new medical facts.
5. Use simple everyday words.
6. Keep the whole response under 150 words.

Return only the formatted answer.
Do not include introductions.

Medical information:
{text}
"""

        for attempt in range(3):

            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash-lite", 
                    # model="gemini-2.5-flash", 
                    # model="gemini-1.5-flash", 
                    # model="gemini-2.5-pro", 
                    contents=prompt)
                
                if response.text:
                    return response.text

                return "No summary generated."

            except Exception as e:
                print(f"Attempt {attempt + 1} failed:", e)
                time.sleep(10)

        return "AI service is temporarily unavailable. Please try again in few minutes time."