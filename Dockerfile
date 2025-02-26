# Versão da linguagem que será usada.
FROM python:3.12-slim
# Pasta de trabalho do container.
WORKDIR /loja_games
# Copia todo o código fonte do projeto.
COPY . .
# Boa prática, sempre atualizar o pip
RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Baixa todas as dependências da aplicação
RUN pip install -r requirement.txt
# Expõe uma porta para rodar a aplicação
EXPOSE 8000
# Roda a aplicação
CMD python3 manage.py migrate  && python3 manage.py runserver 0.0.0.0:8000