from imports.toEbook import toEbook
from imports.multiprocessing import multiprocessing
from imports.dbUpdate import dbUpdate
import subprocess

async def crearLibro(libro):
    #bucle1 iterar sobre libros

    name = libro[0][0]


    arrayCapitulos = await multiprocessing(libro)

    arrayCapitulos.sort(key=lambda x: x[1])
    subprocess.call("taskkill /F /IM chrome.exe /T", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    lastChap = dbUpdate(name, arrayCapitulos)
    print("DB actualizada")

    rutaEbook=toEbook(arrayCapitulos,name,lastChap)## ruta(str)

    return rutaEbook