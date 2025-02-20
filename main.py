from imports.toEbook import toEbook
from imports.getLibros import getLibros
from imports.getArrayNumCaps import getArrayNumCaps
from imports.capBuilder import capBuilder
import mysql.connector as sql
from concurrent.futures import ThreadPoolExecutor
import subprocess
from tqdm import tqdm
apagar = input('Desea apagar el equipo al finalizar? (s/n): ')
if apagar == 's':
    apagar = True
else:
    apagar = False
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
    args = [(url,name,arrayNumCapElement) for arrayNumCapElement in arrayNumCaps]

    with ThreadPoolExecutor(max_workers=7) as executor:
        arrayCapitulos = list(tqdm(executor.map(capBuilder, args), total=len(arrayNumCaps)))



    #break2
    subprocess.call("taskkill /F /IM chrome.exe /T", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        print(arrayCapitulos[len(arrayCapitulos)-1][1])
        lastChap = arrayCapitulos[len(arrayCapitulos)-1][1]
    except Exception as e:
        lastChap =arrayNumCaps[len(arrayCapitulos)-1]

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
    if apagar:
        subprocess.call("shutdown /s /t 1", shell=True)





    







