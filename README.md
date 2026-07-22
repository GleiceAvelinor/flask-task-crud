
# API de Gerenciamento de Tarefas (Flask API)

Esta é uma API RESTful simples desenvolvida em **Python** utilizando o microframework **Flask**. Ela permite realizar operações de CRUD (Criar, Ler, Atualizar e Deletar) para o gerenciamento de tarefas, utilizando uma lista em memória como banco de dados temporário.

---

## 🚀 Tecnologias Utilizadas

* **Python**
* **Flask**
* **uv** (Gerenciador de dependências)

---

## 📁 Estrutura do Projeto

A organização dos arquivos e pastas do projeto segue a estrutura abaixo:

```text
seu_projeto/
├── .venv/              # Ambiente virtual Python
├── models/
│   └── task.py         # Definição da classe Task
├── .gitignore          # Arquivos ignorados pelo Git
├── main.py             # Arquivo principal da aplicação Flask
├── pyproject.toml      # Configuração e dependências do projeto
├── README.md           # Documentação do projeto
├── requirements.txt    # Lista de dependências
└── uv.lock             # Trava de dependências do uv

```

---

## ⚙️ Como Instalar e Executar

Siga os passos abaixo para rodar o projeto em sua máquina local:

### 1. Pré-requisitos

Certifique-se de ter o Python instalado. Você pode verificar executando:

```bash
python --version

```

### 2. Criar e ativar um ambiente virtual

No terminal, dentro da pasta raiz do projeto, execute:

```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual
# No Windows (PowerShell/CMD):
.venv\Scripts\activate

# No macOS/Linux:
source .venv/bin/activate

```

### 3. Instalar as dependências

Você pode utilizar o gerenciador de sua preferência (pip ou uv):

* Utilizando **pip**:
```bash
pip install -r requirements.txt

```


* Ou utilizando **uv**:
```bash
uv sync

```



### 4. Executar a aplicação

Execute o arquivo principal (`main.py`) para iniciar o servidor de desenvolvimento:

```bash
python main.py

```

O servidor estará rodando em `http://127.0.0.1:5000/`.

---

## 📌 Endpoints da API

| Método | Rota | Descrição | Corpo da Requisição (JSON) |
| --- | --- | --- | --- |
| **POST** | `/tasks` | Cria uma nova tarefa | `{"title": "Título", "description": "Descrição"}` |
| **GET** | `/tasks` | Lista todas as tarefas cadastradas | *Nenhum* |
| **GET** | `/tasks/<id>` | Busca uma tarefa específica pelo ID | *Nenhum* |
| **PUT** | `/tasks/<id>` | Atualiza uma tarefa existente | `{"title": "Novo Título", "description": "Nova Descrição", "completed": true}` |
| **DELETE** | `/tasks/<id>` | Remove uma tarefa pelo ID | *Nenhum* |

---

## 🧪 Exemplo de Uso (cURL)

### Criar uma tarefa:

```bash
curl -X POST [http://127.0.0.1:5000/tasks](http://127.0.0.1:5000/tasks) \
-H "Content-Type: application/json" \
-d '{"title": "Estudar Flask", "description": "Aprender a criar rotas e APIs REST"}'

```

### Listar tarefas:

```bash
curl [http://127.0.0.1:5000/tasks](http://127.0.0.1:5000/tasks)

```

```

```