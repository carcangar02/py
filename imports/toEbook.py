from ebooklib import epub
import os

def toEbook(arrayCapitulos, name,lastChap):
    # Crear el libro EPUB
    libro = epub.EpubBook()

    # Configurar título, idioma y autor del libro
    libro.set_title(name)
    libro.set_language("es")
    libro.add_author("Carlos")

    capitulos = []  # Lista para almacenar los capítulos creados

    # Bucle para agregar capítulos
    for idx, cap in enumerate(arrayCapitulos):
        # Extraer contenido y número del capítulo
        contenido = cap[0].replace("\n", "<br>") 
        num_cap = cap[1]

        # Crear un capítulo con un nombre único
        capitulo = epub.EpubHtml(
            title=f"Capítulo {num_cap}",
            file_name=f"capitulo_{num_cap}.xhtml",
            lang="es"
        )
        capitulo.content = f"""
        <h1>Capítulo {num_cap}</h1>
        <div style="white-space: pre-wrap; line-height: 1.6; font-family: Arial, sans-serif; font-size: 16px;">
            {contenido}
        </div>
        """

        # Agregar capítulo al libro y a la lista de capítulos
        libro.add_item(capitulo)
        capitulos.append(capitulo)

    # Crear el índice TOC con todos los capítulos
    libro.toc = tuple(capitulos)

    # Agregar recursos básicos
    libro.add_item(epub.EpubNcx())  # Índice navegable
    libro.add_item(epub.EpubNav())  # Navegación

    # Definir y agregar un archivo CSS para el estilo
    style = """
    body { 
        font-family: Arial, sans-serif; 
        font-size: 16px; 
        line-height: 1.6;  
        margin: 10px;
    }
    h1 { 
        color: darkblue; 
        font-size: 24px; 
    }

    """
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style
    )
    libro.add_item(nav_css)

    # Configurar el flujo de lectura (spine) incluyendo todos los capítulos
    libro.spine = ['nav'] + capitulos


    os.makedirs(f"G:\Mi unidad\ReadEra\Books\{name}", exist_ok=True)
   
    # Guardar el archivo EPUB
    epub.write_epub(f"G:\Mi unidad\ReadEra\Books\{name}\{name}-cap{arrayCapitulos[0][1]}-{lastChap}.epub", libro, {})
    # epub.write_epub(f"D:\VS\py\Libros{name}-cap{arrayCapitulos[0][1]}-{lastChap}.epub", libro, {})

    print(f"EPUB '{name}' creado correctamente.")
    return f"G:/Mi unidad/ReadEra/Books/{name}/{name}-cap{arrayCapitulos[0][1]}-{lastChap}.epub"
