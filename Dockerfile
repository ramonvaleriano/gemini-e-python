ARG VERSION_PYTHON=3.13

FROM python:${VERSION_PYTHON}

WORKDIR /app

COPY . .

CMD [ "python3", "run.py" ]

