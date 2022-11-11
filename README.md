# stickbug
Raw payload obfuscator for Hoaxshell by t3l3machus.

## Installation ##

git clone https://github.com/sternyx/stickbug <br />
cd stickbug <br />
sudo python3 requirements.py <br />

## Usage and Example ##
sudo python3 stickbug.py<br />

Add listener IP and the payload will be created. Copy the payload in Green onto your windows device. 
![Alt text](https://github.com/sternyx/stickbug/blob/main/Images/stickbug%20init.png)<br />
Enter the payload into powershell on the windows device. You should get a hanging powershell window.
![Alt text](https://github.com/sternyx/stickbug/blob/main/Images/windows%20init.png)<br />
Return back to stickbug and press enter to be directed into the hoaxshell tmux session. Type "exit" to fully remove the powershell window. 
![Alt text](https://github.com/sternyx/stickbug/blob/main/Images/hoaxshell%20tmux.png)

