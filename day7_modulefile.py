from colorama import init, Fore
def errormessage (msg, Thisiswarning = False):
    if Thisiswarning:
        print(Fore.YELLOW + "This is a warning")
        print(Fore.RED + msg)
        print(Fore.WHITE)
    else:
        print(Fore.BLUE + msg)
        print(Fore.WHITE)

