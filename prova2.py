import pymysql


conn= pymysql.connect(host='localhost', port=3306, user='root', passwd= 'root', db='fioraio')


cur= conn.cursor()


queries= ["SELECT * FROM fiori",
          "INSERT INTO clienti (nome, cognome) VALUES('Mario', 'Rossi')"]


idx = int(input(f"passami un valore minore di {len(queries)}: "))
print(f"eseguo la query : {queries[idx]}...")
n_righe = cur.execute(queries[idx])

if idx == 0:  # Assuming the first query is a SELECT query
    rows = cur.fetchall()
    for row in rows:
        print(row)
else:
    conn.commit()