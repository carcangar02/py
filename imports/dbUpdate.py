import mysql.connector as sql
from  dotenv import load_dotenv
import os


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

def dbUpdate(name, arrayCapitulos):

    try:
        print(arrayCapitulos[len(arrayCapitulos)-1][1])
        lastChap = arrayCapitulos[len(arrayCapitulos)-1][1]
    except Exception as e:
        print(e)

    query=f"UPDATE librosinfo SET cap = {lastChap} WHERE nombreLibro LIKE '{name}'"
    cursor.execute(query)
    db.commit()
    return lastChap