#Build the AI prompt and (later) call the LLM.
from google import genai

from app.core.config import settings

class AIService:
    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def prepare_repository(self, files: list):

        prompt = """
            You are a Senior Software Engineer and Software Architect.

            Analyze the following GitHub repository.

            Generate a professional report with the following sections:

            1. Project Summary
            2. Purpose of the Project
            3. Technologies Used
            4. Project Architecture
            5. Folder Structure
            6. Code Quality Review
            7. Security Issues
            8. Performance Improvements
            9. Best Practices
            10. Overall Rating (out of 10)

            Repository Source Code:

            """

        for file in files:
            prompt += "\n----------------------------------------\n"
            prompt += f"File: {file['file_name']}\n\n"
            prompt += file["content"]
            prompt += "\n"
            return prompt    
    
    def analyze_repository(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
    )

        return response.text  