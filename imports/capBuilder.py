from imports.getText import getText
from imports.translate import translate

def capBuilder(args):
    try:
        url,name,arrayNumCapElement = args
        urlCap = url+f'{arrayNumCapElement}' 
        text=getText(urlCap)##OUT: text(str)
        print(f'{name}, {arrayNumCapElement}')
        try:
            capitulo = translate(text,arrayNumCapElement)##OUT: capitulo[str,num_cap]
        except Exception as e:
            print(f'Error al traducir el capitulo {arrayNumCapElement}: {e}')               
        
        return capitulo
    except Exception as e:
        print(f'Error al crear el capitulo {arrayNumCapElement}: {e}')
        capitulo = [f'Error al crear el capitulo {arrayNumCapElement}',arrayNumCapElement]
        return capitulo
