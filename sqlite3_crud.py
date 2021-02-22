#connect(): realiza conexão com o banco de dados
#disconnect(): fecha a conexão com o banco de dados
#execute(self, sql, parms): executa um comando no banco de dados. recebe três parâmetros:
#self: referencia para o próprio objeto. não precisa ser informado;
#sql: comando SQL a ser executado;
#parms: vetor com os parâmetros do comando SQL. Pode ser omitido.
#fetchall(): recupera os valores recebidos de um comando select.
#persist(): realiza o commit das operações realizadas.

"""
Note que usamos a interrogação (?) ao invés
 da substituição de string (%s) para inserir valores.
 Usar a substituição de strings NÃO é 
 seguro e não deve ser usado, pois pode 
 permitir ataques de SQL injection.
 O método da interrogação é muito melhor e
 usando o SQLAlchemy é sempre melhor, pois 
 ele faz todo o tratamento para você, e 
 você não precisará se preocupar em 
 converter aspas simples em algo que o 
 SQLite aceite.
"""
import sqlite3

conn = sqlite3.connect("MEUBANCODEDADOS.db") # ou use :memory: para botá-lo na memória RAM
  
try:
    cursor = conn.cursor()
    # cria uma tabela
    cursor.execute("""CREATE TABLE albums (id INTEGER PRIMARY KEY, title text, artist text, release_date text, publisher text, media_type text)""")
    print("O BANCO DE DADOS FUNCIONOU!")
except:
    print("banco criado")


def insere():
    # insere alguns dados
    
    title = "te12478" # tenho que usar ''
    artist = 'tes'
    release_date = 'teste'
    publisher = 'te'
    media_type = 'te'
    
    cursor.execute("INSERT INTO albums VALUES (NULL, ?,?,?,?,?)", (title, artist, release_date, publisher, media_type )) 

    # POSSO USAR ISSO ABAIXO
    #strCmd= "INSERT INTO tbl_partesPecasDiversas VALUES (null, '%s', '%s', %s)" % (descricao, posicao, qty)
    #cursor.execute("INSERT INTO albums VALUES ('Glow', var, '7/24/2012', 'Xplore Records', 'MP3')")

    # salva dados no banco
    conn.commit()

    """
    # insere múltiplos registros de uma só vez usando o método "?", que é mais seguro
    albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
              ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
              ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
              ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
    conn.commit()
    return albums"""
    
#insere()

def atualiza():
    conn = sqlite3.connect("MEUBANCODEDADOS.db")
    cursor = conn.cursor()
    title = 'atualizado'# tenho que usar ''
    artist = 'atualizado'
    release_date = 'atualizado'
    publisher = 'atualizado'
    media_type = 'atualizado'
    id = 1
    #pode ser:
    #sql = """UPDATE albums SET artist = 'John Doe_teste' WHERE artist = 'Andy Hunter'"""
    cursor.execute("UPDATE albums SET title = ?, artist = ?, release_date = ?, publisher = ?, media_type = ? WHERE id = ?", (title, artist, release_date, publisher, media_type, id))
    #cursor.execute(sql)
    conn.commit()

atualiza()

def deleta(id):
    conn = sqlite3.connect("MEUBANCODEDADOS.db")
    cursor = conn.cursor()
    #pode ser:
    #sql = """ DELETE FROM albums WHERE artist = 'John Doe'"""
    #artist = 'te'
    #sql = ("DELETE FROM albums WHERE artist=? ", (artist))
    cursor.execute("DELETE FROM albums WHERE id =? ", (id,))
    conn.commit()

#deleta(2)

def pesquisa(title = "", artist= "", release_date= "", publisher= "", media_type= ""):
    conn = sqlite3.connect("MEUBANCODEDADOS.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM albums WHERE title=? or artist=? or release_date=? or publisher=? or media_type=?", (title, artist, release_date, publisher, media_type))
    rows = cursor.fetchall()
    print(rows)
    return rows

#pesquisa(title = "tes")

def mostra_tudo():
    conn = sqlite3.connect("MEUBANCODEDADOS.db")
    # todos os registros na tabela
    print("\nAqui a lista de todos os registros na tabela:\n")
    for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
        print(row)
    """    
    #Resultados de uma consulta com LIKE:
    print ("\nResultados de uma consulta com LIKE:\n")
    sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
    cursor.execute(sql)
    print ( cursor.fetchall())"""
mostra_tudo()
