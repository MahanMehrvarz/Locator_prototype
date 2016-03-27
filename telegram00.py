from telegramkey import *
import telepot
bot=telepot.Bot(token)
from pprint import pprint
import time
time.sleep(0.5)

while 1:
    response=bot.getUpdates()
    lastM=response[-1]['message']['text']
    lastM=response[-1]['message']
#print pprint(response[-1])
#print bot.getMe()

    #number=response[-1]['message']['chat']['id']
    number=response[-1]['message']
    print lastM
    print number

    if lastM =="begoo":
        number=response[-1]['message']['chat']['id']
        print number
        bot.sendMessage(number, 'ridi azizam, chi bgam')
        time.sleep(0.5)
        break
