from google import genai
from google.genai import types

from core.settings import GEMINI_API_KEY, MODELO_GEMMA


class GeminiSettings:
    def __init__(self):
        self.__gemini_api_key = GEMINI_API_KEY
        self.__modelo_escolhido = MODELO_GEMMA
        self.client = genai.Client(api_key=self.__gemini_api_key)
        self.system_instruction = None

    def send_system_introduction(self, system_instruction):
        self.system_instruction = system_instruction
        return self.system_instruction

    def __definition_of_response(self, response, text_alone=False):
        if not response:
            return None

        if text_alone:
            return response.text

        return response

    def gerator_context(self, question, text_alone=False):
        if self.system_instruction:
            response = self.client.models.generate_content(
                model=self.__modelo_escolhido,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction
                ),
                contents=question,
            )

            response = self.__definition_of_response(
                response=response, text_alone=text_alone
            )

            return response

        response = self.client.models.generate_content(
            model=self.__modelo_escolhido, contents=question
        )

        response = self.__definition_of_response(
            response=response, text_alone=text_alone
        )

        return response
