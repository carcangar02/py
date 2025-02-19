import mysql.connector as sql
def getLibros():
    try:
        db = sql.connect(
            host='localhost',
            user='root',
            password='Qwer1234',
            database='mybooks'
        )
    except Exception as e:
        print(e)
    cursor = db.cursor()  
    query = "SELECT nombreLibro FROM librosinfo;"
    cursor.execute(query) 
    resultados = cursor.fetchall()  
    for name in resultados:
        print(name[0])
    selected=input('Elige el libro:  ')
    book = ''
    for name in resultados:
        if(selected==name[0]):
            book = name[0]
            break
    if (book!=''):
        query=f"SELECT nombreLibro, URL,cap, statuses.status FROM librosinfo JOIN statuses on librosinfo.status = statuses.id_status WHERE nombreLibro = '{book}';"
        cursor.execute(query)
        libro = cursor.fetchall()
        return libro
    else:
        print('El libro seleccionado no existe')
        return