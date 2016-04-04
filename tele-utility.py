from telegramkey import *
import telepot
bot=telepot.Bot(token)
from pprint import pprint
import time
time.sleep(0.5)
import json, ast



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    return {'content':content_type, 'chat':chat_type, 'id':chat_id}

def pack(i):
    response=bot.getUpdates()
    pack=response[i]
    #pack=ast.literal_eval(json.dumps(pack))
    return pack

def all_pack():
    response=bot.getUpdates()
    all_pack=response
    #all_pack=ast.literal_eval(json.dumps(all_pack))
    return all_pack

def text(i):
    text=pack(i)['message']['text']
    return text

def sender_id(i):
    idd=pack(i)['message']['from']['id']
    return idd

def sender_fname(i):
    fname=pack(i)['message']['from']['first_name']
    return fname



def loc_lat(i):
    lat=pack(i)['message']['location']['latitude']
    return lat

def loc_long(i):
    response=bot.getUpdates()
    longt=pack(i)['message']['location']['longitude']
    return longt

def send_txt(teleid, txt):
    bot.sendMessage(teleid, txt)

def custom_keyboard(teleid,bool):
    if bool==1:

        show_keyboard = {'keyboard': [['Yes','No','superyes'], ['Maybe','Maybe not']]}
        bot.sendMessage(teleid, 'This is a custom keyboard', reply_markup=show_keyboard)
    elif bool==0:
        hide_keyboard = {'hide_keyboard': True}
        bot.sendMessage(teleid, 'I am hiding it', reply_markup=hide_keyboard)

def json_maker(dict,bool):
    json.dumps(dict, ensure_ascii=bool)


def head_finder():
    length=len(all_pack())
    for n in range(0,length):
        if 'text' in pack(n)['message']:
            #print "first if passed"
            if text(n)=="i am the head":
                #print "secoond if passed"
                headId=sender_id(n)
                headName=sender_fname(n)
                return {'name':headName,'id':headId}

        else:
            print "no text"




        



        

#pprint (pack(-1)['message']['text'])
#head_finder()
length=len(all_pack())
print length
for n in range(0,length):
    if handle(pack(n)['message'])['chat']=='group':
        if 'text' in pack(n)['message'] :
            print text(n)
#pprint (pack(1))
#pprint (all_pack())
text='this is a test text'
#send_txt(-133850677, text)

#print text(-1)
#print sender_fname(-1)
#print sender_id(-1)
#    print "ok"
#head=head_finder()
#print head['name']
#pprint (all_pack())
#print len(all_pack())


#pprint (loc_long())
#pprint (loc_lat())
#custom_keyboard(107074443, 1)
#custom_keyboard(107074443,0)










        
