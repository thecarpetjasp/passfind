#!/usr/bin/env python3
import json
import requests
import colorama
import os
import time
import platform
from colorama import Fore, Style

class color:
        BOLD = '\033[1m'
        END = '\033[0m'

# ENTER YOUR API KEY BELOW
API_KEY = ("")


os.system("cls||clear")
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
print ("\/_/    " + Fore.YELLOW + " /_/  /_/ |_/___/___/ /_/ /___/_/|_/____/ " + Style.RESET_ALL + "by " + Fore.YELLOW + color.BOLD + "thecarpetjasp" + Style.RESET_ALL + color.END)
skip_choice = 0
passcrack_start = 0
passfind_start = 0
passfind_down = 0
if passfind_down == 1:
        print ("\nPASSFIND is currently unavailable!\n")
        time.sleep(2)
        print ("Redirecting you to PASSCRACK instead...")
        time.sleep(1)
        countdown_int = 4
        for countdown in range(1, 4):
                countdown_int = (countdown_int - 1)
                if countdown_int == 3:
                        print ("..." + str(countdown_int))
                        time.sleep(1)
                else:
                        print ("..." + str(countdown_int))
                        time.sleep(1)
        passcrack_start = 1
        skip_choice = 1
if API_KEY == ("") and passfind_down == 0:
        print ("\nLooks like you don't have an API key!\n")
        time.sleep(2)
        print ("Redirecting you to PASSCRACK instead...")
        time.sleep(1)
        countdown_int = 4
        for countdown in range(1, 4):
                countdown_int = (countdown_int - 1)
                if countdown_int == 3:
                        print ("..." + str(countdown_int))
                        time.sleep(1)
                else:
                        print ("..." + str(countdown_int))
                        time.sleep(1)
        passcrack_start = 1
        skip_choice = 1
if skip_choice == 0:
        print ("\nSelect a service to use:\n")
        print (Fore.RED + "[" + Fore.YELLOW + "1" + Fore.RED + "] " + Style.RESET_ALL + "PASSFIND")
        print (Fore.RED + "[" + Fore.YELLOW + "2" + Fore.RED + "] " + Style.RESET_ALL + "PASSCRACK\n")
        service_choice = input("Choose by number: ")
        if service_choice == ("1"):
                passfind_start = 1
        elif service_choice == ("2"):
                passcrack_start = 1
        else:
                os.system("cls||clear")
                print (Fore.RED + "INVALID OPTION. RESTART PROGRAM." + Style.RESET_ALL)
if passfind_start == 1:
        os.system("cls||clear")
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
        print ("\/_/    " + Fore.YELLOW + " /_/  /_/ |_/___/___/ /_/ /___/_/|_/____/ " + Style.RESET_ALL + "by " + Fore.YELLOW + color.BOLD + "thecarpetjasp" + Style.RESET_ALL + color.END)
        term = input("\nEnter email address: ")
        print ("\nRetrieving information...")
        func = ("auto")

        url = "https://breachdirectory.p.rapidapi.com/"

        querystring = {"func":func,"term":term}

        headers = {
            'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
            'x-rapidapi-key': API_KEY
            }


        response = requests.request("GET", url, headers=headers, params=querystring)

        todos = json.loads(response.text)
        check_for_credit = (len(todos))
        if check_for_credit == 1:
                print ("\n\nYou have exceeded the MONTHLY quota for Requests on your current plan, BASIC. Upgrade your plan at " + Fore.YELLOW + "https://rapidapi.com/rohan-patra/api/breachdirectory\n\n" + Style.RESET_ALL)
                time.sleep(2)
                print ("Redirecting you to PASSCRACK instead...")
                time.sleep(3)
                countdown_int = 4
                for countdown in range(1, 4):
                        countdown_int = (countdown_int - 1)
                        if countdown_int == 3:
                                print ("..." + str(countdown_int))
                                time.sleep(1)
                        else:
                                print ("..." + str(countdown_int))
                                time.sleep(1)
                passcrack_start = 1
                monthly_limit = 1
        if check_for_credit != 1:
                counter = 0
                try:
                        for passwords in range(0, len(todos['result'])):
                                print(Fore.BLUE + "\n[", Fore.YELLOW + str(passwords + 1), Fore.BLUE + "]", sep="", end=" ")
                                print(Fore.BLUE + "     password:", Fore.WHITE + todos['result'][passwords]['password'])
                                print(Fore.RED + "        hash:", Fore.WHITE + todos['result'][passwords]['hash'])
                                print(Fore.YELLOW + "        sources:", Fore.WHITE, todos['result'][passwords]['sources'], Style.RESET_ALL)


                        print("\n\nFetching uncensored passwords...")

                        if func == ("auto"):
                                todos = json.loads(response.text)
                                for a in range(0, len(todos['result'])):
                                        hash_list = []
                                        hash = (todos['result'][a]['hash'])
                                        querystring = {"func":"dehash","term":hash}
                                        headers = {
                                                'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
                                                'x-rapidapi-key': API_KEY
                                                }
                                        response = requests.request("GET", url, headers=headers, params=querystring)
                                        #print(response.text)
                                        todos1 = json.loads(response.text)
                                        time.sleep(2)
                                        print(Fore.BLUE + "\n[", Fore.YELLOW + str(a + 1), Fore.BLUE + "]", Style.RESET_ALL, sep="", end=" ")
                                        print(todos1['found'])
                except KeyError:
                        print (Fore.RED + "\n\nNO RESULTS!" + Style.RESET_ALL)
