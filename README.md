# Sistema de Biblioteca – Tkinter + SQLite

## 📚 Descrição

Este projeto é uma aplicação de gerenciamento de biblioteca desenvolvida em Python. Utiliza a biblioteca Tkinter para a interface gráfica e SQLite para persistência de dados. O sistema permite cadastrar, visualizar, atualizar, pesquisar e excluir livros com informações como autor, título, idioma, editora, ano e preço (separado em reais e centavos).

---

## 🛠️ Funcionalidades

- ✅ Inserção de novos livros
- 🔍 Pesquisa por qualquer campo (autor, título, idioma, etc.)
- ✏️ Atualização de registros
- ❌ Exclusão de registros
- 📃 Visualização completa dos dados cadastrados
- 💰 Tratamento de valores compostos (reais e centavos)
- 🖥️ Interface gráfica com preenchimento automático ao selecionar registros
- 🧠 Armazenamento automático no banco SQLite local

---

## 🗂️ Estrutura do Projeto

```bash
biblioteca/
├── main.py               # Código principal com lógica e integração entre GUI e backend
├── backend.py            # Operações com o banco de dados (CRUD com SQLite)
├── gui.py                # Interface gráfica com Tkinter
├── biblioteca.db         # Banco de dados gerado automaticamente
└── README.md             # Este arquivo
```

## Como Usar

    Certifique-se de ter o Python 3 instalado.

    Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Execute o arquivo principal:

    python main.py

    A interface gráfica será aberta para começar a usar o sistema.

## 🧪 Requisitos

    Python 3.x

    Tkinter (já incluso com Python padrão)

## 🗃️ Sobre o banco de dados

    Usa SQLite (biblioteca.db)

    Criação automática da tabela biblioteca na primeira execução

    Campos:

        id (chave primária)

        autor (texto)

        titulo (texto)

        idioma (texto)

        editora (texto)

        ano (texto)

        reais (inteiro)

        centavos (inteiro)

## ⚙️ Observações Técnicas

    A busca utiliza OR entre os campos, retornando registros que contenham qualquer correspondência.

    O sistema armazena valores textuais com espaços corretamente como strings normais no banco (ex: "Bruno Souza").

    A pasta __pycache__ é gerada automaticamente pelo Python para armazenar arquivos compilados. Pode ser ignorada ou adicionada ao .gitignore.

## 📈 Melhorias Futuras

    Implementar busca parcial com LIKE (ex: digitar "Bruno" e retornar "Bruno Souza")

    Exportar/Importar dados em CSV

    Melhor validação de dados

    Filtros por campo (ex: ano ou editora)

    Paginação para grandes volumes de registros

### 👤 Autor

Bruno Souza – [@BruninSouz](https://github.com/BruninSouza)

### 📝 Licença

Este projeto está licenciado sob a MIT License.