import discord
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$emoji'):
        emojis = ['😀', '😂', '😍', '🤔', '😎', '🥳', '🤖', '😺', '👾', '🦄']
        await message.channel.send(f'Aquí tienes un emoji al azar: {random.choice(emojis)}')
    elif message.content.startswith('$lanzar_moneda'):
        resultado = random.choice(['cara', 'cruz'])
        await message.channel.send(f'Has lanzado una moneda y ha salido: {resultado}')
    if message.content.startswith('$gracias'):
        await message.channel.send("¡De nada!")
    if message.content.startswith('$chiste'):
        await message.channel.send("¿Por qué no confían los científicos en los átomos? ¡Porque lo inventan todo!")
    if message.content.startswith('$clima'):
        await message.channel.send("No puedo verificar el clima, ¡pero espero que esté agradable!")
    if message.content.startswith('$hora'):
        await message.channel.send("El tiempo es una ilusión. ¡Pero probablemente es ahora!")
    if message.content.startswith('$fecha'):
        await message.channel.send("Lo siento, no puedo ir a citas.")
    if message.content.startswith('$ayuda'):
        await message.channel.send("¿En qué puedo asistirte?")
    if message.content.startswith('$noticias'):
        await message.channel.send("No puedo traer noticias, ¡pero mantente informado!")
    if message.content.startswith('$info'):
        await message.channel.send("Estoy aquí para ayudarte con lo que necesites.")
    if message.content.startswith('$cita'):
        await message.channel.send("El único límite para nuestra realización del mañana son nuestras dudas de hoy.")
    if message.content.startswith('$consejo'):
        await message.channel.send("Sé siempre tú mismo.")
    if message.content.startswith('$inspirar'):
        await message.channel.send("La única manera de hacer un gran trabajo es amar lo que haces.")
    if message.content.startswith('$dato'):
        await message.channel.send("¿Sabías que la miel nunca se echa a perder?")
    if message.content.startswith('$juego'):
        await message.channel.send("¡Juguemos! Adivina el número que estoy pensando.")
    if message.content.startswith('$libro'):
        await message.channel.send("Leer es al mente lo que el ejercicio es al cuerpo.")
    if message.content.startswith('$pelicula'):
        await message.channel.send("¿Qué tal ver 'Inception'? Es una gran película.")
    if message.content.startswith('$musica'):
        await message.channel.send("La música calma el alma.")
    if message.content.startswith('$bailar'):
        await message.channel.send("Me encantaría bailar, ¡pero no tengo pies!")
    if message.content.startswith('$cantar'):
        await message.channel.send("La la la! 🎶")
    if message.content.startswith('$poema'):
        await message.channel.send("Las rosas son rojas, las violetas azules, estoy aquí para charlar y aprender de ti.")
    if message.content.startswith('$historia'):
        await message.channel.send("Había una vez, en una tierra muy lejana...")
    if message.content.startswith('$pregunta'):
        await message.channel.send("¡Pregunta lo que quieras!")
    if message.content.startswith('$respuesta'):
        await message.channel.send("La respuesta es...42.")
    if message.content.startswith('$viaje'):
        await message.channel.send("¿A dónde te gustaría ir?")
    if message.content.startswith('$comida'):
        await message.channel.send("Estoy anhelando una pizza virtual.")
    if message.content.startswith('$bebida'):
        await message.channel.send("El agua es esencial para la vida.")
    if message.content.startswith('$sueño'):
        await message.channel.send("Sueña en grande, ¡logra aún más grande!")
    if message.content.startswith('$meta'):
        await message.channel.send("Establece tus metas altas, y no te detengas hasta alcanzarlas.")
    if message.content.startswith('$motivacion'):
        await message.channel.send("Cree que puedes y ya estás a mitad de camino.")    
    # Nuevas funciones añadidas
    if message.content.startswith('$animo'):
        await message.channel.send("¡Tú puedes! No te rindas.")
    if message.content.startswith('$relajacion'):
        await message.channel.send("Respira profundamente y relájate.")
    if message.content.startswith('$meditar'):
        await message.channel.send("Encuentra un lugar tranquilo y medita por unos minutos.")
    if message.content.startswith('$ejercicio'):
        await message.channel.send("El ejercicio es bueno para el cuerpo y la mente. ¡Muévete!")
    if message.content.startswith('$salud'):
        await message.channel.send("Cuida tu salud, es lo más importante.")
    if message.content.startswith('$amigos'):
        await message.channel.send("Los amigos son la familia que elegimos.")
    if message.content.startswith('$familia'):
        await message.channel.send("La familia es el pilar de nuestra vida.")
    if message.content.startswith('$amor'):
        await message.channel.send("El amor es lo que hace girar al mundo.")
    if message.content.startswith('$felicidad'):
        await message.channel.send("La felicidad está en las pequeñas cosas.")
    if message.content.startswith('$suerte'):
        await message.channel.send("¡Buena suerte en todo lo que hagas!")
    if message.content.startswith('$fortuna'):
        await message.channel.send("La fortuna favorece a los valientes.")
    if message.content.startswith('$destino'):
        await message.channel.send("El destino está en tus manos.")
    if message.content.startswith('$aventura'):
        await message.channel.send("La vida es una gran aventura, disfrútala.")
    if message.content.startswith('$misterio'):
        await message.channel.send("El misterio es lo que hace interesante la vida.")
    if message.content.startswith('$creatividad'):
        await message.channel.send("Deja volar tu imaginación y sé creativo.")
    if message.content.startswith('$sabiduria'):
        await message.channel.send("La sabiduría viene con la experiencia.")
    if message.content.startswith('$paciencia'):
        await message.channel.send("La paciencia es una virtud.")
    if message.content.startswith('$perseverancia'):
        await message.channel.send("No te rindas, la perseverancia trae recompensas.")
    if message.content.startswith('$coraje'):
        await message.channel.send("El coraje no es la ausencia de miedo, es la conquista del miedo.")
    if message.content.startswith('$lealtad'):
        await message.channel.send("La lealtad es una de las mayores virtudes.")
    if message.content.startswith('$libertad'):
        await message.channel.send("La libertad es el derecho de cada ser humano.")
    if message.content.startswith('$respeto'):
        await message.channel.send("El respeto se gana con acciones, no con palabras.")
    if message.content.startswith('$dignidad'):
        await message.channel.send("La dignidad es el valor de uno mismo.")
    if message.content.startswith('$gratitud'):
        await message.channel.send("La gratitud es la memoria del corazón.")
    if message.content.startswith('$esperanza'):
        await message.channel.send("La esperanza es lo último que se pierde.")
    if message.content.startswith('$pensamiento'):
        await message.channel.send("Lo que piensas, lo serás.")
    if message.content.startswith('$accion'):
        await message.channel.send("Las acciones hablan más que las palabras.")
    if message.content.startswith('$victoria'):
        await message.channel.send("La victoria llega para aquellos que nunca se rinden.")
    if message.content.startswith('$aprendizaje'):
        await message.channel.send("El aprendizaje es un tesoro que te seguirá a todas partes.")
    if message.content.startswith('$arte'):
        await message.channel.send("El arte es la expresión más bella del alma.")
    if message.content.startswith('$celebrar'):
        await message.channel.send("¡Es tiempo de celebrar!")
    if message.content.startswith('$bienvenido'):
        await message.channel.send("¡Bienvenido al servidor!")
    if message.content.startswith('$cumpleaños'):
        await message.channel.send("¡Feliz cumpleaños!")
    if message.content.startswith('$festival'):
        await message.channel.send("¡Disfruta del festival!")
    if message.content.startswith('$evento'):
        await message.channel.send("Hay un evento programado para hoy.")
    if message.content.startswith('$notificacion'):
        await message.channel.send("Tienes una nueva notificación.")
    if message.content.startswith('$alerta'):
        await message.channel.send("¡Alerta! Revisa esto de inmediato.")
    if message.content.startswith('$recordatorio'):
        await message.channel.send("Aquí tienes un recordatorio importante.")
    if message.content.startswith('$reunion'):
        await message.channel.send("Hay una reunión programada para hoy.")
    if message.content.startswith('$actualizacion'):
        await message.channel.send("Hay una nueva actualización disponible.")
    if message.content.startswith('$descuento'):
        await message.channel.send("¡Aprovecha el descuento especial!")
    if message.content.startswith('$oferta'):
        await message.channel.send("Hay una nueva oferta disponible.")
    if message.content.startswith('$novedad'):
        await message.channel.send("Hay una novedad que deberías conocer.")
    if message.content.startswith('$invitacion'):
        await message.channel.send("Tienes una invitación.")
    if message.content.startswith('$regalo'):
        await message.channel.send("¡Tienes un regalo!")
    if message.content.startswith('$felicitacion'):
        await message.channel.send("¡Felicitaciones por tu logro!")
    if message.content.startswith('$bienhecho'):
        await message.channel.send("¡Bien hecho! Sigue así.")
    if message.content.startswith('$aniversario'):
        await message.channel.send("¡Feliz aniversario!")
    if message.content.startswith('$éxito'):
        await message.channel.send("El éxito es tuyo, disfrútalo.")
    if message.content.startswith('$logro'):
        await message.channel.send("¡Has alcanzado un gran logro!")
    if message.content.startswith('$superar'):
        await message.channel.send("Cada obstáculo es una oportunidad para superar.")
    if message.content.startswith('$resiliencia'):
        await message.channel.send("La resiliencia es la clave del éxito.")
    if message.content.startswith('$triunfo'):
        await message.channel.send("¡Triunfa en cada paso que des!")
    if message.content.startswith('$fortaleza'):
        await message.channel.send("La fortaleza te llevará lejos.")
    else:
        await message.channel.send(message.content)
        
client.run("MTI5Njk2ODQ1NzE1MzI4MjExMA.Gwfn8z.kP3jmSlIKGcIHLkPZUEasZ3NoxJwpIZxhbnrGg")

