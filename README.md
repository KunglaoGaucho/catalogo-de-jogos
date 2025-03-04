# Loja de Jogos - Django Application

Este projeto é uma aplicação web de um catálogo de jogos, construída com Django e PostgreSQL. O projeto está dockerizado e pode ser facilmente configurado e executado em qualquer máquina com Docker e Docker Compose.

## Requisitos

Antes de começar, você precisa ter o seguinte instalado:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

- ## Como rodar a aplicação

### 1. Clone o repositório

Primeiro, clone o repositório para sua máquina:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA_CLONADA>
```

2. Crie o arquivo .env, para definir a variavel de ambiente da chave api
```bash
touch .env
```
Agora adicione dentro desse arquivo:
```bash
GOOGLE_API_KEY=sua_chave_api
```

4. Construir as imagens e rodar os containers
Com o repositório clonado, use o Docker Compose para construir as imagens e rodar os containers:
```bash
docker-compose up 
```

Este comando vai:

Criar a imagem do Django a partir do Dockerfile.
Criar a imagem do banco de dados PostgreSQL.
Subir os containers de forma que a aplicação Django e o banco de dados PostgreSQL rodem em containers separados.

5. Acessar a aplicação
Após o comando terminar, a aplicação estará rodando na porta 8000. Acesse no navegador:
http://localhost:8000

6. (Se necessário) Rodar as migrações
Se você estiver rodando a aplicação pela primeira vez ou se o banco de dados foi resetado, será necessário rodar as migrações para criar as tabelas no banco de dados:
```bash 
docker-compose exec loja_web python manage.py migrate
```
7. Criar um superusuário
Para acessar a área administrativa do Django, crie um superusuário executando:
```bash 
docker-compose exec loja_web python manage.py createsuperuser
``` 

8. Parar os containers
Quando terminar de usar a aplicação, você pode parar os containers com o seguinte comando:
```bash
docker-compose down
```
