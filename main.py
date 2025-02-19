from imports.toEbook import toEbook
from imports.getLibros import getLibros
from imports.getArrayNumCaps import getArrayNumCaps
from imports.capBuilder import capBuilder
import mysql.connector as sql
from concurrent.futures import ThreadPoolExecutor
# ESTE ES EL MAIN
libros = getLibros()
#bucle1 iterar sobre libros
for libro in libros:
    name=libro[0]
    url=libro[1]
    num_cap=libro[2]
    status=libro[3]



    arrayCapitulos=[]
    urlCap = url+f'{num_cap}'
    #bucle2 iterar sobre capitulos pendientes 

    arrayNumCaps = getArrayNumCaps(urlCap,num_cap)##OUT: arrayNumCaps[caps]    caps(int)
    
    for arrayNumCapElement in arrayNumCaps:
            capitulo = capBuilder(url,name,arrayNumCapElement)##OUT: capitulo[arrayCapitulo,num_cap]   arrayCapitulo[str], num_cap(int)
            arrayCapitulos.append(capitulo)







    #break2



    lastChap = arrayCapitulos[len(arrayCapitulos)-1][1]


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

    rutaEbook=toEbook(arrayCapitulos,name,lastChap)## ruta(str)





    







