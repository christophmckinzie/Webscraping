# Raspberry Pi Webscraping

## Setting Up A Raspberry Pi
This guide is how I chose to set up my Pi with Raspberry Pi OS, Wi-Fi, SSH, VNC Viewer, MariaDB, etc. My goal was to get familiar with a Pi and shell scripting with Linux. 


1. [Flashing Operating System](#Flashing-OS)
2. [First Time Login](#First-Login)
3. [Remote Access - VNC](#Remote-Access-With-VNC)
4. [SSH](#SSH)
5. [Updating OS](#Updating-The-Pi-OS)

----------------------------------------------------------------

# Flashing-OS
Firstly, you need to download the image file of the operating system. I am using [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/). This file is an image file which needs to be written onto a SD card.

To do this you can use [Balenaetcher](https://www.balena.io/etcher/) or Win32DiskImager. You need to be VERY careful about choosing the right drive to flash the image file to. Choosing your PCs local disk will delete everything and put the OS on it. 

----------------------------------------------------------------

# First-Login
The newer OS versions have SSH and and VNC disabled by default for security reasons. There are methods to enable it where you place an empty file named ssh (no extension) in the root of the boot disk, but I chose to plug into a montinor and keyboard for the first login to enable these. The default hostname, username and password are:

```
default hostname: raspberrypi
default username: pi
default password: raspberry
```

Once you are logged in open the terminal and change the password using the `passwd` command. 

Under Preferences open Raspberry Pi Configuration and enable SSH and VNC (you can open with `raspi-config`). It is also recommened that you disable Auto Login Under User 'Pi'.

Connect to the internet by either hardwiring or with Wi-Fi. The Wi-Fi settings are found in the top right.  

To download [VNC Viewer](https://www.realvnc.com/en/) use the terminal command `sudo apt-get install realvnc-vnc-viewer`. Open VNC in the top right and note your ip address. You can also use the command `ifconfig -a` to get the ip address.

----------------------------------------------------------------

# Remote-Access-With-VNC
Now that VNC is installed on the Pi, download it onto your desktop/laptop/whatever device you want to use to connect to the Pi. Open the program and make a new connection to your Pi using its ip address. 

Connecting to a Pi this way is called head melted or headless and can often have resolution issues. The best results I could get were by directly editing the /boot/config.txt file. To do this open the terminal and run the command `sudo nano /boot/config.txt`. The following are what I edited:

* `frame_buffer_width=1920` 
* `frame_buffer_height=1080`
* Uncommented `hdmi_force_hotplug=1` which is important if you are running the Pi head melted. 
* Comment out `hdmi_group`, `hdmi_mode` and `hdmi_ignore_edid`

Click `ctrl-x` and then click `y` to save changes. Reboot the Pi. 

----------------------------------------------------------------

# SSH
Another method is connecting to your Pi is by using SSH (terminal), which now comes with Windows 10. The command to connect to the Pi from your Windows desktop is `ssh pi@raspberrypi.local` if you are using the default username and hostname as mentioned above. You may also use the IP address of the Pi as follows: `ssh pi@IP_ADDRESS`. Exit the SSH terminal using the `exit` command. 

----------------------------------------------------------------

# Updating-The-Pi-OS
To make sure everything is up to date run.

```
sudo apt-get update -y
sudo apt-get upgrade -y
```

At this point its ready for whatever you wanna do with it. The Web Scraping folder README has the steps to install a MySQL server and packages to do some webscraping with Python. 

