import socket # socket is low-level utility pre-installed in python module that helps to build network connections using sockets

target = input("Enter the Target you want to scan:") #The domain or IP user wants to target
start_port = int(input("Enter the starting port to scan:")) # Number of port user want scanner to start
end_port = int(input("Enter the port you want scanner to run:")) # Number of port user want scanner to run till
print("-" * 45) #This will print - line 45 times so that it makes a line based difference for better understanding

for port in range(start_port, end_port+1): #Runs the for loop as if it considers 0-4 but won't take 0 it will start with 0,1,2,3 so 4+1 will also conclude till 4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s basically means socket, for socket connection we use AF_INET which stands for Address Family ipv4 and sock_stream means always new TCP socket
    s.settimeout(0.7) # this just set time out before scanning to new port 
    result = s.connect_ex((target,port)) # this will make connection to target and port to check about port 
    if result == 0:   # if result is true means port open in binary 0 = true and 1 = false
        banner = ""      # we give new variable for banner grabbing
        try:   # it will try to grab banner
            s.settimeout(1.0) #another time before moving further
            banner = s.recv(1024).decode().strip()   #it will grab the response after grabbing banner and will decode to give output
        except:
            pass   #if not will pass it to further

        if banner: 
            print(f"[+] Port {port} is open and banner is {banner}") # so if banner is there it will give port and banner both
        else:
            print(f"[+] Port {port} is open") # if can't get banner only port will be displayed
        s.close # socket connection closed here

print("\n Scan Completed")        #scanning completetion print statement/

