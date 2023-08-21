#Nice little script to connect to the internet on a minimal Gentoo system, with dhcpcd and wpa_supplicant.
#I wrote this specifically for my laptop, but should work on other computers.
#ALSO! Pretty please ignore the fact that I used os. I just wanted to use it for *insert reason*. If you want to, you can fork this and use subprocess instead
#NOTE: The constant sleeping is to ensure that dhcpcd and wpa_supplicant actually has time to register what you are doing and not cause a delay in connectivity

#Dependancies/Creating variables:

import time
import os
import getpass
SSID = ""

print("Hi! So, you'd like to connect to the internet? Well of course! Just go ahead and type in the SSID and Password!")
print("NOTE: This assumes you are on a WPA/WPA2 connection by dhcpcd's defaults")
print("")
print("SSID:")
SSID = input("")
print("")
print("Password:")
Password = getpass.getpass(prompt="")

time.sleep(3)

os.system(f"wpa_supplicant -B -i wlp0s20f3 -c <(wpa_passphrase '{SSID}' '{Password}')")
print("You have been connected to your router")
time.sleep(3)
os.system("dhcpcd")
os.system("echo nameserver 8.8.8.8 > /etc/resolv.conf")
print("Initializing...")
time.sleep(10)
print("You have been successfully connected to the internet!")
