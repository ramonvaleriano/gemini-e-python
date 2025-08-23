from core.gemini_settings import GeminiSettings
from utils.screen import Screen


if __name__ == "__main__":
    screen = Screen()
    gemini_settings = GeminiSettings()

    while screen.contador < 3:
        result = screen.start_menu()

        if result.upper() == "SAIR":
            break

        response = gemini_settings.gerator_context(question=result, text_alone=True)

        screen.response_screen(response)

        screen.contador += 1
