import telegram.ext
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

##################################################3
def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('945487978:AAHAsO66Z9xpjHKPIIyjUqaUKTroIAA2XTw')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            delete_msg(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            update.message.reply_text(update.message.text)

def delete_msg(bot, update):
    
    
    bot.delete_message(chat_id=-1001466055022, message_id= 0+1)
if __name__ == '__main__':
    main()

    
