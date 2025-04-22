import mysql.connector as sql

def dbUpdate(name, arrayCapitulos):

    try:
        print(arrayCapitulos[len(arrayCapitulos)-1][1])
        lastChap = arrayCapitulos[len(arrayCapitulos)-1][1]
    except Exception as e:
        print(e)

    db = sql.connect(
        host='localhost',
        user='root',
        password='Qwer1234',
        database='mybooks'
    )
    cursor=db.cursor()
    query=f"UPDATE librosinfo SET cap = {lastChap} WHERE nombreLibro LIKE '{name}'"
    cursor.execute(query)
    db.commit()
    return lastChap