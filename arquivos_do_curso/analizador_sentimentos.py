import google.generativeai as genai

from settings import GEMINI_API_KEY, MODELO_ESCOLHIDO


def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")


def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")


system_intruction = """
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

nome_produto = "Camisetas de algodão orgânico"
caminho_dado = f"dados/avaliações-{nome_produto}.txt"
prompt_usuario = carrega(caminho_dado)

print("\n")
print(f"Caminho do arquivo: {caminho_dado}")
print(f"Iniciando a analisar de sentimentos: {prompt_usuario}")
print("\n")

genai.configure(api_key=GEMINI_API_KEY)

config_mode = {
    "temperature": 2,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=system_intruction,
    #generation_config=config_mode,
)

response = llm.generate_content(prompt_usuario)

print("\n\n")
print("Testando o LLM: ")
print(f"Resposta: {response.text}")
