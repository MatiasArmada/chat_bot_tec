import os
import sys
import telegram
import functions
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = "5673534665:AAEKqocVGaSTmkQQNj-hlDEuWa7iqD9Owt8"
'os.getenv("TOKEN")' 


if __name__=="__main__":
    #obtener informacion del bot
    print(TOKEN)
    myBot=telegram.Bot(token=TOKEN)


#Updater se conecta y recibe los mensajes
updater=Updater(myBot.token, use_context=True)

#crear dispatcher
dp=updater.dispatcher

#crear comando para poder interactuar con el bot
dp.add_handler(CommandHandler("start", functions.start))
dp.add_handler(CommandHandler("informaciondelcurso", functions.getClasesInfo))
dp.add_handler(CommandHandler("links", functions.getLinks))
dp.add_handler(CommandHandler("agregarEvento", functions.addEvent, pass_args=True))
dp.add_handler(CommandHandler("eliminarevento", functions.del_event, pass_args=True))
dp.add_handler(CommandHandler("consulta", functions.query_teacher, pass_args=True))
dp.add_handler(CommandHandler("respuesta", functions.request_teacher, pass_args=True))
dp.add_handler(CommandHandler("evento", functions.Event))
dp.add_handler(CommandHandler("python", functions.Python))
dp.add_handler(CommandHandler("help", functions.start))


#El bot envia mensajes a un grupo en el que esta
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, functions.welcomeMessage))
dp.add_handler(MessageHandler(Filters.text, functions.echo)) #Va a leer mensajes 

updater.start_polling()#pregunta por mensajes entrantes, mantiene el bot funcionando
print("RUNNING BOT")

updater.idle()#Terminar bot con ctrl+c



#Comandos descartados para el grupo del curso

#dp.add_handler(CommandHandler("dimeunchiste", functions.Chistes))
#dp.add_handler(CommandHandler("bitcoin", functions.Bit))
#dp.add_handler(CommandHandler("ciudad", functions.datosCiudad, pass_args=True))