# thaiza.dev — Portfólio

Portfólio pessoal desenvolvido com HTML, CSS e JavaScript no frontend 
e FastAPI + Python no backend.

## Tecnologias
- HTML, CSS, JavaScript
- FastAPI
- smtplib (envio de e-mails)

## Funcionalidades
- Apresentação pessoal
- Listagem de projetos
- Formulário de contato com envio real de e-mail
- Validação de formulário em JavaScript

## Como rodar localmente

1. Clone o repositório
2. Crie um arquivo `.env` com sua senha de app do Gmail:
GMAIL_SENHA=sua_senha_aqui
3. Instale as dependências:
pip install fastapi uvicorn python-dotenv
4. Rode a API:
uvicorn main:app --reload
5. Abra o `sobre.html` no navegador

# thaiza.dev — Portfólio Pessoal

Portfólio pessoal desenvolvido com HTML, CSS e JavaScript no frontend e FastAPI + Python no backend. O projeto inclui um formulário de contato funcional que salva mensagens no banco de dados e encaminha para o e-mail da desenvolvedora via Gmail.

---

## Sobre o projeto

Este portfólio foi desenvolvido como projeto acadêmico e também como vitrine profissional. O site apresenta informações pessoais, formação, projetos e um canal de contato direto. O backend foi construído seguindo boas práticas de desenvolvimento com separação de responsabilidades em camadas (routes, models, schemas, dependencies).

---

## Tecnologias utilizadas

**Frontend**
- HTML5 e CSS3
- JavaScript (validação de formulário e integração com a API)
- Fonte JetBrains Mono (Google Fonts)
- Animações com CSS puro (fundo com bolhas em movimento, transições, hover)

**Backend**
- Python 3
- FastAPI
- SQLAlchemy (ORM)
- MySQL (banco de dados)
- Pydantic com EmailStr (validação de dados)
- smtplib (envio de e-mails via Gmail)
- python-dotenv (variáveis de ambiente)

---

## Estrutura do projeto

```
portfolio/
│
├── frontend/
│   ├── sobre.html          # Página principal — apresentação
│   ├── formacao.html       # Formação acadêmica e hobbies
│   ├── portfolio.html      # Projetos
│   ├── contato.html        # Formulário de contato
│   ├── style.css           # Estilos globais
│   ├── script.js           # Validação e envio do formulário
│   └── minha-foto.png      # Foto de perfil
│
└── backend/
    ├── main.py             # Inicialização da aplicação FastAPI
    ├── database.py         # Conexão com o banco de dados
    ├── models.py           # Modelo da tabela no banco
    ├── schemas.py          # Validação de dados com Pydantic
    ├── dependencies.py     # Sessão do banco de dados
    ├── routes/
    │   └── contato.py      # Endpoints do formulário de contato
    └── .env                # Variáveis de ambiente (não versionado)
```

---

## Funcionalidades

**Frontend**
- Apresentação pessoal com foto, descrição e tecnologias
- Listagem de projetos com descrição, tecnologias e links para o GitHub
- Formação acadêmica com linha do tempo
- Formulário de contato com validação em JavaScript campo a campo
- Verificação de formato de e-mail com expressão regular
- Modal de confirmação após envio bem-sucedido
- Fundo animado com CSS puro (bolhas com movimento orgânico)
- Favicon personalizado

**Backend**
- Recebimento dos dados do formulário via `POST /contato/`
- Salvamento da mensagem no banco de dados MySQL
- Envio automático de e-mail para a desenvolvedora via Gmail SMTP
- Listagem de todas as mensagens recebidas via `GET /contato/`
- Validação de e-mail no backend com Pydantic EmailStr
- Configuração de CORS para permitir requisições do frontend

---

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/contato/` | Recebe os dados, salva no banco e envia e-mail |
| `GET` | `/contato/` | Lista todas as mensagens recebidas |

**Exemplo de corpo da requisição POST:**
```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "mensagem": "Olá, gostaria de conversar sobre uma oportunidade."
}
```

---

## Como rodar localmente

### Pré-requisitos
- Python 3.10+
- MySQL rodando localmente
- Conta Gmail com verificação em duas etapas ativa

### 1. Clone o repositório
```bash
git clone https://github.com/thaiza-d/NOME_DO_REPO.git
cd NOME_DO_REPO
```

### 2. Instale as dependências do backend
```bash
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv pydantic[email]
```

### 3. Crie o banco de dados no MySQL
```sql
CREATE DATABASE portfolio;
```

### 4. Crie o arquivo `.env` na pasta do backend
```
DB_USER=seu_usuario_mysql
DB_PASSWORD=sua_senha_mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=portfolio

MEU_EMAIL=seu_email@gmail.com
SENHA_EMAIL=sua_senha_de_app_gmail
```

> **Sobre a senha do Gmail:** não use sua senha normal. O Google exige uma **senha de app** específica.  
> Para gerar: myaccount.google.com → Segurança → Verificação em duas etapas → Senhas de app → criar para "Mail". O Google gera uma senha de 16 caracteres — essa é a que vai no `.env`.

### 5. Rode a API
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.  
A documentação automática estará em `http://127.0.0.1:8000/docs`.

### 6. Abra o frontend

Abra o arquivo `sobre.html` no navegador ou use a extensão **Live Server** do VS Code.

---

## Variáveis de ambiente

| Variável | Descrição |
|----------|-----------|
| `DB_USER` | Usuário do banco de dados MySQL |
| `DB_PASSWORD` | Senha do banco de dados MySQL |
| `DB_HOST` | Host do banco (geralmente `localhost`) |
| `DB_PORT` | Porta do banco (geralmente `3306`) |
| `DB_NAME` | Nome do banco de dados |
| `MEU_EMAIL` | E-mail Gmail para envio e recebimento |
| `SENHA_EMAIL` | Senha de app gerada pelo Google |

---

## Observações importantes

- O arquivo `.env` **não está versionado** — nunca suba credenciais para o GitHub
- Ao hospedar a API, atualize a URL do `fetch` no `script.js` de `http://127.0.0.1:8000/contato/` para a URL real do servidor
- A tabela do banco é criada automaticamente pelo SQLAlchemy ao rodar a aplicação (`Base.metadata.create_all`)

---

## Autora

**Thaiza Dantas**
- GitHub: [github.com/thaiza-d](https://github.com/thaiza-d)
- LinkedIn: [linkedin.com/in/thaiza-dantas-b312101b2](https://www.linkedin.com/in/thaiza-dantas-b312101b2/)