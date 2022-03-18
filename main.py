from telethon.sync import TelegramClient
import os
artt = """
     ▄         ▄▄▄▄▄   ▄█▄    █▄▄▄▄ ██   █ ▄▄  \033[37m1.0\033[35m
 ▀▄   █       █     ▀▄ █▀ ▀▄  █  ▄▀ █ █  █   █ 
   █ ▀  \033[37m▄▄▄\033[35m    ▀▀▀▀▄   █   ▀  █▀▀▌  █▄▄█ █▀▀▀  
  ▄ █        ▀▄▄▄▄▀    █▄  ▄▀ █  █  █  █ █     
 █   ▀▄                ▀███▀    █      █  █  \033[37m[\033[35m+\033[37m] By \033[37m@Pablox_xd\033[35m
  ▀                            ▀      █    ▀    [\033[37m+\033[35m] Special thanks \033[35m@Netro3
                                    ▀         
"""
os.system('clear || cls')
print ("\033[35m" + artt)

try:
    apiss = open('api.txt','r')
    apis = apiss.readlines()
except:
    apiss = open('api.txt','w')
    apiss.close()
    apiss = open('api.txt','r')
    apis = apiss.readlines()

if apis == []:
    api_id = int(input("\033[35mApi\033[37mId: \033[35m"))
    api_hash = input("\033[35mApi\033[37mHash: \033[35m")
    api_id = int(str(api_id).replace(' ',''))
    api_hash = api_hash.replace(' ','')
    apiss = open('api.txt', 'w')
    apiss.write(str(api_id))
    apiss.write('\n')
    apiss.write(api_hash)
    apiss = apiss.close()
    ewdewde = input("\n\033[35mPress enter to \033[37mcontinue\033[35m.")
    os.system('clear || cls')    
elif len(apis) == 2:
    api_id = int(apis[0])
    api_hash = apis[1]
    print ("\033[35mApi\033[37mId: " + "\033[35m" + str(api_id))
    print ("\033[35mApi\033[37mHash: " + "\033[35m" + api_hash) 
    print("\n\033[35mIf you want to change your \033[37mapi\033[35m delete '\033[37mapi.txt\033[35m'.")
    sdwed = input("\033[37mPress enter to \033[35mcontinue\033[37m.")
    os.system('clear || cls')
    

username = 'XScrap'
lst = ["0","1","2","3","4","5","6","7","8","9","|","\n"]
ccp = []
cnter = 0
clorr1 = "\033[35m"
clorr2 = "\033[37m"
clord = 0

os.system('rm XScrap.session || del XScrap.session')
os.system('clear || cls')
chanil = input('\033[37mChannel\033[35m/\033[37mGroup\033[37m:\033[35m')
chanil = chanil.replace('@','')
with TelegramClient(username, api_id, api_hash) as client:
    os.system('clear || cls')
    print(clorr2 + "Scraping" + clorr1 + " Started...")
    for message in client.iter_messages(chanil):
        msg = str(message.text)
        msgln = len(msg)
        rr = 0
        cc = ""
        lstc = []
        while rr != msgln:
            if msg[rr] in lst:
                if msg[rr] == lst[0]:
                    cc = cc + lst[0]
                elif msg[rr] == lst[1]:
                    cc = cc + lst[1]
                elif msg[rr] == lst[2]:
                    cc = cc + lst[2]
                elif msg[rr] == lst[3]:
                    cc = cc + lst[3]
                elif msg[rr] == lst[4]:
                    cc = cc + lst[4]
                elif msg[rr] == lst[5]:
                    cc = cc + lst[5]
                elif msg[rr] == lst[6]:
                    cc = cc + lst[6]
                elif msg[rr] == lst[7]:
                    cc = cc + lst[7]
                elif msg[rr] == lst[8]:
                    cc = cc + lst[8]
                elif msg[rr] == lst[9]:
                    cc = cc + lst[9]
                elif msg[rr] == lst[10]:
                    cc = cc + lst[10]
                elif msg[rr] == lst[11]:
                    cc = cc + lst[11]
                rr = rr + 1
            else:
                rr = rr + 1
        neme = 'Scraped/%s_Scrapped.txt'% chanil
        texti = open(neme, 'a')
        #default
        if "|" in cc:
            cc = cc.split('\n')
            ccln = len(cc)
            ccl = 0
            while ccl != ccln:
                if len(cc[ccl]) == 28 and "|" not in str(cc[ccl])[0:14] and "|" not in str(cc[ccl])[26:28] :
                    if cc[ccl] not in ccp:
                        ccp.append(cc[ccl])
                        texti.write(cc[ccl])
                        texti.write('\n')
                        texti.close
                        cnter = cnter + 1
                        if clord == 0:
                            clord = 1
                            print(clorr1 + str(cnter) + clorr2 + "|" + clorr1 + chanil + clorr2 + "|" + clorr1 + "X-Scrap" + clorr2 + "|" + clorr1 + "Pablox_xd" + clorr2 + "|" + clorr1 + "Netro3")
                        elif clord == 1:
                            clord = 0
                            print(clorr2 + str(cnter) + clorr1 + "|" + clorr1 + chanil + clorr2 + "|" + clorr2 + "X-Scrap" + clorr1 + "|" + clorr2 + "Pablox_xd" + clorr1 + "|" + clorr2 + "Netro3")

                        else:
                            pass
                     
                ccl = ccl + 1
        elif len(cc) < 15:
            pass

        #ccnum
        elif cc[0:15].isdigit and cc[0] == "4" or "3" or "5" or "6" and cc.split('\n')[1].isdigit and cc.split('\n')[2].isdigit:
            try:
                cc = cc.split('\n')
                nrte = cc[2]
                nrta = cc[3]
                if nrte[0] == "2" or nrte[0] == "3" and len(nrte) == 2:
                    yyyy = "20" + nrte
                elif nrta[0] == "2" or nrta[0] == "3" and len(nrta) == 2:
                    yyyy = "20" + nrta
                if len(cc[2]) == 2 and str(cc[2])[0] != "2":
                    mm = cc[2]
                elif len(cc[3]) == 2 and str(cc[3])[0] != "2":
                    mm = cc[3]
                ccer = cc[0] + "|" + mm + "|" + yyyy + "|" + cc[1]
                if ccer not in ccp and len(ccer) == 28:
                    ccp.append(ccer)
                    texti.write(ccer)
                    texti.write('\n')
                    texti.close
                    cnter = cnter + 1
                    if clord == 0:
                        clord = 1
                        print(clorr1 + str(cnter) + clorr2 + "|" + clorr1 + chanil + clorr2 + "|" + clorr1 + "X-Scrap" + clorr2 + "|" + clorr1 + "Pablox_xd" + clorr2 + "|" + clorr1 + "Netro3")
                    elif clord == 1:
                        clord = 0
                        print(clorr2 + str(cnter) + clorr1 + "|" + clorr1 + chanil + clorr2 + "|" + clorr2 + "X-Scrap" + clorr1 + "|" + clorr2 + "Pablox_xd" + clorr1 + "|" + clorr2 + "Netro3")
                    else:
                        pass
            except:
                pass
        else:
            pass

