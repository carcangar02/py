from imports.getText import getText
from imports.translate import translate

def capBuilder(args):
    try:
        url,name,arrayNumCapElement = args
        urlCap = url+f'{arrayNumCapElement}' 
        text=getText(urlCap)##OUT: text(str)
        try:
            capitulo = translate(text,arrayNumCapElement)##OUT: capitulo[str,num_cap]
        except Exception as e:
            print(f'Error al traducir el capitulo {arrayNumCapElement}')               
        
        return capitulo 
    except Exception as e:
        print(f'Error al crear el capitulo {arrayNumCapElement}')
        capitulo = [f'Error al crear el capitulo {arrayNumCapElement}',arrayNumCapElement]
        return capitulo
