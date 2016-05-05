from telegramkey import *
import telepot
bot=telepot.Bot(token)
from pprint import pprint
import time
time.sleep(0.5)
import json, ast
from math import radians, cos, sin, asin, sqrt

def handler(msg):
    pprint(msg)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    return {'content':content_type, 'chat':chat_type, 'id':chat_id}

def chattype(i):
    ctype=handle(pack(i)['message'])['chat']
    return ctype

def pack(i):
    response=bot.getUpdates()
    pack=response[i]
    #pack=ast.literal_eval(json.dumps(pack))
    return pack


"""def leader_pack(i):
    response=bot.getUpdates()
    pack=response[i]
    #pack=ast.literal_eval(json.dumps(pack))
    return pack"""

def all_pack():
    response=bot.getUpdates()
    all_pack=response
    #all_pack=ast.literal_eval(json.dumps(all_pack))
    return all_pack
    bot.notifyOnMessage(handle)

def text(i):
    #ch.encode('ascii', 'ignore')
    text=pack(i)['message']['text']
    text=ast.literal_eval(json.dumps(text))
    return text
    
def group_id(i):
    gid=pack(i)['message']['chat']['id']
    return gid


def sender_id(i):
    idd=pack(i)['message']['from']['id']
    return idd

def message_id(i):
    idd=pack(i)['message']['message_id']
    
    return idd

def sender_fname(i):
    fname=pack(i)['message']['from']['first_name']
    return fname


def loc_lat(i):
    lat=pack(i)['message']['location']['latitude']
    return lat

def loc_long(i):
    longt=pack(i)['message']['location']['longitude']
    return longt

def send_txt(teleid, txt):
    bot.sendMessage(teleid, txt)

def custom_keyboard(teleid,bool):
    if bool==1:

        show_keyboard = {'keyboard': [["ICantBreath","BlackLivesMatter"],["Irhal","StopTheWar"], ['AmINext',"WhereIsMyVote?"],['RefugeesWelcome',"Occupy"]]}
        bot.sendMessage(teleid, 'This is the current concern list.', reply_markup=show_keyboard)
    elif bool==0:
        hide_keyboard = {'hide_keyboard': True}
        bot.sendMessage(teleid, 'I understood your concern.', reply_markup=hide_keyboard)

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



def location_dictionary_maker(name, long, lat,m_id):
    dictl={name:{'name':name, 'long':long, 'lat':lat,'id':m_id}}
    return dictl




def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

"""
        
#pprint (all_pack())
a=location_dictionary(sender_fname(-1),loc_long(-1),loc_lat(-1), -1)
b=location_dictionary(sender_fname(-3),loc_long(-3),loc_lat(-3), -3)

all_dict=a
all_dict.update(b)
pprint (all_dict)
print all_dict['Paria']['long']
#print message_id(-1)
"""

pprint (pack(-1))

if 'location' not in pack(-1)['message']:
    print "nabood"
else:
    print "bood"


#print group_id(-1)





        
