def print_banner():
    banner = r"""
                                                                                                                              
                                                                                                                              
                                 ___                                                                                          
,-.----.                       ,--.'|_                                                                                        
\    /  \    ,---.    __  ,-.  |  | :,'                                                  ,---,      ,---,             __  ,-. 
|   :    |  '   ,'\ ,' ,'/ /|  :  : ' :           .--.--.                            ,-+-. /  | ,-+-. /  |          ,' ,'/ /| 
|   | .\ : /   /   |'  | |' |.;__,'  /           /  /    '     ,---.     ,--.--.    ,--.'|'   |,--.'|'   |   ,---.  '  | |' | 
.   : |: |.   ; ,. :|  |   ,'|  |   |           |  :  /`./    /     \   /       \  |   |  ,"' |   |  ,"' |  /     \ |  |   ,' 
|   |  \ :'   | |: :'  :  /  :__,'| :           |  :  ;_     /    / '  .--.  .-. | |   | /  | |   | /  | | /    /  |'  :  /   
|   : .  |'   | .; :|  | '     '  : |__          \  \    `. .    ' /    \__\/: . . |   | |  | |   | |  | |.    ' / ||  | '    
:     |`-'|   :    |;  : |     |  | '.'|          `----.   \'   ; :__   ," .--.; | |   | |  |/|   | |  |/ '   ;   /|;  : |    
:   : :    \   \  / |  , ;     ;  :    ;         /  /`--'  /'   | '.'| /  /  ,.  | |   | |--' |   | |--'  '   |  / ||  , ;    
|   | :     `----'   ---'      |  ,   /         '--'.     / |   :    :;  :   .'   \|   |/     |   |/      |   :    | ---'     
`---'.|                         ---`-'            `--'---'   \   \  / |  ,     .-./'---'      '---'        \   \  /           
  `---`                                                       `----'   `--`---'                             `----'            
                                                                                                                              
    """
    print(banner)

    info = """
    =[ Port Scanner v1.0 ]

    """
    print(info)


if __name__ == "__main__":
    print_banner() 

import socket

# Target IP address or hostname
target = input("Enter target IP or hostname: ")

# Port range
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except:
                service = "unknown"
            print(f"✅ Port {port} ({service}) is OPEN")
        else:
            print(f"❌ Port {port} is CLOSED")
        s.close()
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        break
    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
        break
    except socket.error:
        print("❌ Couldn't connect to server.")
        break
