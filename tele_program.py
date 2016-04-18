
from teleutility import *



#pprint (all_pack())

"""
for n in range(0,length):
    if handle(pack(n)['message'])['chat']=='group':
        if 'text' in pack(n)['message'] :
            print text(n)
        elif 'location' in pack(n)['message']:
            print sender_fname(n)
            print "\t"+str(loc_long(n))
            print "\t"+str(loc_lat(n))
        else:
            print "no valid input"

"""

groupid=-133850677
mahanid=107074443
secretgroup=-146263017
v02=-117578537
theid=v02
leader=0
concern=0

errortext="I do'n't know who the leader is.  I can't realize whether you are packed with others or\
 not."+"\n"+"Leader of the pack is whose location i will be using as a cordination.to specify the leader he/she would use the command:'Tobot: I am the leader'.\
"+"\n"+"Then I will search for his/her location if it's also available here. I will set it up and you're all ready to go."


welcome="Hello, they call me the packer. 'Pack' is an old unit superior to the crowd. It means a small group of people gathered together for a purpose.\
"+"\n"+"Please specify one person as the leader using the command 'Tobot: I am the leader'."
errwelcome="Please specify one person as the leader using the command 'Tobot: I am the leader'."

multileader= "Your pack already has a leader. If you want to cancel his leadership, he/she has to send me 'Tobot: not leader anymore'"

invitationtxt="Now your pack has a leader and a concern (what connects you to other packs). Please send out your locations."+"\n"+"Sometimes you have to \
wait for some second untill your location gets more accurate"

concerninvitation="Now your pack has a leader. Please tell me why do you want to construct a pack? In this version of me you can only specify a cocern \
from the preset concern list."+"\n"+" Please do so using the command 'Tobot: give me the concern list'."

report="test"

unknown="I didn't recogenize this command"

leave= "You can always leave the group. If you don't want to continue."

#send_txt(mahanid, invitationtxt)

# the main program
C=False
A=False
B=True
while 1:
	last_m_id=message_id(-1)
	location_dict={}
	while leader==0 or concern==0:
		#the first time after code is run
		if A==False:
			send_txt(theid, welcome)
			A=True

		time.sleep(5)
		print "main while"
		# who is leader
		# a new message should be processed
		if last_m_id!=message_id(-1) and chattype(-1)=='group':
			index=len(all_pack())-1
			tmp=pack(index)
			last_m_id=message_id(-1)
			print "new message"

			if 'text' in tmp['message']:
				tmp_txt=text(index)

			#check if it's a message to define or change the leader
				if tmp_txt.lower()=="tobot: i am the leader":
					leader=sender_fname(index)
					send_txt(theid, concerninvitation)
					all_locations_dict={}
					print "leader defined"
					last_m_id=message_id(-1)
				elif tmp_txt.lower()=="tobot: give me the concern list":
					custom_keyboard(theid,1)
					time.sleep(0.5)
				elif  tmp_txt=="ICantBreath" or tmp_txt=="BlackLivesMatter" or tmp_txt=='AmINext' or tmp_txt=='RefugeesWelcome':
					custom_keyboard(theid,0)
					time.sleep(0.5)
					concern=tmp_txt
					send_txt(theid,invitationtxt)
					print "concern got"
					

				else:
					if leader!=0 and concern==0:
						send_txt(theid, "I know the leader but I am lacking your concern")
						print "no concern yet"
					elif leader==0 and concern!=0:
						send_txt(theid, "I understand your concern but i have to know who the pack leader is")
						print "no concern yet"
					else:
						send_txt(theid, "Try again, this was not a known command for me."+"\n"+errwelcome+"\n"+leave)
						print "nerror"						
					#break	
			else:
				send_txt(theid, "Try again, this was not a known message format for me."+"\n"+errwelcome+"\n"+leave)
				print "no leader defined"
							
	yes_list=[]
	no_list=[]
	while leader!=0 and concern!=0:

		#if a location arrived	
		print "leader loop"
		time.sleep(5)

		if 'location' in pack(-1)['message'] and last_m_id!=message_id(-1):
			index=len(all_pack())-1
			tmp=pack(index)
			last_m_id=message_id(-1)

			#if it's the first location was the leader
			if len(all_locations_dict)==0 and sender_fname(index)==leader:

				send_txt(theid, "okay "+sender_fname(index)+". I got it. Thanks")

				tmp_location_dict=location_dictionary_maker(sender_fname(index),loc_long(index),loc_lat(index),message_id(index))
				all_locations_dict=tmp_location_dict

				leader_long=loc_long(index)
				leader_lat=loc_lat(index)
				B=True

				print "location got"
				C=False

			#if it's the first location was not the leader
			elif len(all_locations_dict)==0 and sender_fname(index)!=leader:

				send_txt(theid, sender_fname(index)+", "+"you are not defined as the leader. Fist, I need to know where "+leader+" is.")

				B=True

				print "not the leader"
				

			#if not the first location
			else:

				if sender_fname(index) in all_locations_dict:

					#if it's an updated location of somone
					if all_locations_dict[sender_fname(index)]['id']!=message_id(index):

						tmp_location_dict=location_dictionary_maker(sender_fname(index),loc_long(index),loc_lat(index),message_id(index))
						all_locations_dict.update(tmp_location_dict)

						print "updated location got while already had some"
						C=False

						send_txt(theid, "okay "+sender_fname(index)+". I got your updated location. Thanks")

					#to ignore the same location
					elif all_locations_dict[sender_fname(index)]['id']==message_id(index):
						print "just passed"
						pass
				#if it's not the first but a new location from a new person
				else:		

						tmp_location_dict=location_dictionary_maker(sender_fname(index),loc_long(index),loc_lat(index),message_id(index))

						all_locations_dict.update(tmp_location_dict)

						print "location from a new member"
						C=False

						send_txt(theid, "okay "+sender_fname(index)+". I got your location. Thanks")

				B=True

			print "loction stored successfully"
			pprint (all_locations_dict)


		#if someone is disturbing the locationing process
		elif 'location' not in pack(-1)['message'] and last_m_id!=message_id(-1):
			index=len(all_pack())-1
			tmp=pack(index)
			last_m_id=message_id(-1)

			send_txt(theid, "For Now I am just waiting for locations. Please send your location")	
			print "when leader not location"
			
		if C==False and len(all_locations_dict)>1:

			for key in all_locations_dict:
				long2=all_locations_dict[key]['long']
				lat2=all_locations_dict[key]['lat']
				name=all_locations_dict[key]['name']
				distance=haversine(leader_long, leader_lat, long2, lat2)
				if distance !=0 and distance < 0.02:
					yes_list.append(name)
				else:
					no_list.append(name)

					#send_txt(theid, name + "You are "+str(distance)+ " apart from "+ leader)
					C=True
				B=False	
				time.sleep(1)

			if len(yes_list)>2:
				conclusion_text1="Thank you. As I understood "+'-'.join(yes_list)+" are staying together"+"Now, you have created your pack.\
				 I put yours beside many others and make sure that everyone knows about all packs including you sharing this concern.\
				And don't worry I remove all geolocation data from what you gave me and make sure no one can abuse your data."
				conclusion_text2='-'.join(no_list)+". If possible, try to find and existing pack and join that one or initiate a new one.\
				 My programmers believe there\
				is a point on being physically together as long as it's not prevented. Try again, but don't give up."
				send_txt(theid, name + "You are "+str(distance)+ " apart from "+ leader)











					


			