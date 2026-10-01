# thaiza.dev — Portfólio Pessoal

Portfólio pessoal desenvolvido com HTML, CSS e JavaScript no frontend e FastAPI + Python no backend. O projeto inclui um formulário de contato funcional que salva mensagens no banco de dados e encaminha para o e-mail da desenvolvedora via Resend.

Link do portfólio: https://thaiza-dantas.netlify.app/

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
- PostgreSQL (banco de dados — Render em produção)
- Pydantic com EmailStr (validação de dados)
- Resend (envio de e-mails)
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
└── app/
    ├── main.py             # Inicialização da aplicação FastAPI
    ├── database.py         # Conexão com o banco de dados
    ├── models.py           # Modelo da tabela no banco
    ├── schemas.py          # Validação de dados com Pydantic
    ├── dependencies.py     # Sessão do banco de dados
    ├── requirements.txt    # Dependências do projeto
    ├── routes/
    │   └── contato.py      # Endpoint do formulário de contato
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
- Salvamento da mensagem no banco de dados PostgreSQL
- Envio automático de e-mail para a desenvolvedora via Resend
- Validação de e-mail no backend com Pydantic EmailStr
- Configuração de CORS para permitir requisições do frontend

---

## Endpoint da API

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/contato/` | Recebe os dados, salva no banco e envia e-mail |

**Exemplo de corpo da requisição:**
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
- PostgreSQL rodando localmente
- Conta no Resend (resend.com) — gratuito

### 1. Clone o repositório
```bash
git clone https://github.com/thaiza-d/Portifolio-Pessoal.git
cd Portifolio-Pessoal
```

### 2. Instale as dependências
```bash
pip install -r app/requirements.txt
```

### 3. Crie o banco de dados no PostgreSQL
```sql
CREATE DATABASE portfolio;
```

### 4. Crie o arquivo `.env` dentro da pasta `app/`
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/portfolio

MEU_EMAIL=seu_email@gmail.com
RESEND_API_KEY=sua_chave_do_resend
```

### 5. Rode a API
```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.  
A documentação automática estará em `http://127.0.0.1:8000/docs`.

### 6. Abra o frontend

Abra o arquivo `sobre.html` no navegador ou use a extensão **Live Server** do VS Code.

---

## Variáveis de ambiente

| Variável | Descrição |
|----------|-----------|
| `DATABASE_URL` | String de conexão com o PostgreSQL |
| `MEU_EMAIL` | E-mail que receberá as mensagens |
| `RESEND_API_KEY` | Chave de API gerada no painel do Resend |

---

## Deploy

- **Backend:** [Render](https://render.com) — Web Service com PostgreSQL gratuito
- **Frontend:** [GitHub Pages](https://pages.github.com)

A `DATABASE_URL` em produção é fornecida automaticamente pelo banco PostgreSQL do Render.

---

## Observações importantes

- O arquivo `.env` **não está versionado** — nunca suba credenciais para o GitHub
- Ao hospedar a API, atualize a URL do `fetch` no `script.js` para a URL real do servidor
- A tabela do banco é criada automaticamente pelo SQLAlchemy ao rodar a aplicação

---

## Autora

**Thaiza Dantas**
- GitHub: [github.com/thaiza-d](https://github.com/thaiza-d)
- LinkedIn: [linkedin.com/in/thaiza-dantas-b312101b2](https://www.linkedin.com/in/thaiza-dantas-b312101b2/)
