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
    while(l != requestss):
        p = requests.post(site, auth=('random@gmail.com', 'random123456789'))
        if(p.status_code != 200):
            print(f"{p.status_code} ; Request not sent succesfully")
        else:
            print(f"{p.status_code} ; Request sent succesfully")
            l+=1
try:
    main(site = site, requestss = requestss)
except KeyboardInterrupt:
    print("the user pressed CTRL+C, stopping the process..")
    exit()