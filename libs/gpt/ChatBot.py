from typing import Dict, List
import openai

class ChatBot:
    def __init__(self, message_history: List[Dict[str, str]] = []):        
        self.message_history = message_history.copy()

    def send_prompt(self, prompt: str, role: str = "user"):
        # Send the prompt to the OpenAI API and retrieve the response
        self.message_history.append({"role": role, "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message_history,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # remove all leading newlines and spaces from response.choices[0].message
        response.choices[0].message.content = response.choices[0].message.content.lstrip()
        self.message_history.append(response.choices[0].message)

        # Return the response
        return response.choices[0].message.content