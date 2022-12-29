import requests, sys, os, platform

if(len(sys.argv) < 3):
    print("missing parameter")
    exit()

try:
    site = sys.argv[1]
    requestss = int(sys.argv[2])
except ValueError:
    print("Error. requests must be numeric")
    exit()

def banner():
    print('''                                                                                
                                                                                
                     /(/(                                                       
                     /%((                                                       
                     /%((                                                       
                     (%%(                                                       
                     (%%(                                                       
                     (%,(                                                       
                     (%,/                                                       
                     (%./                                                       
                     (%./                                                       
                     /%./                                                       
                     /%.*                                                       
                     /%.*                                                       
                     *%,*                                                       
                     *%,,                                                       
                     *%,,                              ,                        
                     *%,,                              /                        
                     *%,.                              /*                       
                     *%..                             ///,                      
                     *%,.                             ((*.                      
                     /%,.                             . #%,                     
                     /%//                               #%%/                    
                     (%%(                                #%.                    
                      /%,                                #%%                    
                      *%%(                               /%#                    
                       /%%(                             (#%/                    
                         %%*(                         ./%%/                     
                          *%%%#                     ((%%#                       
                             (&%%#((            (##%%%(                         
                                 /&%%%%%%%%%%%%%%#(                      \n\n\n''')

def main(site, requestss):
    if(platform.system() != "Windows"):
        os.system("clear")
    else:
        os.system("cls")
    banner()
    l = int(0)
    if(platform.system() == "Linux"):
        proxy = input("\n\n Do You want to usa a proxy? [Y/n] -> ")
        if(proxy == "Y" or "y"):
            proxyess = {
                "sock4" : "127.0.0.1:9050"
            }
            print("\n\n Starting Tor service...")
            r = os.system("sudo systemctl start tor")
            if(r == 1):
                print("\n Tor not found, please install it")
                exit()
    while(l != requestss):
        try:
            if(proxy == "Y" or "y"):
                p = requests.post(site, auth=('random@gmail.com', 'random123456789'), proxies=proxyess)
            else:
                p = requests.post(site, auth=('random@gmail.com', 'random123456789'))
            if(p.status_code != 200):
                print(f"{p.status_code} ; Request not sent succesfully")
            else:
                print(f"{p.status_code} ; Request sent succesfully")
                l+=1
        except:
            print("Error. site not found")
            exit()
try:
    main(site = site, requestss = requestss)
except KeyboardInterrupt:
    print("the user pressed CTRL+C, stopping the process..")
    exit()
