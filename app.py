import os
import sys
import logging #Para analizar que hace el bot
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pyjokes import get_joke
from Cripto import report
from informacionciudad import ciudad
eventos="Eventos siguientes del cursado:"
badWords=["baboso", "puta", "tonto", "pinche", "joto", "putita", "pito"]

#Creacion de log
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

TOKEN = os.getenv("TOKEN")
'os.getenv("TOKEN")' 

def getClasesInfo(update, context):
    bot = context.bot
    chatId=update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f"El usuario {userName} ha solicitado informacion sobre las clases")
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=(f"""Hola {userName} las clases de Pyton son los días:
    
    <b>Clase teoricas</b>
    Lunes de 19 hs a 20.30 hs
    
    <b>Clases practicas</b>
    <b>Grupo 1</b>
    Martes de 19 hs a 20.30 hs

    <b>Grupo 2</b>    
    Martes de 20.45 hs a 22.15 hs""")
    )

def Python(update, context):
    bot = context.bot
    chatId=update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f"El usuario {userName} ha solicitado informacion sobre las clases")
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=(f"""Hola {userName}¿Sabías que existen más de 700 lenguajes de programación? De hecho, algunas fuentes indican que incluso podrían existir... ¡cerca de 9000 lenguajes de programación! Aprenderlos todos sería imposible pero, por suerte, los más utilizados en la actualidad son solo 50, y entre ellos, se encuentra Python.

<b>¿Qué es y para qué sirve Python?</b>

Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. A diferencia de otros lenguajes como Java o .NET, se trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina.
Python es un lenguaje sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites.

<b>¿Dónde se utiliza Python?</b>

- Data analytics y big data
- Data mining
- Data science
- Inteligencia artificial
- Blockchain
- Machine learning 
- Desarrollo web
- Juegos y gráficos 3D

Como has podido ver, Python es un lenguaje de programación de código abierto versátil, flexible, multiplataforma y totalmente gratuito, En el presente y en el futuro tendrá una gran relevancia debido a su utilidad en campos tecnológicos en auge como la inteligencia artificial, el big data, el data science, el machine learning, el Blockchain o el desarrollo web. Su uso va en aumento y, por lo tanto, la demanda de programadores expertos en Python, también.

¿Quieres aprender Python y reorientar tu carrera profesional?
¡Aca estamos para enseñarte a usarlo! Te esperamos""")
    )

def getLinks(update, context):
    bot = context.bot
    chatId=update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f"El usuario {userName} ha solicitado el link del meet")
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=(f"""Link del meet: meet.google.com/ygj-jehr-inm

Link del Classroom: https://classroom.google.com/c/NTMxNDQ1NzU4MTgy?hl=es&cjc=7pu5weo

Link del Drive: https://drive.google.com/drive/u/2/folders/1TIXywseL5j6B2y-PoMQYAbrQ_mIDMai94ND-xxSh6OmfUPvOmYmstglPEyw124I_K35sdb3R""")
    )

def Chistes(update, context):
    bot = context.bot
    chatId=update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f"El usuario {userName} ha solicitado el link del meet")
    chiste=get_joke(language="es", category="all")
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=(f"""{chiste}""")
    )


def welcomeMessage(update, context):
    bot=context.bot
    chatId=update.message.chat_id
    updateMsg=getattr(update, "message", None)
    for user in updateMsg.new_chat_members:
        userName = user.first_name

    logger.info(f"El usuario {userName} es un nuevo alumno")

    bot.sendMessage(
        chat_id= chatId,
        parse_mode="HTML",
        text=f"""<b>¡Bienvenido al grupo de Python avanzado {userName}!</b>
En este curso vas a aprender a manejar python como el más mejor, vas a saber hacer cosas como este mensaje,
vas a poder crear aplicaciones web por medio de un framework y un poco más... Gracias por unirte!"""
    )


def userIsAdmin(chatId, userId, bot):
    try:
        groupAdmins = bot.get_chat_administrators(chatId)
        for admin in groupAdmins:
            if admin.user.id == userId:
                isAdmin = True
                return isAdmin
            else:
                isAdmin = False
        return isAdmin

    except Exception as e:
        print(e)



