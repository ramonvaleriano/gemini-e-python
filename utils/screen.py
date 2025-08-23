class Screen:
    def __init__(self):
        self.contador = 0

    @staticmethod
    def start_menu():
        print("*" * 10 + "MENU" + "*" * 10)
        result = str(input("Faça sua pergunta Ou digite 'Sair': "))

        return result

    @staticmethod
    def response_screen(response):
        print("\n")
        print("$" * 10 + "RESPONSE" + "$" * 10)
        print(response)
        print("$" * 10 + "RESPONSE" + "$" * 10)
