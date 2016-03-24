import textmagic.client

client = textmagic.client.TextMagicClient('mahanmeh@buffalo.edu', '10012textmagic')
import time
import random
# result = client.send("Hello, World!", "17162923620")
# message_id = result['message_id'].keys()[0]




# content of last message

def last_message():
    # all messages
    received_messages = client.receive(0)
    # constructing a tree dictionary
    messages_info = received_messages['messages']
    num_messages = len(messages_info)
    # the following line will make the list dictionary of the last message
    last = messages_info[num_messages - 1]
    # now i have to read the content of the last message so i have to call content(text)
    # from the dictionary
    last_text = last[('text')]
    last_number= last[('from')]
    return {"text":last_text,"number":last_number}



    last_text = last_text.lower()
    return last_text


# sender of last message

def finding_last_number():
    # all messages
    received_messages = client.receive(0)
    # constructing a tree dictionary
    messages_info = received_messages['messages']
    num_messages = len(messages_info)
    # the following line will make the list dictionary of the last message
    last = messages_info[num_messages - 1]
    # now i have to read the content of the last message so i have to call
    # the numer (from) from the dictionary
    last_number = last[('from')]
    last_number_string = str(last_number)
    return last_number_string


# ID of last message

def finding_last_id():
    # all messages
    received_messages = client.receive(0)
    # constructing a tree dictionary
    messages_info = received_messages['messages']
    num_messages = len(messages_info)
    # the following line will make the list dictionary of the last message
    last = messages_info[num_messages - 1]
    # now i have to read the content of the last message so i have to
    # call the numer (from) from the dictionary
    last_id = last[('message_id')]
    return last_id


# sending a text to a number

def sending_txt(txt, number):
    # sending
    result = client.send(txt, number)
    # uniqque id for a txt message
    message_id = result['message_id'].keys()[0]
    return message_id


# reading the devleivery status of a sent message
# this doesn't work for now

def status(message_id):
    response = client.message_status(message_id)
    message_info = response[message_id]
    delivery_status = message_info['status']
    time_string = time.strftime("%a, %d %b %Y %H:%M:%S", message_info['created_time'])
    return delivery_status
    return time_string


# i need to develope it but it's one of the last steps dec 03

def insist():
    return "come on, it is easy! move me please!"


# i need to develope it but it's one of the last steps dec 03

def thanking():
    return "Thanks. This was an experiment research to examine people's biases or\
    prejudices about daily activities of different ethnicities."


def thanking2():
    return "Hope You're happy with what you've done. You'll see the end result somewhere!\
     Have a good life"


# generating the random select along the 4 different ethinical names dec 04

def figure_name():
    name_list = ["Mohammad", "George", "Jing", "Gabriela"]
    figure_name = random.choice(name_list)
    return figure_name


# generating a random day time

def random_daytime():
    time_list = ["9 am", "3 pm", "7 pm", "11 pm"]
    daytime = random.choice(time_list)
    return daytime


# this is the request function

def request_txt():
    txt_req = "Hello, this is " + figure_name() + ". It's " + random_daytime() + "." + "\n" + "Where do you think\
     I should be now? Please move me over there!"
    return txt_req


# condition to start the game
def hello_check():
    last = finding_last_message()

    st = last.replace(',', '')
    str = st.replace('.', '')
    string = str.split()
    list = []
    for t in string:
        list.append(t)
    if list[0] == "hello":
        bol = True
    else:
        bol = False
    return bol


# understanding the name which is followed by hello
def p_name():
    last = last_message()['text']

    st = last.replace(',', '')
    str = st.replace('.', '')
    string = str.split()
    list = []
    for t in string:
        list.append(t)
        #list.append("")
    #del list[0]
    #last_name = ''.join(list)
    return list[-1]


# this function will get the location of figure from the sensors
# i need to develope it but i still don't have the circut

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)



