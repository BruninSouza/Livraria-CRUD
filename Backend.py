import sqlite3 as sql

# Controla Conexão com o banco de dados
class TransactionObjetc(): 
    database = "biblioteca.db" # Nome do BD
    conn = None # Conexão com o bando de dados
    cur = None # Cursor
    connected = False # Status da conexão

    # Abre o banco de dados
    def connect(self):
        TransactionObjetc.conn = sql.connect(TransactionObjetc.database)
        TransactionObjetc.cur = TransactionObjetc.conn.cursor()
        TransactionObjetc.connected = True

    # Fecha conexão com banco de dados
    def disconnect(self):
        TransactionObjetc.conn.close()
        TransactionObjetc.connected = False

    # Executa funções sql, parms são os paramentros do comando
    def execute(self, sql, parms = None):
        if TransactionObjetc.connected:
            if parms == None:
                TransactionObjetc.cur.execute(sql)
            else:
                TransactionObjetc.cur.execute(sql, parms)
            return True
        else:
            return False

    # Recupera resultados de uma consulta ao DB
    def fetchall(self):
        return TransactionObjetc.cur.fetchall()

    # Salva as alterações no banco de dados
    def persist(self):
        if TransactionObjetc.connected:
            TransactionObjetc.conn.commit()
            return True
        else:
            return False

# Cria a tabela se ela ainda não existir
def initDB():
    trans = TransactionObjetc()
    trans.connect()

    trans.execute("CREATE TABLE IF NOT EXISTS biblioteca (id INTEGER PRIMARY KEY, autor VARCHAR, titulo VARCHAR" \
    ", idioma VARCHAR, editora VARCHAR, ano TEXT, reais INTEGER, centavos INTEGER)")

    trans.persist()
    trans.disconnect()

# Adiciona um novo livro ao banco de dados
def insert(autor, titulo, idioma, editora, ano, reais, centavos):
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("INSERT INTO biblioteca VALUES(NULL, ?,?,?,?,?,?,?)",\
                   (autor, titulo, idioma, editora, ano, reais, centavos))
    trans.persist()
    trans.disconnect()

# Faz uma consulta sql para exibir todos os itens do DB
def view():
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("SELECT * FROM biblioteca")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# Realiza uma consulta ao banco de dados utilizando parâmetros
def search(autor="", titulo="", idioma="", editora="", ano="", reais="", centavos=""):
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("SELECT * FROM biblioteca WHERE autor=? or titulo=? or idioma=? or editora=?"\
                   "or ano=? or reais=? or centavos=?", (autor, titulo, idioma, editora, ano, reais, centavos))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# Deleta um livro do banco de dados
def delete(id):
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("DELETE FROM biblioteca WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

# Atualiza um livro do banco de dados
def update(id, autor, titulo, idioma, editora, ano, reais, centavos):
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("UPDATE biblioteca SET autor=?, titulo=?, idioma=?, editora=?, "\
                   "ano=?, reais=?, centavos=? WHERE id=?",(autor, titulo, idioma, editora, ano, reais, centavos, id))
    trans.persist()
    trans.disconnect()
    
initDB()


