from data import completion
from data import json
from data import load_dotenv

load_dotenv()

class LLm():
    @staticmethod
    def generate_response(prompt):
        content = None
        try:
            response = completion(
                model="gemini/gemini-3.5-flash",
                messages=prompt,
                max_tokens=2048
            )
            content = response.choices[0].message.content
            content = content.replace("```json", "")
            content = content.replace("```", "")
            content = content.strip()
            return json.loads(content)
        except json.JSONDecodeError:
            print("Invalid Json. Raw model output was:")
            print(repr(content))
            return {}
        except Exception as e:
            print(f"Error:{e}")
            return {}
        