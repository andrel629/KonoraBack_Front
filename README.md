# 🍃 Konoha API (Front-end & Back-end)

![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Axios](https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)

Este é um projeto de estudo full-stack que demonstra a integração entre um front-end moderno em **Next.js** e um back-end em **Python** (com **FastAPI**).

O projeto simula uma pequena Wiki de Konoha, onde o front-end consome uma API (o back-end) para listar os personagens principais e exibir seus detalhes.

## ✨ Funcionalidades

* **Front-end (Next.js):** Uma interface limpa que busca e exibe os dados.
* **Back-end (FastAPI):** Uma API RESTful que serve os dados dos personagens.
* **Consumo de API:** O front-end usa `axios` para fazer requisições ao back-end.
* **Roteamento:**
    * Uma rota principal (`/`) que lista os personagens cadastrados.
    * Rotas dinâmicas (`/Persons/[per]`) que exibem detalhes de um personagem específico.

## 🛠️ Stack de Tecnologias

### Front-end
* **Next.js** (React)
* **Axios** (Para requisições HTTP)
* **Styled-Components** (Para estilização CSS-in-JS)

### Back-end
* **Python 3**
* **FastAPI** (Para a criação da API)

## 📦 API Endpoints

O back-end (rodando em `http://127.0.0.1:8000`) expõe duas rotas principais:

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/` | Retorna uma lista JSON com 3 dos 4 personagens cadastrados (Naruto, Sasuke, Sakura, Kakashi). |
| `GET` | `/personagens/{personagem}` | Retorna os dados detalhados de um personagem específico (ex: `/personagens/Naruto`). |

## 🚀 Como Executar o Projeto

Este é um "monorepo" (contém o back-end e o front-end no mesmo repositório). Siga os passos abaixo para rodar ambos os serviços.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/andrel629/KonoraBack_Front.git](https://github.com/andrel629/KonoraBack_Front.git)
cd front_and
cd blogkonora-app
# 2. Instale as dependências
npm install
# (Pode ser necessário instalar o axios separadamente)
npm install axios

# 3. Inicie o servidor de desenvolvimento
npm run dev

# 1. Navegue até a pasta do backend (substitua 'backend' pelo nome real da sua pasta)
cd back_and

# 2. Instale as dependências
pip install fastapi
pip install fastapi[standard]

# 3. Inicie o servidor
fastapi dev main.py
