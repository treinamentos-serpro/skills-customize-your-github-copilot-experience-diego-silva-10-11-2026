# 📘 Tarefa: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para administrar um catálogo de livros usando FastAPI. Você vai praticar rotas HTTP, validação de dados com modelos Pydantic e respostas apropriadas para cada operação. Os dados ficam em memória e não serão preservados quando o servidor for reiniciado.

## 🚀 Preparação

1. Instale as dependências: `python -m pip install fastapi uvicorn`
2. Complete o arquivo `starter-code.py`.
3. Inicie o servidor na pasta da tarefa: `python -m uvicorn starter-code:app --reload`
4. Abra `http://127.0.0.1:8000/docs` para explorar e testar os endpoints interativamente.

## 📝 Tarefas

### 🛠️ Consultar o catálogo

#### Descrição

Implemente endpoints para consultar os livros cadastrados. Use os modelos fornecidos para manter o formato das respostas consistente.

#### Requisitos

A API concluída deve:

- Responder a `GET /books` com a lista de livros e `200 OK`
- Responder a `GET /books/{book_id}` com o livro correspondente e `200 OK`
- Retornar `404 Not Found` quando o livro solicitado não existir

### 🛠️ Adicionar livros

#### Descrição

Permita que clientes enviem os dados de um novo livro no corpo de uma requisição e recebam o recurso criado.

#### Requisitos

A API concluída deve:

- Responder a `POST /books` usando o modelo `BookCreate` como corpo da requisição
- Gerar um ID único para o novo livro e adicioná-lo ao catálogo
- Retornar o livro criado com `201 Created`
- Usar a validação do modelo para rejeitar título ou autor vazio, com `422 Unprocessable Entity`

### 🛠️ Atualizar e remover livros

#### Descrição

Complete as operações de escrita da API permitindo atualizar ou remover um livro existente.

#### Requisitos

A API concluída deve:

- Responder a `PUT /books/{book_id}` para substituir o título e o autor do livro
- Responder a `DELETE /books/{book_id}` para removê-lo
- Retornar `404 Not Found` ao tentar atualizar ou remover um ID inexistente
- Retornar `204 No Content` ao remover um livro com sucesso

## ✅ Verificação

- Teste cada operação em `/docs` e confirme também os casos de ID inexistente e dados inválidos.
- Depois de reiniciar o servidor, confirme que os dados voltam ao catálogo inicial: a persistência em banco de dados não faz parte desta tarefa.
