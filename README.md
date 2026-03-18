📦 API de Controle de Estoque

API REST desenvolvida em Python para gerenciamento de produtos em estoque, permitindo operações completas de CRUD (Create, Read, Update e Delete).

---

🚀 Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Swagger (documentação automática)

---

📌 Funcionalidades

- Criar produtos
- Listar produtos
- Buscar produto por ID
- Atualizar produtos
- Deletar produtos

---

🧠 Conceitos aplicados

- API REST
- Estrutura em camadas (models, schemas, services)
- ORM com SQLAlchemy
- Banco de dados relacional (SQLite)
- Documentação automática com Swagger
- Boas práticas de organização de código

---

📂 Estrutura do projeto

app/
├── main.py
├── database.py
├── models/
│ └── product.py
├── schemas/
│ └── product.py
├── services/
│ └── product_service.py

---

⚙️ Como rodar o projeto

1. Clonar o repositório

git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

2. Acessar a pasta

cd nome-do-projeto

3. Criar ambiente virtual

python -m venv venv

4. Ativar o ambiente virtual

Windows:

venv\Scripts\activate

5. Instalar dependências

pip install fastapi uvicorn sqlalchemy

6. Rodar a API

uvicorn app.main:app --reload

---

📖 Documentação da API

Após iniciar o servidor, acesse:

http://127.0.0.1:8000/docs

---

🔌 Endpoints principais

Método| Endpoint| Descrição
GET| /products| Listar produtos
GET| /products/{id}| Buscar produto por ID
POST| /products| Criar produto
PUT| /products/{id}| Atualizar produto
DELETE| /products/{id}| Deletar produto

---

💡 Exemplo de requisição

Criar produto

POST /products

{
  "name": "Mouse",
  "quantity": 10,
  "price": 59.90
}

---

🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar desenvolvimento backend utilizando Python, criação de APIs REST e integração com banco de dados.

---

📈 Próximas melhorias

- Paginação de produtos
- Filtros de busca
- Ordenação
- Autenticação de usuários (JWT)
- Banco de dados PostgreSQL

---

👨‍💻 Autor

Gadiel Almeida
GitHub: https://github.com/SEU-USUARIO
