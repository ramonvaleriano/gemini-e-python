# Bibliotecas google.
import google.generativeai as genai

# Variáveis de ambiente.
from read_env import GEMINI_API_KEY, MODELO_ESCOLHIDO

# Configurando Chave de acesso
genai.configure(api_key=GEMINI_API_KEY)

lista_de_categorias_possiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos,Produtos de Higiene Sustentáveis"

prompt_sistema = f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.
            # Lista de Categorias Válidas
            {lista_de_categorias_possiveis.split(",")}
            
            # Formato da Saída
            Produto: Nome do Produto
            Categoria: apresente a categoria do produto
            Resumo: resumo básico do produto

            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Categoria: Eletrônicos Verdes
            Resumo: Produto feito para casas e tal
        """


llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema,

)

pergunta = "Escova de dente de Bambu"

response = llm.generate_content(pergunta)
print(response.text)