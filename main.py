from imports.getLibros import getLibrosSacarTodos, getLibrosSacarInfo
from imports.crearLibro import crearLibro
import asyncio
import subprocess
import os
from dotenv import load_dotenv
import discord



load_dotenv(dotenv_path="tokens.env")  

TOKEN = os.getenv("TOKEN")


TIEMPO_LIMITE_SEGUNDOS = 10

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)




@client.event
async def on_message(message):
    if message.author == client.user:
        return  
    

    #Comando para apagar el PC
    if message.content.lower() == "apagar":
        await message.channel.send("Apagando el PC... Buenas Noches Carlos")
        await subprocess.call("shutdown /s /t 1", shell=True)


    if message.content.lower() == "libros":
        libros = getLibrosSacarTodos()
        def check(m):
            return m.author == message.author and m.channel == message.channel

        if libros:
            libros_concatenados = "\n ".join(libros)  # Concatenar los nombres de los libros
            await message.channel.send(f"Libros disponibles:\n {libros_concatenados}")
            try:
                    msg = await client.wait_for('message', timeout=30.0, check=check)
                    if msg.content in libros:
                        libro = msg.content
                        libroInfo = getLibrosSacarInfo(libro)
                        await message.channel.send("Comenzando proceso...")
                        epubFinal= await crearLibro(libroInfo)
                        if epubFinal:
                            await message.channel.send("El libro ha sido creado con éxito.")
                    else:
                        await message.channel.send("El libro no está disponible.")



            except asyncio.TimeoutError:
                    await message.send("Se acabó el tiempo para responder.")
                    return

            



        else:
            await message.channel.send("No hay libros disponibles.")  

client.run(TOKEN)




    







