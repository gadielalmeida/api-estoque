📦 API de Controle de Estoque

API REST desenvolvida com FastAPI para gerenciamento de produtos em estoque.

---

🚀 Funcionalidades

- Criar produtos
- Listar produtos
- Buscar produto por ID
- Atualizar produto
- Deletar produto
- Paginação com controle de página e limite
- Filtro por nome de produto
- Ordenação por preço, quantidade e nome (asc/desc)
- Resposta estruturada com metadados (total, page, limit)

---

🛠️ Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

📂 Estrutura do projeto

app/
 ├── main.py
 ├── database.py
 ├── models/
 │ └── product.py
 ├── schemas/
 │ └── product.py
 └── services/
      └── product_service.py

---

▶️ Como rodar o projeto

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install fastapi uvicorn sqlalchemy

# Rodar servidor
uvicorn app.main:app --reload

---

📌 Acessar documentação

Após rodar o servidor:

👉 http://127.0.0.1:8000/docs

---

🔎 Listar produtos

GET /products

Parâmetros:

Parâmetro| Tipo| Descrição
page| int| Número da página (default: 1)
limit| int| Itens por página (default: 10, máximo: 100)
name| string| Filtro por nome do produto
sort| string| Ordenação dos resultados

Exemplos de ordenação:

- "price"
- "price_desc"
- "quantity"
- "quantity_desc"
- "name"
- "name_desc"

---

📌 Exemplo de resposta

{
  "total": 1,
  "page": 1,
  "limit": 10,
  "data": [
    {
      "id": 1,
      "name": "Mouse",
      "quantity": 20,
      "price": 59.9
    }
  ]
}

---

🧠 Conceitos aplicados

- Arquitetura em camadas (models, schemas, services)
- Boas práticas REST
- Separação de responsabilidades
- Paginação de dados
- Filtros dinâmicos via query params
- Ordenação de resultados
- Integração com banco de dados via ORM

---

📈 Melhorias futuras

- Autenticação com JWT
- Banco de dados PostgreSQL
- Docker
- Testes automatizados
- Deploy na nuvem (Render, Railway ou AWS)

---

👨‍💻 Autor

Desenvolvido por Gadiel Almeida
