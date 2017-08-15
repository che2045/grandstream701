# Python 2.7 config uploader for Grandstream HT701 ATA

In case you have ATA at a remote site with no access to your TFTP service (ACS) you are left with no other option than to manualy set the device since it does not have config upload feature. Instead of configuring the device from scratch I've written this Python script to load previously saved configuration to the device.

The main idea is that you only enter new device password and SIP account username (number)/password with the rest of the options already set. You can automate this to your liking if you don't mind having passwords written in text files.

## Preparing the config file (you only need to do this once)

- First you need to create the template for future configurations by accessing ATA's web interface, change and apply all the options you need to be set, and download configuration (`config.txt`) to your local PC.

- Then you need to prepare the file for the script by issuing following Linux/MacOS terminal command, or if you are on Windows you can use any text editor that supports regular expressions, just replace "P" at the beginning of every line with "set " and first "=" in every line with " " and save the new file as `commands.list`:

	```sed -e 's/^P/set /' -e '0,//s/\=/ /' config.txt > commands.list```
	
## hosts.list

- This file contains IP addresses of devices you want to configure via the script

## How to run the script
```
python ht701.py
```
### Warning: since this is plain telnet script, use only secured connection to the device.