if passcrack_start == 1:
        def split(word):
                return [char for char in word]
        osystem = (platform.system())
        if osystem == ("Windows"):
                print ("\nOops! We're sorry, but PASSCRACK is only available for Linux users right now! :(")
                exit()
        while True:
                os.system("cls||clear")
                print ("Welcome to PASSCRACK!\n\n")
                print ("Please visit " + Fore.YELLOW + "breachdirectory.org " + Style.RESET_ALL + "and input the email address to get all censored passwords and their hashes.")
                print ("Copy and paste " + Fore.GREEN + "1 " + Style.RESET_ALL + "censored password and it's designated SHA-1 hash below to crack.\n\n\n\n\n\n\n\n\n\n")
                known_char_input1 = input("Input the censored password: ")
                known_char_input = known_char_input1.replace("	", "")
                known_char_list = (split(known_char_input))
                star_count = 0
                known_char = ("")
                for z in range(0, len(known_char_list)):
                        if known_char_list[z] == ("*"):
                                star_count = (star_count + 1)
                        elif known_char_list[z] != ("*"):
                                known_char = (known_char + known_char_list[z])
                if star_count > 4:
                        os.system("cls||clear")
                        if star_count == 5:
                                pass_storage = ("12 GB.")
                        elif star_count == 6:
                                pass_storage = ("923 GB.")
                        elif star_count == 7:
                                pass_storage = ("66046 GB / 64 TB.")
                        elif star_count == 8:
                                pass_storage = ("4694395 GB / 4584 TB.")
                        elif star_count > 8:
                                pass_storage = ("DANGEROUS. Higher than 4 PB!!!")
                        print ("THERE ARE TOO MANY UNKNOWN CHARACTERS!\n\n")
                        print ("Please visit " + Fore.YELLOW + "weleakinfo.to" + Style.RESET_ALL + " to find more known characters for the password.")
                        print (Fore.YELLOW + "weleakinfo.to" + Style.RESET_ALL + " will only censor the last 4 characters, revealing more characters.\n")
                        print ("*ALL CENSORED PASSWORDS WILL BE IN THE SAME ORDER AS BREACHDIRECTORY*")
                        print ("*PLEASE CONTINUE TO USE SHA-1 HASH FROM BREACHDIRECTORY*\n\n")
                        print ("You can continue, but only at your own risk!")
                        print ("By agreeing to continue, you acknowledge this job could take an extreme length of")
                        print ("time to complete and will take up a lot of disk space on your PC in order to create")
                        print ("password dictionary's in the attempt to crack the password.\n\n")
                        print ("THE CURRENT SIZE FOR THE DICTIONARY YOU ARE ABOUT TO CREATE IS: " + color.BOLD + pass_storage + Style.RESET_ALL + "\n\n")
                        print ("Would you like to continue or re-enter a shorter version of the censored password?\n")
                        print ("[1] Go back")
                        print ("[2] Continue\n")
                        user_choice = input("Choose by number: ")
                        if user_choice == ("2"):
                                os.system("cls||clear")
                                print ("Are you sure? [y/n]\n")
                                answer = input("answer: ")
                                if answer == ("y"):
                                        os.system("cls||clear")
                                        break
                                elif answer != ("y") or answer != ("n"):
                                        print ("INVALID ANSWER\n")
                        elif user_choice != ("1") and user_choice != ("2"):
                                print ("INVALID CHOICE\n")
                elif star_count == 4 or star_count < 4:
                        print ("\n")
                        break
        pass_hash_input = input("Input the SHA-1 hash: ")
        pass_hash = pass_hash_input.replace(" ", "")
        with open("hash", "w") as hash_file:
                hash_file.writelines(pass_hash)

        cracked_check = os.popen("grep " + pass_hash + " ~/.john/john.pot").read()
        if cracked_check != (""):
                os.system("cls||clear")
                print ("You have previously cracked this password.\n\n")
                final = cracked_check.replace(("$dynamic_26$" + pass_hash + ":"), "")
                print ("PASSWORD FOUND: " + color.BOLD + final + Style.RESET_ALL)
                exit()

        crunch_input = str(known_char)
        for at in range(0, star_count):
                crunch_input = (crunch_input + "@")
        crunch_command = ("crunch " + str(len(known_char_list)) + " " + str(len(known_char_list)) + " abcdefghijklmnopqrstuvwxyz1234567890,.!' 'ABCDEFGHIJKLMNOPQRSTUVWXYZ -t " + crunch_input + " -o pass > /dev/null 2>&1")
        create = 0
        cracking = 0
        end = 0
        while end == 0:
                os.system("cls||clear")
                print ("CRACKING THE PASSWORD!\n")
                print (Fore.RED + color.BOLD + "Do NOT close the program! Please be patient.\n\n" + Style.RESET_ALL)
                if create == 0:
                        time.sleep(2)
                if create == 0:
                        create = 1
                        print (Fore.YELLOW + "Creating a password dictionary..." + Style.RESET_ALL)
                        os.system(crunch_command)
                elif create == 1:
                        cracking = (cracking + 1)
                        print (Fore.GREEN + "Password dictionary successfully created!\n" + Style.RESET_ALL)
                        if cracking == 1:
                                time.sleep(1)
                                print (Fore.YELLOW + "Cracking the password..." + Style.RESET_ALL)
                                os.system("john hash --format=raw-sha1 --wordlist=pass > grep.txt 2>&1")
                                grepped = os.popen("grep '(?)' grep.txt").read()
                                final = grepped.replace("(?)", "")
                                if final != (""):
                                        result = 1
                                else:
                                        result = 0
                        elif cracking == 2:
                                if result == 1:
                                        print (Fore.GREEN + "Password sucessfully cracked!\n\n" + Style.RESET_ALL)
                                        print ("PASSWORD FOUND: " + color.BOLD + final + Style.RESET_ALL)
                                        end = 1
                                elif result == 0:
                                        print (Fore.RED + "Password could not be cracked!" + Style.RESET_ALL + "\n\nCreating a stronger dictionary with 100% guarantee.")
                                        print ("\n*These dictionaries take up a lot more storage. Precise Storage capacity will be displayed.*")
                                        to_continue = input("\nPress enter to continue...")
                                        end = 2
                                        create = 0
                                        cracking = 0
                                        crunch_command = ("crunch " + str(len(known_char_list)) + " " + str(len(known_char_list)) + " \"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',''.'' ''/''\\\\''|''<''>''?'';''#'':''~'\\\"'\\\"'@''['']''{''}''=''-''+''_'')''(''*''&''^''%''$''£''\\\"''!'\" -t " + crunch_input + " -o pass | python -c 'import os; from colorama import Fore, Style; os.system(\"clear\"); print (\"CRACKING THE PASSWORD!\"); print(\"\"); print (Fore.RED + \"Do NOT close the program! Please be patient.\" + Style.RESET_ALL); print(\"\"); print(\"\"); print (Fore.YELLOW + \"Creating a password dictionary...\" + Style.RESET_ALL); print (\"Press Enter to continue...\")'")
                                        while end == 2:
                                                os.system("cls||clear")
                                                print ("CRACKING THE PASSWORD!\n")
                                                print (Fore.RED + color.BOLD + "Do NOT close the program! Please be patient.\n\n" + Style.RESET_ALL)
                                                if create == 0:
                                                        time.sleep(2)
                                                if create == 0:
                                                        create = 1
                                                        print (Fore.YELLOW + "Creating a password dictionary..." + Style.RESET_ALL)
                                                        os.system(crunch_command)
                                                elif create == 1: 
                                                        cracking = (cracking + 1)
                                                        print (Fore.GREEN + "Password dictionary successfully created!\n" + Style.RESET_ALL)
                                                        if cracking == 1:
                                                                time.sleep(1)
                                                                print (Fore.YELLOW + "Cracking the password..." + Style.RESET_ALL)
                                                                os.system("john hash --format=raw-sha1 --wordlist=pass > grep.txt 2>&1")
                                                                grepped = os.popen("grep '(?)' grep.txt").read()
                                                                final = grepped.replace("(?)", "")
                                                                if final != (""):
                                                                        result = 1
                                                                else:
                                                                        result = 0
                                                        elif cracking == 2:
                                                                if result == 1:
                                                                        print (Fore.GREEN + "Password sucessfully cracked!\n\n" + Style.RESET_ALL)
                                                                        print ("PASSWORD FOUND: " + color.BOLD + final + Style.RESET_ALL)
                                                                        end = 1
                                                                elif result == 0:
                                                                        print (Fore.RED + "Password could not be cracked!" + Style.RESET_ALL)
                                                                        end = 1
        os.system("rm grep.txt & rm hash & rm pass")
