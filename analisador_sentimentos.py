import google.generativeai as genai

from read_env import GEMINI_API_KEY, MODELO_ESCOLHIDO

# Configurando Genai
genai.configure(api_key=GEMINI_API_KEY)


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


prompt_sistema = """
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

prompt_ususario = carrega(f"dados/avaliações-{nome_produto}.txt")

print(f"Iniciando análise de sentimentos do produto: {nome_produto}")

llm = genai.GenerativeModel(
    system_instruction=prompt_sistema,
    model_name=MODELO_ESCOLHIDO
)

resposta = llm.generate_content(prompt_ususario)
resposta_text = resposta.text

salva(f"dados/resposta-{nome_produto}.txt", resposta_text)