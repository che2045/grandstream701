# Python 2.7 config uploader for Grandstream HT701 ATA

In case you have ATA at a remote site with no access to your TFTP service (ACS), instead of configuring the device from scratch I've written this Python script to load configuration to the device.

The main idea is that with this script you only need to enter new device password and SIP account username (number)/password. You can automate that to your liking if you don't mind having passwords written in text files.

## Preparing the config file

- First you need to save template for future configurations, by accessing web interface and downloading configuration (config.txt) to your local PC. Example file is included here, but you should create your own to fit your VoIP provider and locale settings.

- Then you need to prepare the file for the script by issuing this Linux terminal command (or if you are on Windows you can user any text editor that support regular expression - you need to replace "P" at the beginning of every line with "set " and first "=" in every line with " "):

		sed -e 's/^P/set /' -e '0,//s/\=/ /' config.txt > commands.list
	
## hosts.list

- This file contains IP addresses of devices you want to configure via the script

## How to run the script

Issue the command:

	python ht701.py

## Warning: since this is plain telnet script, use only secured connection to the device.
