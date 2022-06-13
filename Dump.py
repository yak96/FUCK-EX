
import platform
import os
os.system('termux-setup-storage')


arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Jm")._login()
elif 'aarch' in arc:
	__import__("Dump")._login()
else:
	exit(f' Unknow device machine {arc}')
logo = ("""\033[1;32m
       
┌───────────────────────────────────────────────────────────┐
│                                                           │
│   █████╗ ██╗      █████╗ ███╗   ███╗ ██████╗ ██╗██████╗   │
│  ██╔══██╗██║     ██╔══██╗████╗ ████║██╔════╝ ██║██╔══██╗  │
│  ███████║██║     ███████║██╔████╔██║██║  ███╗██║██████╔╝  │
│  ██╔══██║██║     ██╔══██║██║╚██╔╝██║██║   ██║██║██╔══██╗  │
│  ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║██║  ██║  │
│  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝  │
│                                            │
└───────────────────────────────────────────────────────────┘  \033
__________________×______________________
  
  Auther   :  MD ALAMGIR HOSEN
 
  Github   :  THE DARK WORLD TEAM-CYBER ARMY&RECOVERY ZONE 
  Facebook : https://www.facebook.com/TeraPaPa.ALAMgir.HoSeN ⭐⭐⭐⭐
  
  Contact : Whatsapp+8801712034653 
__________________×______________________\033[1;37m""")
