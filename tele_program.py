
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
final01=-130868018
theid=final01
Locus=0
concern=0

errortext="I do'n't know who the Locus is.  I can't realize whether you are packed with others or\
 not."+"\n"+"Locus of the pack is whose location i will be using as a cordination.to specify the Locus he/she would use the command:'Locus'.\
"+"\n"+"Then I will search for his/her location if it's also available here. I will set it up and you're all ready to go."


welcome="Hello, This is the packer prototype v 0.2. 'Pack' is an old unit superior to the crowd and refering to a small group of \
people gathered together for a purpose."+"\n"
start="The first step is to specify a locus. I constatnly check if members of your pack are close enough to him/her.Use the command 'locus' to specfy the locus"

errwelcome="Please specify one person as the Locus using the command 'Locus'."

multiLocus= "Your pack already has a Locus. If you want to cancel his Locusship, he/she has to send me 'Tobot: not Locus anymore'"

invitationtxt="Now your pack has a Locus and a concern (what connects you to other packs). Please send out your locations."+"\n"+"Sometimes you have to \
wait for some second untill your location gets more accurate"

concerninvitation="Now your pack has a Locus. Please tell me why do you want to construct a pack? In this version of me you can only specify a cocern \
from the preset concern list."+"\n"+" Please do so using the command 'concern list'."

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
	while Locus==0 or concern==0:
		#the first time after code is run
		if A==False:
			send_txt(theid, welcome)
			time.sleep(1)
			send_txt(theid, start)
			A=True

		time.sleep(1)
		print "main while"
		# who is Locus
		# a new message should be processed
		if last_m_id!=message_id(-1) and chattype(-1)=='group'and group_id(-1)==theid:
			index=len(all_pack())-1
			tmp=pack(index)
			last_m_id=message_id(-1)
			print "new message"

			if 'text' in tmp['message']:
				tmp_txt=text(index)

			#check if it's a message to define or change the Locus
				if tmp_txt.lower()=="locus":
					Locus=sender_fname(index)
					send_txt(theid, concerninvitation)
					all_locations_dict={}
					print "Locus defined"
					last_m_id=message_id(-1)
				elif tmp_txt.lower()=="concern list":
					custom_keyboard(theid,1)
					time.sleep(0.5)
				elif  tmp_txt=="ICantBreath" or tmp_txt=="BlackLivesMatter" or tmp_txt=='AmINext' or tmp_txt=='\
				RefugeesWelcome' or tmp_txt=='Irhal' or tmp_txt=='WhereIsMyVote' or "StopTheWar" or tmp_txt=='Occupy':
					custom_keyboard(theid,0)
					time.sleep(0.5)
					concern=tmp_txt
					send_txt(theid,invitationtxt)
					print "concern got"
					

				else:
					if Locus!=0 and concern==0:
						send_txt(theid, "I know the Locus but I am lacking your concern")
						print "no concern yet"
					elif Locus==0 and concern!=0:
						send_txt(theid, "I understand your concern but i have to know who the pack Locus is")
						print "no concern yet"
					else:
						send_txt(theid, "Try again, this was not a known command for me."+"\n"+errwelcome+"\n"+leave)
						print "nerror"						
					#break	
			else:
				send_txt(theid, "Try again, this was not a known message format for me."+"\n"+errwelcome+"\n"+leave)
				print "no Locus defined"
							
	
	no_list=[]
	while Locus!=0 and concern!=0:

		yes_list=[Locus]
		#if a location arrived	
		print "Locus loop"
		time.sleep(1)

		if 'location' in pack(-1)['message'] and last_m_id!=message_id(-1):
			index=len(all_pack())-1
			tmp=pack(index)
			last_m_id=message_id(-1)

			#if it's the first location was the Locus
			if len(all_locations_dict)==0 and sender_fname(index)==Locus:

				send_txt(theid, "okay "+sender_fname(index)+". I got it. Thanks")

				tmp_location_dict=location_dictionary_maker(sender_fname(index),loc_long(index),loc_lat(index),message_id(index))
				all_locations_dict=tmp_location_dict

				Locus_long=loc_long(index)
				Locus_lat=loc_lat(index)
				B=True

				print "location got"
				C=False

			#if it's the first location was not the Locus
			elif len(all_locations_dict)==0 and sender_fname(index)!=Locus:

				send_txt(theid, sender_fname(index)+", "+"you are not defined as the Locus. Fist, I need to know where "+Locus+" is.")

				B=True

				print "not the Locus"
				

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
			print "when Locus not location"
			
		if C==False and len(all_locations_dict)>1:

			print "in dictionary"

			for key in all_locations_dict:
				print "for"
				long2=all_locations_dict[key]['long']
				lat2=all_locations_dict[key]['lat']
				name=all_locations_dict[key]['name']
				distance=haversine(Locus_long, Locus_lat, long2, lat2)
				#if distance !=0 and distance < 0.08:
				if distance !=0 :
					yes_list.append(name)
					print "yes list"
					pprint (yes_list)
				else:
					no_list.append(name)
					print "yes list"

					#send_txt(theid, name + "You are "+str(distance)+ " apart from "+ Locus)
					C=True
				B=False	
				time.sleep(1)

			if len(yes_list)>3:

				conclusion_text1="As I understood "+"\n"+' & '.join(yes_list)+" are staying together."
				conclusion_text11="You have created your pack."
				conclusion_text2="I put yours beside many others and make sure that everyone knows about all packs including you sharing this concern."
				conclusion_text3=' & '.join(no_list)+".If possible, try to find an existing pack and join that one or initiate a new one."
				
				
				send_txt(theid, conclusion_text1)
				time.sleep(0.5)
				send_txt(theid, conclusion_text11)
				time.sleep(0.5)
				send_txt(theid, conclusion_text2)
				time.sleep(0.5)

				#send_txt(theid, conclusion_text3)











					


			