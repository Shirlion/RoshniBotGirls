from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("✅ به ربات روشنی خوش آمدید!")

TOKEN = "8332352844:AAG_s3QpG3bnl8bpG1er2UR82wCmJrqNnbs"
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
