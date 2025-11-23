# 🎁 Amigo Secreto API - Edição Friends Pedrada

> "Я Бэтмен"

API desenvolvida com **FastAPI** e arquitetura **Clean Code** para realizar sorteios de amigo secreto de forma justa, segura e moderna. Nada de papelzinho!

## 🚀 Funcionalidades

- Sorteio Inteligente: Algoritmo de deslocamento circular (ninguém tira a si mesmo).
- Cadastro de Usuários: Sistema de contas com senhas criptografadas.
- Documentação Automática: Swagger UI interativo.
- Validação de Dados: Garante que não haja nomes duplicados ou dados inválidos.

---

## 🛠️ Como Rodar o Projeto

Siga os passos abaixo. Você precisa ter Python instalado.

### 1. Clone o repositório

    git clone https://github.com/SEU_USUARIO/Sorteio-de-Amigos-FastAPI.git
    cd Sorteio-de-Amigos-FastAPI

### 2. Crie o Ambiente Virtual

Windows:

    python -m venv venv

Linux/Mac:

    python3 -m venv venv

### 3. Ative o Ambiente

Windows:

    venv\Scripts\activate

Linux/Mac:

    source venv/bin/activate

### 4. Instale as Dependências

    pip install -r requirements.txt

### 5. Rode o servidor

    python -m uvicorn main:app --reload

---

## 📚 Como Usar (Documentação)

Com o servidor rodando, acesse:

    http://127.0.0.1:8000/docs

### Passo a passo no Swagger

1. Crie sua conta: use POST /auth/cadastro  
2. Faça login: use POST /auth/login  
3. Realize o sorteio: acesse POST /sorteio e clique em "Try it out"

JSON de exemplo:

    {
      "nomes": ["Ana", "Bruno", "Carlos", "Daniela"]
    }

---

## 💻 Tecnologias Usadas

- Python 3.13
- FastAPI
- Bcrypt & Passlib
- Pydantic
- Uvicorn

Feito com 🐍 por Wasabi.
