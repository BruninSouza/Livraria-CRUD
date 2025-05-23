import sqlite3 as sql

class TransactionObjetc():
    database = "biblioteca.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObjetc.conn = sql.connect(TransactionObjetc.database)
        TransactionObjetc.cur = TransactionObjetc.conn.cursor()
        TransactionObjetc.connected = True

    def disconnect(self):
        TransactionObjetc.conn.close()
        TransactionObjetc.connected = False

    def execute(self, sql, parms = None):
        if TransactionObjetc.connected:
            if parms == None:
                TransactionObjetc.cur.execute(sql)
            else:
                TransactionObjetc.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObjetc.cur.fetchall()

    def persist(self):
        if TransactionObjetc.connected:
            TransactionObjetc.conn.commit()
            return True
        else:
            return False

def initDB():
    trans = TransactionObjetc()
    trans.connect()

    trans.execute("CREATE TABLE IF NOT EXISTS biblioteca (id INTEGER PRIMARY KEY, autor TEXT, titulo TEXT" \
    ", idioma TEXT, editora TEXT, ano TEXT, reais INTEGER, centavos INTEGER)")

    trans.persist()
    trans.disconnect()

def insert(autor, titulo, idioma, editora, ano, reais, centavos):

    if centavos >= 100:
        reais += centavos // 100
        centavos = centavos % 100

    trans = TransactionObjetc()
    trans.connect()
    trans.execute("INSERT INTO biblioteca VALUES(NULL, ?,?,?,?,?,?,?)",\
                   (autor, titulo, idioma, editora, ano, reais, centavos))
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("SELECT * FROM biblioteca")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(autor="", titulo="", idioma="", editora="", ano="", reais="", centavos=""):
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("SELECT * FROM biblioteca WHERE autor=? or titulo=? or idioma=? or editora=?"\
                   "or ano=? or reais=? or centavos=?", (autor, titulo, idioma, editora, ano, reais, centavos))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("DELETE FROM biblioteca WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, autor, titulo, idioma, editora, ano, reais, centavos):
    trans = TransactionObjetc()
    trans.connect()
    trans.execute("UPDATE biblioteca SET autor=?, titulo=?, idioma=?, editora=?, "\
                   "ano=?, reais=?, centavos=? WHERE id=?",(autor, titulo, idioma, editora, ano, reais, centavos, id))
    trans.persist()
    trans.disconnect()
    
initDB()
