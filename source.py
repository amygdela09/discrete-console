import os

def main(cmmd):
    #run command with proxy
    os.system("sudo proxychains " + cmmd)
    start()
def start():
    #get command
    cmd = input("$")
    #empty
    if cmd == "":
        start()
    #execute
    else:
        main(cmd)
def banner():
    #title
    print("\033[1;32;40mDiscrete Console\nAutomatically proxies commands.")
    print("\033[1;34;40mNo Need To Type Sudo.\033[1;37;40m")
    print("Type any terminal command and it will run through ProxyChains automatically.")
    start()
banner()
