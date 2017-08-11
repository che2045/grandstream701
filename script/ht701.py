#!usr/bin/python

import getpass
import sys
import telnetlib
import time
from array import *

nlines = 0
f = open("hosts.list","r")
default_password = "admin"
prompt = "CONFIG>"
wrong_login = "Permission denied, please try again"
command_01="config"
command_02="commit"
command_03="exit"

for line in f:
	
	if nlines > 0:
		print "\nWaiting 2s before logging in to the device...\n"
		time.sleep(2)
	
	nlines += 1
	log_date = time.strftime("%Y.%m.%d")
	log_time = time.strftime("%H:%M:%S")
	HOST = line.rstrip("\n")
	
	print "\r"
	print "Connecting to " + str(nlines) + ". host: " + HOST

	try: 
		tn = telnetlib.Telnet(HOST, port=23, timeout=5)

	except:
		print "Error connecting to the device. Log entry created.\n"
		with open("error.log","ab") as e:
			e.write(log_date + " " + log_time + " " + HOST + " Unable to connect to the device." + "\r\n")
			e.close()
		continue
	
	tn.read_until("Password:")
	tn.write(default_password + "\n")	
	
	login_fail, match, console_output = tn.expect([wrong_login, prompt], 10)
	
	if login_fail == 0:
		print "Error connecting to the device. Log entry created.\n"
		with open("error.log","ab") as e:
			e.write(log_date + " " + log_time + " " + HOST + " Wrong password." + "\r\n")
		#print console_output
		e.close()
		tn.close()
		continue
		
	elif login_fail == -1:

		client_telephone = raw_input("\nEnter customer's SIP account name: ")
		client_password = getpass.getpass(prompt="Enter customer's SIP account password: ", stream=None)

		tn.write(command_01.encode("UTF-8")+"\r\n")
		print "Successfully connected to host. Executing commands: \n"

		command_array = array('i', [3,35,36])

		for i in command_array:
			tn.read_until(prompt)
			time.sleep(.3)
			tn.write(("set " + str(i) + " " + client_telephone).encode("UTF-8")+"\r\n")
			print "set " + str(i) + " " + client_telephone + "\n"
		
		tn.read_until(prompt)
		time.sleep(.3)
		tn.write(("set 34 " + client_password).encode("UTF-8")+"\r\n")
		print "Client account password set.\n"
		
		device_password = getpass.getpass(prompt="Enter new device password: ", stream=None)
		tn.write(("set 2 " + device_password).encode("UTF-8")+"\r\n")
		print "New device password set.\n"

		k = open("commands.list","r")
		for line in k:
			command_from_file = line.rstrip("\n")
			tn.read_until(prompt)
			time.sleep(.3)
			tn.write(command_from_file.encode("UTF-8")+"\r\n")
			print command_from_file

		tn.write(command_02.encode("UTF-8")+"\r\n")
		print "\nWaiting 10s for ATA to apply changes.\n"
		time.sleep(10)

		tn.write(command_03.encode("UTF-8")+"\r\n")
		print "All commands are executed successfully.\n"
		
		k.close()
		tn.close()  
		
	else:
		print "Unknown error. Log entry created."
		with open("error.log","ab") as e:
			e.write(log_date + " " + log_time + " " + HOST + " Unknown error." + "\r\n")
		e.close()
		tn.close()

if nlines == 0:
	print "\nList of hosts is empty.\n"
else:
	print "\nEnd of the program.\n"
f.close()
quit()
