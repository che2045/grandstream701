# Python 2.7 config uploader for Grandstream HT701 ATA

In case you have ATA at a remote site with no access to your TFTP service (ACS), instead of configuring the device from scratch I've written this Python script to load configuration to the device.

# Preparing the config file

- First you need to save template for future configurations, by accessing web interface and downloading configuration (config.txt) to your local PC.

- Then you need to prepare the file for the script by issuing this Linux terminal command (or if you are on Windows you can user any text editor that support regular expression - you need to replace "P" at the beginning of every line with "set " and first "=" in every line with " "):

		sed -e 's/^P/set /' -e '0,//s/\=/ /' ht701.txt > commands.list
	
# Hosts list

- This file contains IP addresses of devices you want to configure via the script
