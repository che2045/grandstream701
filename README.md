# Python 2.7 config uploader for Grandstream HT701 ATA

In case you have ATA at a remote site with no access to your TFTP service (ACS) you are left with no other option than to manualy set the device since it does not have config upload feature. Instead of configuring the device from scratch I've written this Python script to load previously saved configuration to the device.

The main idea is that you only need to enter SIP account username (number)/password with the rest of the options already set. You can automate this to your liking if you don't mind having passwords written in text files.

## Preparing the config file

- Create the template for future configurations by accessing ATA's web interface, change and apply all the options you need to be set, and download configuration (`config.txt`) to your local PC. Copy it to the same folder with the `ht701.py` and `hosts.list`, and the script will parse the file and make output `commands.list`.
- If you want to change the config, delete files `config.txt` and `commands.list`, and repeat the process from the beginning.

## hosts.list

- This file contains IP addresses of devices you want to configure via the script

## How to run the script
```
python ht701.py
```
### Warning: since this is plain telnet script, use only secured connection to the device.
