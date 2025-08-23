ARG VERSION_PYTHON=3.13

FROM python:${VERSION_PYTHON}

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]