def addEvent(update, context):
    global eventos
    bot=context.bot
    chatId=update.message.chat_id
    userName = update.effective_user["first_name"]
    userId = update.effective_user["id"]
    args = context.args

    if userIsAdmin(chatId, userId, bot):
        if len(args) == 0:
            logger.info(f"El usuaro {userName} no ha ingresado argumentos")
            bot.sendMessage(
                chat_id=chatId,
                text=f"{userName} agrega argumentos a tu petición"
            )
        else:
            evento = " ".join(args)
            eventos = eventos + "\n>>" + evento #\n>> esto sirve para que no escriba la variable y escriba varios eventos

            logger.info(f"El usuario {userName} ha ingresado un nuevo evento")

            bot.sendMessage(
                chat_id=chatId,
                text=f"{userName}, el evento se agrego correctamente"
            )
    else:
        logger.info(f"El alumno/a {userName} intento ingresar un evento, no se le permitio")
        bot.sendMessage(
                chat_id=chatId,
                text=f"{userName}, no tienes permisos para agregar eventos"
            )
    
def Event(update, context):
    chatId=update.message.chat_id
    userName=update.effective_user["first_name"]
    bot=context.bot

    logger.info(f"El usuario {userName} ha solicitado los eventos")
    bot.sendMessage(
        chat_id=chatId,
        text=eventos
    )
#funcion que elimina el mensaje
def deleteMsg(bot, chatId, messageId, userName):
    try:
        bot.delete_message(chatId, messageId)
        logger.info(f"El mensaje de {userName} se elimino por ser inapropiado")
    except Exception as e:
        print(e)

#funcion que toma el mensaje y analiza si debe ser eliminado
def echo(update, context):
    bot=context.bot
    updateMsg= getattr(update, "message", None)
    messageId= updateMsg.message_id #Obtenemos el id del mensaje
    chatId= update.message.chat_id
    userName= update.effective_user["first_name"]
    text=update.message.text #Obtener texto que envio el usuario
    logger.info(f"El usuario {userName} a enviado un nuevo mensaje en el grupo {chatId}")

    for badWord in badWords:
        if badWord in text.lower():
            deleteMsg(bot, chatId, messageId, userName)
            bot.sendMessage(
            chat_id= chatId,
            parse_mode="HTML",
            text=f"El mensaje de <b>{userName}</b> fue eliminado por ser <b>inapropiado</b>")
            return
    if "bot" in text.lower() and "hola" in text.lower():
        bot.sendMessage(
    chat_id= chatId,
    parse_mode="HTML",
    text=f"Hola <b>{userName}</b> soy el bot, ¿que necesitas?")

def Bit(update, context):
    bot=context.bot
    chatId=update.message.chat_id
    format_result=report()
    bot.sendMessage(
        chat_id= chatId,
        parse_mode="HTML",
        text=f"{format_result}"
    )

def datosCiudad(update, context):
    bot=context.bot
    chatId=update.message.chat_id
    args = context.args
    print(args[0])
    data=ciudad(args[0])
    
    if data[6] == True:
        bot.sendMessage(
            chat_id= chatId,
            parse_mode="HTML",
            text=f"""Pais: {data[3]}
provincia: {data[2]}
latitud: {data[1]}
longitud: {data[0]}
temperatura: {data[4]}
    sensación termica: {data[5]}"""
        )
    else:
        bot.sendMessage(
            chat_id= chatId,
            parse_mode="HTML",
            text=f"{data}"
            )

if __name__=="__main__":
    #obtener informacion del bot
    myBot=telegram.Bot(token=TOKEN)

#Updater se conecta y recibe los mensajes
updater=Updater(myBot.token, use_context=True)

#crear dispatcher
dp=updater.dispatcher

#crear comando para poder interactuar con el bot
dp.add_handler(CommandHandler("calendario", getClasesInfo))
dp.add_handler(CommandHandler("links", getLinks))
dp.add_handler(CommandHandler("agregarEvento", addEvent, pass_args=True))
dp.add_handler(CommandHandler("evento", Event))
dp.add_handler(CommandHandler("dimeunchiste", Chistes))
dp.add_handler(CommandHandler("python", Python))
dp.add_handler(CommandHandler("bitcoin", Bit))
dp.add_handler(CommandHandler("ciudad", datosCiudad, pass_args=True))

#El bot envia mensajes a un grupo en el que esta
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcomeMessage))
dp.add_handler(MessageHandler(Filters.text, echo)) #Va a leer mensajes 

updater.start_polling()#pregunta por mensajes entrantes, mantiene el bot funcionando
print("RUNNING BOT")

updater.idle()#Terminar bot con ctrl+c