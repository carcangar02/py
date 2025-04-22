from imports.toEbook import toEbook
from imports.multiprocessing import process_chapters
from imports.dbUpdate import dbUpdate
from imports.getLibros import getlibros
import subprocess

apagar = input('Desea apagar el equipo al finalizar? (s/n): ')
if apagar == 's':
    apagar = True
else:
    apagar = False       
libros = getlibros()
#bucle1 iterar sobre libros

name = libros[0]


arrayCapitulos = process_chapters(libros)


arrayCapitulos.sort(key=lambda x: x[1])
subprocess.call("taskkill /F /IM chrome.exe /T", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

lastChap = dbUpdate(name, arrayCapitulos)


rutaEbook=toEbook(arrayCapitulos,name,lastChap)## ruta(str)
if apagar:
    subprocess.call("shutdown /s /t 1", shell=True)





    







