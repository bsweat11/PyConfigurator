import os
import time
from tqdm import tqdm
import colorama
from colorama import Fore

DirectoryRTR = r'C:/Routers/'
DirectorySW = r'C:/Switches/'
if not os.path.exists(DirectoryRTR):
    os.makedirs(DirectoryRTR)
if not os.path.exists(DirectorySW):
    os.makedirs(DirectorySW)


print(" © 2022 Brandon Sweat • Author\n All Rights Reserved • Copyright Configurator v1.93\n    "
      "Distribution of this program is not allowed unless\n    explicitly stated by the Author named herein. Use of\n    this program is done so at the risk of the user.\n")
print(" ")
print(" ")
print(Fore.GREEN + "          _.-;;-._                                                              ")
print("   '-..-'|   ||   |   ____             __ _                       _             ")
print("   '-..-'|_.-;;-._|  / ___|___  _ __  / _(_) __ _ _   _ _ __ __ _| |_ ___  _ __ ")
print("   '-..-'|   ||   | | |   / _ \| '_ \| |_| |/ _` | | | | '__/ _` | __/ _ \| '__|")
print("   '-..-'|_.-''-._| | |__| (_) | | | |  _| | (_| | |_| | | | (_| | || (_) | |")
print("                     \____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__\___/|_|")
print("                                             |___/                              ")
print(Fore.WHITE + "\n")
print("               #################################################")
print("               *                    Models:                    *")
print("               * --------------------------------------------- *")
print("               *|" + Fore.YELLOW + " SRX320      SRX210       EX2300      EX2200" + Fore.WHITE + " |*")
print("               * --------------------------------------------- *")
print("               #################################################")
print("\n")

print('\n')

DEV1 = input("     Device Type?   ")

print("\n")

RTR_SW = ('EX2200', 'EX2300', 'SRX210', 'SRX320')
SW = ('EX2200', 'EX2300')

if DEV1 in RTR_SW:
    Subnet = input(" Subnet (Input the 3rd & 4th octet, in xx.yy format e.g. 0.125)..........:      ")
    Hostname = input(" Hostname (Input the entire location of the device e.g. HQ-02)...:      ")

if DEV1 not in SW:
    VPN = input(" VPN (Input the 4th octet VPN IP e.g. 42)................................:      ")
    VPNHost = input(" VPN Hostname............................................................:      ")
    PCI = input(" Is this a PCI network? [Y/n]............................................:      ")


Activate20 = 'activate DHCP server'


