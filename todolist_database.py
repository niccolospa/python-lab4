from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
import pymysql

API_TOKEN = ""

def start():
    print("Starting")

def insert(bot, update, args):
    #args is a list
    new = " ".join(args)

    sql = "insert into task (id_task, todo) value (%s,%s)"
    connection = pymysql.connect(user="root", password="", host="localhost", database="todolist_bot")
    cursor = connection.cursor()
    cursor.execute(sql, (new,))
    cursor.close()
    connection.close()
    update.message.reply_text("The new task %s was successfully added to the list!", task)

def remove(tasks, task):
    tasks.remove(task)

def close_program(tasks):
    file = open(argv[1],"w")
    for task in tasks:
        file.write(task)

def err(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    reply = "I'm sorry, I can't do that."
    update.message.reply_text(reply)

def show(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    sql = "select todo from task"
    connection = pymysql.connect(user="root", password="", host="localhost", database="todolist_bot")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    connection.close()
    tasks = []
    for task in result:
        tasks.append(" ".join(task))

    if len(tasks) == 0:
        update.message.reply_text("Nothing to do, here!")
        return

    sortedTasks = sorted(tasks)
    reply = ""
    for task in sortedTasks:
        reply += task + '\n'
    update.message.reply_text(reply)

def main():
    '''
    AmITaskListBot
    '''



    updater = Updater(API_TOKEN)

    dp = updater.dispatcher

    start()
    dp.add_handler(MessageHandler(Filters.text, err))
    dp.add_handler(CommandHandler("showTasks", show))
    dp.add_handler(CommandHandler("newTask", insert, pass_args=True))
    # dp.add_handler(CommandHandler("removeTask", remove))
    # dp.add_handler(CommandHandler("removeAllTasks", removeall))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__': #equivalente della funzione main
    main()
