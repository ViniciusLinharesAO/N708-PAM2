# 📓 Descição

Projeto da disciplina de "Projeto Aplicado de Multiplataformas etapa 2"

---

# 👥 Membros da equipe 18

- 2323748 - Vinícius Linhares Alves de Oliveira
- 2314031 - Andrew Ribeiro Pires
- 2226022 - Maurício Conde Ramon Oliveira
- 1610329 - Artur Vinicius Araujo Vieira de Sousa
- 2313394 - Kawhan Santos

---

# 🔐 User API

API de autenticação e controle de usuários construída com Flask, PostgreSQL e JWT. Organizada com arquitetura MVC, fortemente tipada (com `pydantic`).

---

# 📦 Tecnologias

- Python 3.13
- Flask
- SQLAlchemy
- PostgreSQL (via Docker)
- Flask-Migrate (migrations)
- JWT (access & refresh tokens)
- Pydantic (validação forte)
- Docker e Docker Compose
- Makefile (atalhos de comandos)

---

# 🚀 Rodando Localmente (com Docker)

## ✅ Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Make](https://www.gnu.org/software/make/) (já vem instalado em Linux/macOS; no Windows, usar Git Bash ou WSL)

---

## ⚙️ 1. Rodar a aplicação

```bash
make up         # ou make upd para rodar em segundo plano
```

---

## 🧱 2. Preparar o banco (migrations)

```bash
make db-init
make db-migrate
make db-upgrade
```

---

# 💻 Rodando Localmente (sem Docker)

Caso prefira rodar o projeto localmente com Python instalado na sua máquina:

## ✅ Pré-requisitos

- Python 3.13 ou superior
- [PostgreSQL](https://www.postgresql.org/) rodando localmente (ou modifique a `DATABASE_URL` para outro banco)
- [Poetry](https://python-poetry.org/) (opcional) ou `pip`

---

## 🧪 1. Criar ambiente virtual e ativar

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

---

## 📦 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 🛠️ 3. Criar e configurar o arquivo `.env`

Crie um arquivo `.env` com o conteúdo abaixo:

```env
SECRET_KEY=suachavesecreta
DATABASE_URL=sqlite:///./dev.db
```

💡 Certifique-se de que o banco `userdb` já existe e que o PostgreSQL esteja rodando.

---

## 🧱 4. Rodar as migrações

```bash
flask db init     # só na primeira vez
flask db migrate -m "initial"
flask db upgrade
```

---

## 🚀 5. Iniciar o servidor

```bash
python run.py
```

A aplicação estará disponível em [http://localhost:5000](http://localhost:5000)

---

## ❌ Problemas comuns

- **ModuleNotFoundError** → Certifique-se de ativar o ambiente virtual.
- **psycopg2 error** → Instale as dependências de desenvolvimento do PostgreSQL:
  - Debian/Ubuntu: `sudo apt install libpq-dev`
  - macOS: `brew install postgresql`
- **Flask CLI não reconhece comandos** → Exporte a variável `FLASK_APP`:
  ```bash
  export FLASK_APP=run.py       # Linux/macOS
  set FLASK_APP=run.py          # Windows cmd
  ```

---

# 🧪 Testando a API

## Rotas principais:

### ▶️ Registro
```http
POST localhost:5000/auth/register
Content-Type: application/json

{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

### ▶️ Login
```http
POST localhost:5000/auth/login
Content-Type: application/json

{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

Retorno:
```json
{
  "access_token": "...",
  "refresh_token": "..."
}
```

### 🔐 Rota protegida
```http
GET localhost:5000/auth/me
Authorization: Bearer {access_token}
```

### ♻️ Refresh token
```http
POST localhost:5000/auth/refresh
Content-Type: application/json

{
  "refresh_token": "..."
}
```

---

# 🛡️ Segurança

- Tokens JWT com tipo (`access` ou `refresh`)
- Validação de entrada com Pydantic
- Hash de senha com `werkzeug.security`

---

# 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo `LICENSE` para mais informações.
