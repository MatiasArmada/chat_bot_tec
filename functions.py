#librerias necesarias
from log import logger
import querys

eventos=["Eventos siguientes del cursado: \n"]
badWords=["baboso", "puta", "tonto", "pinche", "joto", "putita", "pito"]

def start(update, context):
    bot=context.bot
    chatId= update.message.chat_id
    if -1001305930012 == chatId:
        pass
    else:
        userName= update.effective_user["first_name"]
        bot.sendMessage(
        chat_id= chatId,
        parse_mode="HTML",
        text=querys.msg_start.format(userName))

#Funcion para consultar al profesor directamente
def query_teacher(update, context,text):
    bot=context.bot
    chatId= update.message.chat_id
    userName= update.effective_user["first_name"]
    #args = context.args
    #args=" ".join(args)
    args=text
    bot.sendMessage(
    chat_id= 1514482331,
    parse_mode="HTML",
    text=f"""chatID: {chatId} 
<b>{userName}</b> {args}""")


def req_teacher(update,context):
    bot=context.bot
    args = context.args
    chatId=args.pop(0)
    print(chatId)
    userName=args.pop(0)
    print(userName)
    args=" ".join(args)
    bot.sendMessage(
    chat_id= chatId,
    parse_mode="HTML",
    text=f"""<b>{userName}</b> respuesta: {args}""")


#Funcion que envia un mensaje al chat administrador
def msg_admin(context, text, userName):
    bot=context.bot
    chatId=1514482331
    bot.sendMessage(
    chat_id= chatId,
    parse_mode="HTML",
    text=f"<b>{userName}</b> dijo {text}")


def getClasesInfo(update, context):
    bot = context.bot
    chatId=update.message.chat_id
    if -1001305930012 == chatId:
        pass
    else:
        userName = update.effective_user["first_name"]
        logger.info(f"El usuario {userName} ha solicitado informacion sobre las clases {chatId}")
        bot.sendMessage(
            chat_id=chatId,
            parse_mode="HTML",
            text=(querys.info_clases.format(userName))
        )

def Python(update, context):
    bot = context.bot
    chatId=update.message.chat_id
    if -1001305930012 == chatId:
        pass
    else:
        userName = update.effective_user["first_name"]
        logger.info(f"El usuario {userName} ha solicitado informacion sobre las clases")
        bot.sendMessage(
            chat_id=chatId,
            parse_mode="HTML",
            text=(querys.info_python.format(userName))
        )

def getLinks(update, context):
    bot = context.bot
    chatId=update.message.chat_id
    if -1001305930012 == chatId:
        pass
    else:
        userName = update.effective_user["first_name"]
        logger.info(f"El usuario {userName} ha solicitado el link del meet")
        bot.sendMessage(
            chat_id=chatId,
            parse_mode="HTML",
            text=(querys.links_clases)
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
        text=(querys.msg_welcome.format(userName))
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
            word = " ".join(args)
            evento = f">> {word} \n"
            eventos.append(evento) #\n>> esto sirve para que no escriba la variable y escriba varios eventos

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
    if -1001305930012 == chatId:
        pass
    else:
        userName=update.effective_user["first_name"]
        bot=context.bot
        for evento in eventos:
            if evento =="Eventos siguientes del cursado: \n":
                text=evento
            else:
                text+=evento
                
        logger.info(f"El usuario {userName} ha solicitado los eventos")
        bot.sendMessage(
            chat_id=chatId,
            text=text
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
    #msg_admin(context, text,userName)
    for badWord in badWords:
        if badWord in text.lower():
            deleteMsg(bot, chatId, messageId, userName)
            bot.sendMessage(
            chat_id= chatId,
            parse_mode="HTML",
            text=f"El mensaje de <b>{userName}</b> fue eliminado por ser <b>inapropiado</b>")
            return
    if "consulta" in text.lower():
        query_teacher(update, context,text)
        return
    elif "bot" in text.lower() and "hola" in text.lower():
        bot.sendMessage(
    chat_id= chatId,
    parse_mode="HTML",
    text=f"Hola <b>{userName}</b> soy el bot, ¿que necesitas?")

#funcion que elimina un evento
def del_event(update, context):
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
                text=f"{userName} agrega el id a borrar"
            )
        else:
            
            if int(args[0]) == 1:
             
                eventos.pop(int(args[0]))
                logger.info(f"El usuario {userName} ha eliminado un evento")
                bot.sendMessage(
                chat_id=chatId,
                text=f"{userName}, el evento se elimino correctamente"
            )
            else:
                logger.info(f"El usuario {userName} ingreso mal un parametro")

                bot.sendMessage(
                    chat_id=chatId,
                    text=f"{userName}, el evento no se elimino, ingresaste mal un parametro"
                )
    else:
        logger.info(f"El alumno/a {userName} intento eliminar un evento")
        bot.sendMessage(
                chat_id=chatId,
                text=f"{userName}, no tienes permisos para eliminar eventos"
            )


#librerias descartadas

#from pyjokes import get_joke
#from Cripto import report
#from informacionciudad import ciudad

