import re 
import subprocess
import argparse
import json

def mac_changer(interface,mac):
    subprocess.run(["ifconfig",interface,"down"])
    subprocess.run(["ifconfig",interface,"hw","ether",mac])
    subprocess.run(["ifconfig",interface,"up"])


def mac_checker(interface):
    mac = subprocess.run(["ifconfig",interface], capture_output=True, text=True)
    mac = mac.stdout
    mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",mac)
    return mac.group()


def arg_taker():
    obj = argparse.ArgumentParser()
    obj.add_argument("-i", "--interface", help="To select interface.", dest="interface")
    obj.add_argument("-m", "--mac_address", help="For new MAC address.", dest="mac")
    obj.add_argument("-t", "--time", help="To set time", dest="time")
    obj.add_argument("-ml", "--mac_list", help="To add MAC list and -t required.", dest="mac_list")
    args = obj.parse_args()
    return args


def arg_checker(args):
    interface = args.interface
    mac = args.mac
    time = args.time
    mac_list = args.mac_list
    arg_list = [bool(mac),bool(interface),bool(mac_list),bool(time)] 
    if arg_list == [True, True, False, False]:
        return 1
    elif arg_list == [False, True, True, True ]:
        return 2 
    else:
        return False


def mac_list_taker(path):
    with open(path,"r",encoding="utf-8") as file:
        data = json.load(file)
    return data



