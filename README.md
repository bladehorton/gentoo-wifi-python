# gentoo-wifi-python
Python script for connecting to the internet on gentoo with dhcpcd and wpa_supplicant


This is a Python script I created for the purposes of easily connecting to any WiFi connection on my Gentoo partition. I only created this due to it being a GUI-less install, and NetworkManager not working too well for me personally.
I'm sure this would work on other distros, but I created it with mnimal Gentoo in mind.

In order for this to work, you will obviously need to emerge wpa_supplicant and dhcpcd and configure those to your liking.

I highly recommend adding an alias that runs this file to your bashrc (or whatever you use) so that you may run it with a simple command.
