# Bibliotecas Google.
from google import genai
from google.genai import types

# Variáveis de ambiente.
from read_env import GEMINI_API_KEY, MODELO_ESCOLHIDO

# Configurando chave de acesso.
client = genai.Client(api_key=GEMINI_API_KEY)

lista_de_categorias_possiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos,Produtos de Higiene Sustentáveis"

prompt_sistema = f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.
            # Lista de Categorias Válidas
            {lista_de_categorias_possiveis.split(",")}
            
            # Formato da Saída
            Produto: Nome do Produto
            Classificação: apresente a categoria do produto
            Resumo: resumo básico do produto

            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Classificação: Eletrônicos Verdes
            Resumo: Produto feito para casas e tal
        """

pergunta = "Escova de bambu"

response = client.models.generate_content(
    model=MODELO_ESCOLHIDO,
    config=types.GenerateContentConfig(
        system_instruction=prompt_sistema
    ),
    contents=pergunta
)

print(response.text)