##############################################################################
##############################################################################
##############################################################################
##############################################################################
#                       Config for SRX320 secondfile
if DEV1 == "SRX320" and PCI in ["y", "Y", "yes", "YES"]:
    with open('C:\Program Files\Configurator\Templates\SRX320.txt', 'r') as firstfile, open(f'C:/Routers/{Hostname}' + '_320_R2.txt', 'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)
    with open(f'C:/Routers/{Hostname}' + '_320_R2.txt', 'r+') as secondfile:
        filedata = secondfile.read()
        filedata = filedata.replace(':vpn', VPN)
        filedata = filedata.replace(':hostname', Hostname)
        filedata = filedata.replace(':headend', VPNHost)
        filedata = filedata.replace('xx.yy', Subnet)
        filedata = filedata.replace('DNS-CACHE-STATIC', Activate20)
    with open(f'C:/Routers/{Hostname}' + '_320_R2.txt', 'r+') as secondfile:
        secondfile.write(filedata)
elif DEV1 == "SRX320":
    with open('C:\Program Files\Configurator\Templates\SRX320.txt', 'r') as firstfile, open(f'C:/Routers/{Hostname}' + '_320.txt', 'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)
    with open(f'C:/Routers/{Hostname}' + '_320.txt', 'r+') as secondfile:
        filedata = secondfile.read()
        filedata = filedata.replace(':vpn', VPN)
        filedata = filedata.replace(':hostname', Hostname)
        filedata = filedata.replace(':headend', VPNHost)
        filedata = filedata.replace('xx.yy', Subnet)
        secondfile.write(filedata)
    with open(f'C:/Routers/{Hostname}' + '_320.txt', 'r+') as secondfile:
        secondfile.write(filedata)
        secondfile.close()

###Config for SRX210 thirdfile
if DEV1 == "SRX210" and PCI in ["y", "Y", "yes", "YES"]:
    with open('C:\Program Files\Configurator\Templates\SRX210.txt', 'r') as firstfile, open(f'C:/Routers/{Hostname}' + '_210_R2.txt', 'w') as secondfile: #Copies template to temp file
        for line in firstfile:
            secondfile.write(line)
    with open(f'C:/Routers/{Hostname}' + '_210_R2.txt', 'r+') as secondfile: #replaces variables in new temp file
        filedata = secondfile.read()
        filedata = filedata.replace(':vpn', VPN)
        filedata = filedata.replace(':hostname', Hostname)
        filedata = filedata.replace(':headend', VPNHost)
        filedata = filedata.replace('xx.yy', Subnet)
        filedata = filedata.replace('DNS-CACHE-STATIC', Activate20)
    with open(f'C:/Routers/{Hostname}' + '_210_R2.txt', 'r+') as secondfile:  #writes temp file
        secondfile.write(filedata)
elif DEV1 == "SRX210":
    with open('C:\Program Files\Configurator\Templates\SRX210.txt', 'r') as firstfile, open(f'C:/Routers/{Hostname}' + '_210.txt', 'w') as secondfile: #Copies template to temp file
        for line in firstfile:
            secondfile.write(line)
        secondfile.close()
        firstfile.close()
    with open(f'C:/Routers/{Hostname}' + '_210.txt', 'r+') as secondfile: #replaces variables in new temp file
        filedata = secondfile.read()
        filedata = filedata.replace(':vpn', VPN)
        filedata = filedata.replace(':hostname', Hostname)
        filedata = filedata.replace(':headend', VPNHost)
        filedata = filedata.replace('xx.yy', Subnet)
    with open(f'C:/Routers/{Hostname}' + '_210.txt', 'r+') as secondfile:  # writes temp file
        secondfile.write(filedata)
###Config for EX2300 fourthfile
if DEV1 == "EX2300":
    with open('C:\Program Files\Configurator\Templates\EX2300.txt', 'r') as firstfile, open(f'C:/Switches/{Hostname}' + '_2300.txt', 'w') as secondfile:

        for line in firstfile:
            secondfile.write(line)
        secondfile.close()
        firstfile.close()
    with open(f'C:/Switches/{Hostname}' + '_2300.txt', 'r+') as secondfile:
        filedata = secondfile.read()
        filedata = filedata.replace(':hostname', Hostname)
        filedata = filedata.replace('xx.yy', Subnet)
    with open(f'C:/Switches/{Hostname}' + '_2300.txt', 'r+') as secondfile:
        secondfile.write(filedata)

###Config for EX2200 fifthfile
if DEV1 == "EX2200":
    with open('C:\Program Files\Configurator\Templates\EX2200.txt', 'r') as firstfile, open(f'C:/Switches/{Hostname}' + '_2200.txt', 'w') as secondfile:

        for line in firstfile:
            secondfile.write(line)
        secondfile.close()
        firstfile.close()
    with open(f'C:/Switches/{Hostname}' + '_2200.txt', 'r+') as secondfile:
        filedata = secondfile.read()
        filedata = filedata.replace(':hostname', Hostname)
        filedata = filedata.replace('xx.yy', Subnet)
    with open(f'C:/Switches/{Hostname}' + '_2200.txt', 'r+') as secondfile:
        secondfile.write(filedata)

print("\n")
print("    Hang on.. I'm working on it....")

for i in tqdm (range (100), desc="     Building", ascii=False, colour='#00c853'):
    time.sleep(.02)
    pass

time.sleep(1.5)

if DEV1 in ['SRX320', 'SRX210']:
    FOLDER = '\Routers'
else:
    FOLDER = '\Switches'

print("\n")
print("Your configuration was successfully created!\n " + Fore.BLUE + " • " + Fore.YELLOW + " Check C:" + FOLDER + " for configuration\n")
print(Fore.WHITE + '')
input("Press " + Fore.GREEN + "'enter'" + Fore.WHITE + " to exit...")
