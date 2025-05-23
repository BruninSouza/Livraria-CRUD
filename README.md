# Sistema de Livraria – Tkinter + SQLite

## 📚 Descrição

Este projeto é uma aplicação de gerenciamento de uma livraria desenvolvida em Python. Utiliza a biblioteca Tkinter para a interface gráfica e SQLite para persistência de dados. 

## 🛠️ Funcionalidades

- ✅ Inserção de novos livros
- 🔍 Pesquisa por qualquer campo (autor, título, idioma, etc.)
- ✏️ Atualização de registros
- ❌ Exclusão de registros
- 📃 Visualização completa dos dados cadastrados
- 💰 Tratamento de valores compostos (reais e centavos)
- 🖥️ Interface gráfica com preenchimento automático ao selecionar registros
- 🧠 Armazenamento automático no banco SQLite local

## 🗂️ Estrutura do Projeto

```bash
biblioteca/
├── .gitignore            # Arquivo de exclusão do Git
├── main.py               # Código principal com lógica e integração entre GUI e backend
├── backend.py            # Operações com o banco de dados (CRUD com SQLite)
├── gui.py                # Interface gráfica com Tkinter
├── biblioteca.db         # Banco de dados gerado automaticamente
├── LICENSE               # Licensa MIT
└── README.md             # Este arquivo

```

## Como Usar

    Certifique-se de ter o Python 3 instalado.

    Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd nome-do-repositório

Execute o arquivo principal:

    python main.py

    A interface gráfica será aberta para começar a usar o sistema.

## 🧪 Requisitos

    Python 3.x

    Tkinter (já incluso com Python padrão)

## 🗃️ Sobre o banco de dados
O banco é criado automaticamente no primeiro uso com a seguinte tabela:

```
CREATE TABLE IF NOT EXISTS biblioteca (
    id INTEGER PRIMARY KEY,
    autor VARCHAR,
    titulo VARCHAR,
    idioma VARCHAR,
    editora VARCHAR,
    ano TEXT,
    reais INTEGER,
    centavos INTEGER
)
```

## .gitignore
Este projeto inclui um arquivo .gitignore para evitar o versionamento de arquivos desnecessários, como os arquivos compilados do Python:
```
# Ignorar cache do Python
__pycache__/
*.py[cod]
```

## ⚙️ Observações Técnicas

    A busca utiliza OR entre os campos, retornando registros que contenham qualquer correspondência.

    A pasta __pycache__ é gerada automaticamente pelo Python para armazenar arquivos compilados. 

## 📈 Melhorias Futuras

    Implementar busca parcial com LIKE (ex: digitar "Bruno" e retornar "Bruno Souza")

    Exportar/Importar dados em CSV

    Melhor validação de dados

    Paginação para grandes volumes de registros

### 👤 Autor

Bruno Souza – [@BruninSouza](https://github.com/BruninSouza)

### 📝 Licença

Este projeto está licenciado sob a [Licensa MIT](LICENSE).