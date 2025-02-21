from imports.toEbook import toEbook
from imports.getLibros import getLibros
from imports.getArrayNumCaps import getArrayNumCaps
from imports.capBuilder import capBuilder
import mysql.connector as sql
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    lastChap =arrayNumCaps[len(arrayCapitulos)-1]
    args = [(url,name,arrayNumCapElement) for arrayNumCapElement in arrayNumCaps]

    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = {executor.submit(capBuilder, arg): arg for arg in args}  

        arrayCapitulos = []
        for future in tqdm(as_completed(futures), total=len(arrayNumCaps)):
            result = future.result(timeout=10)
            arrayCapitulos.append(result)
  

    arrayCapitulos.sort(key=lambda x: x[1])
    subprocess.call("taskkill /F /IM chrome.exe /T", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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

    rutaEbook=toEbook(arrayCapitulos,name,lastChap)## ruta(str)
    if apagar:
        subprocess.call("shutdown /s /t 1", shell=True)





    







