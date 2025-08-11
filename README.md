Perfeito 👍
Segue o `README.md` atualizado, sem o `exec` e já com a instrução para **startar** o contêiner:

````markdown
# 🐍 Python Gemini - Docker

Este projeto utiliza **Docker** para criar e executar a aplicação **Python Gemini**.

## 📦 Construção da Imagem

Para construir a imagem Docker, execute o seguinte comando na raiz do projeto:

```bash
docker build -t python-gemini:0.0.3 .
````

## 🚀 Executando o Contêiner

Após a imagem ser criada, execute o contêiner com:

```bash
docker run --name python-gemini python-gemini:0.0.3
```

## ▶️ Iniciando o Contêiner Parado

Se o contêiner estiver parado, inicie-o com:

```bash
docker start -a python-gemini
```

## 📝 Observações

* Substitua `0.0.3` pela versão desejada caso atualize o projeto.
* Certifique-se de ter o **Docker** instalado e em execução no seu sistema.
* Para parar o contêiner:

  ```bash
  docker stop python-gemini
  ```
* Para removê-lo:

  ```bash
  docker rm python-gemini
  ```

---

💡 **Dica:** Você pode usar `--rm` no `docker run` caso queira que o contêiner seja removido automaticamente após ser parado.
