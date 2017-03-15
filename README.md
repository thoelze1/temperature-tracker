# Track Temperature
Using arduino and raspberry pi.

# Old tutorial
http://renatoppl.com/blog/2014/03/03/thermometer-using-arduino-and-raspberrypi/

# SSH into Pi with Ubuntu and ethernet cable
http://raspberrypi.stackexchange.com/questions/3867/ssh-to-rpi-without-a-network-connection

# Connect to WiFi
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

# Connect to WiFi on boot
http://raspberrypi.stackexchange.com/questions/13558/how-to-get-wi-fi-to-connect-on-boot

# Stay connected to WiFi
Enable roaming: http://raspberrypi.stackexchange.com/questions/27475/wifi-disconnects-after-period-of-time-on-raspberry-pi-doesnt-reconnect
Turn power saver off: https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=139407&p=924859
What I did:
	Followed raspberry pi website
	Enabled at boot
	Enabled roaming
	Turned power saver off

# Recent Pi models
http://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip-address/37921#37921

# Arduino from command line: official software
Man: https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc
Download:
Add to PATH: http://osxdaily.com/2014/08/14/add-new-path-to-path-command-line/
Verify and upload:
$ /Applications/Arduino.app/Contents/MacOS/Arduino --upload sketch.ino --port /dev/tty.usbmodemXXXXX)
View serial port: https://www.baldengineer.com/alternatives-to-arduinos-serial-monitor.html
$ screen /dev/tty.usb.modemXXXXX 9600

