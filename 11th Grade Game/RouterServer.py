"""RouterServer - Coordinating Program for phase I act III

Internal Use Only
Made for NPS HSR

Credits:
Everytab (Gautham K)
Ralf (Srijon S)"""

# Module Imports
import time
import os


# le function
def GetLStat():
    while True:
        LStat = ""
        try:
            with open("LR", "r") as file:
                LStat = file.read(10)
        except FileNotFoundError:
            with open("LR", "a") as file:
                file.write("NOT RUN")
        LStat = LStat.split(",")
        if len(LStat) == 6:
            del LStat[-1]
        if LStat != [""]:
            break
    return LStat


def GetRStat():
    while True:
        RStat = ""
        try:
            with open("RR", "r") as file:
                RStat = file.read(10)
        except FileNotFoundError:
            with open("RR", "a") as file:
                file.write("NOT RUN")
        RStat = RStat.split(",")
        if len(RStat) == 6:
            del RStat[-1]
        if RStat != [""]:
            break
    return RStat


def BetterDisplay(le_item, a):
    zList = ["121", "122", "123", "124", "W"]
    print(a)
    if len(le_item) == 5:
        for i in range(0, 5, 1):
            print(zList[i], "-", le_item[i])
        print("\n")
    else:
        print("Is offline or invalid data provided")
        print("Data :-", le_item)


# Status (The only thing this will ever do)
overall = 0
delay = 0.1
os.system("clear")
print("RouterServer")
print("Starting in 3 seconds")
time.sleep(3)
with open("ENDR", "w") as file:
    file.write("10")
try:
    while True:
        LStat = GetLStat()
        RStat = GetRStat()
        if overall >= 1:
            os.system("clear")
            BetterDisplay(LStat, "Left")
            BetterDisplay(RStat, "Right")
            overall = 0
        overall = overall + delay

        # TODO : add RStat check as well once everything is ready
        # print("[DEBUG], LSTAT IS:",LStat)
        markq = 0
        while ((len(LStat) == 5) and (LStat[4] == "1")) and (
            (len(RStat) == 5) and (RStat[4] == "1")
        ):
            markq = markq + delay
            LStat = GetLStat()
            RStat = GetRStat()
            with open("ENDR", "w") as file:
                file.write("11")
            time.sleep(delay)
            # print("[DEBUG], InnerLSTAT IS:",LStat)
            if markq >= 3:
                print("The game was completed")
                print("Please keep the server running until the room is ready to reset")
                print(
                    "When the room is ready to reset, press CTRL + C to terminate the server"
                )
                print("and then restart the server")
                with open("ENDR", "w") as file:
                    file.write("12")
                time.sleep(2)
                os.system("python StatusServer.py")
                print("RouterServer quit, e")
                exit()
        time.sleep(delay)
except KeyboardInterrupt:
    print("RouterServer is informing clients of shutdown")
    with open("ENDR", "w") as file:
        file.write("00")
    print("RouterServer has stopped due to manually initated shutdown")
    exit()
