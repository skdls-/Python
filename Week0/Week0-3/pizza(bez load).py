import os
import sys
from time import time
from datetime import datetime


orders = {}


def pizza():
    while True:
        last_command = ""
        command = input("Enter command>")
        if command == "finish":
            if last_command != "save":
                print (
                    "You haven't saved your order. If you wish to continue, type finish again. If you want to save your order, type save.")
                command = input("Enter command>")
            if command == "finish":
                print ("Order Finished.")
                break
        elif command != "finish":
            if command.startswith("take"):
                take(command.split()[1], command.split()[2])
            elif command == "status":
                last_command = "status"
                print("status_aktiviran")
                status()
            elif command == "save":
                last_command = "save"
                ts = time()
                stamp = datetime.fromtimestamp(
                    ts).strftime('%Y_%m_%d_%H_%M_%S')
                filename = "orders_" + stamp
                file = open(filename, "w")
                for order, price in orders.items():
                    file.write("{}: {} \n".format(order, price))

                file.close()
            elif command == "list":
                i = 1
                for path, subdirs, files in os.walk('/home/rolev/Python/Week0/Week0-3'):
                    for filename in files:
                        if filename.startswith("order"):
                            last_command = "list"
                            f = os.path.join(filename)
                            print ("[", i, "]", str(f))
                            i += 1


def take(name, price):
    if name not in orders:
        orders[name] = int(price)
    else:
        orders[name] += int(price)


def status():
    for order, price in orders.items():
        print("{}: {}".format(order, price))

pizza()
