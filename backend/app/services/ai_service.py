#Build the AI prompt and (later) call the LLM.
from google import genai
import time
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

    def prepare_chunk(self, chunk: list):

        prompt = """
            You are a Senior Software Engineer.

            Analyze ONLY this repository chunk.

            Generate:

            1. Summary of this chunk
            2. Technologies used
            3. Code Quality
            4. Security Issues
            5. Performance Suggestions

            Repository Chunk:

            """

        for file in chunk:

            prompt += "\n----------------------------------------\n"
            prompt += f"File: {file['file_name']}\n\n"
            prompt += file["content"]
            prompt += "\n"
            return prompt
        
    def analyze_chunk(self, prompt: str) -> str:

        try:
            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return response.text

        except Exception:
            time.sleep(30)

            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return response.text

    
    def analyze_repository(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
    )

        return response.text  

    def merge_analysis(self, all_analysis: list):

        prompt = """
            You are a Principal Software Architect.

            Below are analyses of different repository chunks.

            Combine them into ONE professional software engineering report.

            Include:

            1. Project Summary
            2. Purpose
            3. Technologies Used
            4. Architecture
            5. Folder Structure
            6. Code Quality
            7. Security Review
            8. Performance Review
            9. Best Practices
            10. Overall Rating

            Chunk Analyses:

            """

        for analysis in all_analysis:

            prompt += "\n----------------------------------------\n"
            prompt += analysis
            prompt += "\n"

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text