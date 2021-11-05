#!/usr/bin/env python3
import json
import requests
import colorama
import os
import time
from colorama import Fore, Style

class color:
	BOLD = '\033[1m'
	END = '033[0m'

# ENTER YOUR API KEY BELOW
API_KEY = ("")


os.system("cls|clear")
print ("            ______")              
print ("         .-'      `-.")           
print ("       .'            `.")         
print ("      /                \ ")       
print ("     ;                 ;;  ")     
print ("     |    PASS FIND    |;   ")   
print ("     ;                 ;|")
print ("     '\               / ;  ")     
print ("      \`.           .' /  ")      
print ("       `.`-._____.-' .'  ")       
print ("         / /`_____.-'  ")         
print ("        / / /    ")               
print ("       / / /")
print ("      / / /")
print ("     / / /")
print ("    / / /")
print ("   / / /")
print ("  / / / " + Fore.YELLOW + "    ___  ___   ________  _________  _____" + Style.RESET_ALL)
print (" / / /  " + Fore.YELLOW + "   / _ \\/ _ | / __/ __/ / __/  _/ |/ / _ \\" + Style.RESET_ALL)
print ("/ / /   " + Fore.YELLOW + "  / ___/ __ |_\\ \\_\\ \\  / _/_/ //    / // /" + Style.RESET_ALL)
print ("\/_/    " + Fore.YELLOW + " /_/  /_/ |_/___/___/ /_/ /___/_/|_/____/ " + Style.RESET_ALL)

url = "https://breachdirectory.p.rapidapi.com/"

email_input = input("\nEnter email address: ")
print ("\nRetrieving information...")

querystring = {"func":"auto","term":email_input}

headers = {
    'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

todos = json.loads(response.text)

check_for_credit = (len(todos))
if check_for_credit == 1:
	print ("\n\nYou have exceeded the MONTHLY quota for Requests on your current plan, BASIC. Upgrade your plan at https:\\/\\/rapidapi.com\\/rohan-patra\\/api\\/breachdirectory}")
	exit()

counter = 0
try:
	for a in range(0, (len(todos['result']))):
		if counter == 0:
			print("\n\nFOUND PASSWORDS:")
			counter = 1
		found_password1 = (todos['result'][a]['has_password'])
		found_password = json.dumps(found_password1)
		if found_password == ("true"):
			print (Fore.RED + "\n[", Fore.YELLOW, (a + 1), Fore.RED + "]", sep="", end=" ")
			print (Style.RESET_ALL + color.BOLD + todos['result'][a]['password'], Style.RESET_ALL)
		else:
			print (Fore.RED + "\n[", Fore.YELLOW, (a + 1), Fore.RED + "]", sep="", end=" ")
			print (Style.RESET_ALL + "N/A")
	print("\n\nSOURCES:")
	for b in range(0, (len(todos['result']))):
		print (Fore.RED + "\n[", Fore.YELLOW, (b + 1), Fore.RED + "]", sep="", end=" ")
		print (Style.RESET_ALL, todos['result'][b]['sources'])
	print("\n\nSHA1 HASHES:")
	for c in range(0, (len(todos['result']))):
		found_password1 = (todos['result'][c]['has_password'])
		found_password = json.dumps(found_password1)
		if found_password == ("true"):
			print (Fore.RED + "\n[", Fore.YELLOW, (c + 1), Fore.RED + "]", sep="", end=" ")
			print (Style.RESET_ALL, todos['result'][c]['sha1'])
		else:
			print (Fore.RED + "\n[", Fore.YELLOW, (c + 1), Fore.RED + "]", sep="", end=" ")
			print (Style.RESET_ALL + "N/A")
except KeyError:
	print (Fore.RED + "\n\nNO RESULTS!" + Style.RESET_ALL)
