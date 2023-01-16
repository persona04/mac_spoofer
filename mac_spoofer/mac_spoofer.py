#!usr/bin/python3


from mac_spoof_functions import * 
import time


arg = arg_taker()
x = arg_checker(arg)
if x == 1:
    old = mac_checker(arg.interface)
    mac_changer(arg.interface,arg.mac)
    new = mac_checker(arg.interface)
    if old == new :
        print(30*'-')
        print("Fail!")
        print(30*'-')
        exit()
    else :
        print(30*'-')
        print("Success!")
        print(30*'-')
        print (f"Old MAC : {old}")
        print(30*'-')
        print(f"New MAC : {new}")
        print(30*'-')
        exit()
elif x == 2:
    mac_list = mac_list_taker(arg.mac_list)
    for i in mac_list:
        old = mac_checker(arg.interface)
        print(i)
        mac_changer(arg.interface,i)
        new = mac_checker(arg.interface)
        if old == new:
            print(30*'-')
            print("Fail!")
            print(30*'-')
        else:
            print(30*'-')
            print("Success!")
            print(30*'-')
        if mac_list[-1] == i:
            print("End of the list!")
            print(30*'-')
            exit()
        time.sleep(60*int(arg.time))
elif x == False:
    print(30*'-')
    print("Wrong parameter usage! ")
    print(30*'-')
    exit()
