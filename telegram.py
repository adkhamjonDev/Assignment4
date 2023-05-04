from telegram.ext import Updater, CommandHandler

token = "5810131091:AAGlKfRwNvraXMI6WI2iWgd-9NqYx74U6ZU"


# Define a command handler
def start(update, context):
    context.bot.send_message(
        update.effective_chat.id, text="Hi there! I will notify you in case of fire, I am developed by Adkhamjon "
                                       "Rakhimov"
    )


def no_fire(update, context):
    context.bot.send_message(
        update.effective_chat.id, text="No fire detected in the room"
    )


def fire(update, context):
    context.bot.send_message(
        update.effective_chat.id, text="Fire detected in the room!"
    )


# Create an updater and add the handlers
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
