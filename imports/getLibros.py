import mysql.connector as sql
import os
from  dotenv import load_dotenv


load_dotenv(dotenv_path="tokens.env")  
while True:
    try:
            db = sql.connect(
                host=os.getenv("host"),
                user=os.getenv("user"),
                password=os.getenv("password"),
                database=os.getenv("database")
            )
            if db.is_connected():
                break
    except Exception as e:
            print(e)
cursor = db.cursor() 


def getLibrosSacarTodos():
 
    query = "SELECT nombreLibro FROM librosinfo;"
    cursor.execute(query) 
    resultados = cursor.fetchall()  
    return [resultado[0] for resultado in resultados]  # Devolver solo los nombres de los libros


def getLibrosSacarInfo(libroElegido):

    cursor = db.cursor() 
    book = libroElegido
    query=f"SELECT nombreLibro, URL,cap, statuses.status FROM librosinfo JOIN statuses on librosinfo.status = statuses.id_status WHERE nombreLibro = '{book}';"
    cursor.execute(query)
    libro = cursor.fetchall()
    return libro
