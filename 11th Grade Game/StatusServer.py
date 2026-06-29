'''StatusServer - Coordinating Program for the entire ACT III

Internal Use Only
Made for NPS HSR

Credits: Everytab (GauthamK)'''




# Module Imports
import time
import os

# le function
def GetLStat():
    while True:
        LStat = ""
        try:
            with open("LS","r") as file:
                LStat = file.read(10)
        except FileNotFoundError:
            with open("LS","a") as file:
                file.write("NOT RUN")
        LStat = LStat.split(",")
        if len(LStat) == 6:
            del(LStat[-1])
        if LStat != ['']:
            break
    return LStat

def GetRStat():
    while True:
        RStat = ""
        try:
            with open("RS","r") as file:
                RStat = file.read(10)
        except FileNotFoundError:
            with open("RS","a") as file:
                file.write("NOT RUN")
        RStat = RStat.split(",")
        if len(RStat) == 6:
            del(RStat[-1])
        if RStat != ['']:
            break
    return RStat

def BetterDisplay(le_item, a):
    zList = ["Arm","Leg","Heart","Body","Mind"]
    print(a)
    if len(le_item) == 5:
        for i in range(0,5,1):
            print(zList[i],"-",le_item[i])
        print("\n")
    else:
        print("Is offline or invalid data provided")
        print("Data :-",le_item)


# Status (The only thing this will ever do)
overall = 0
delay = 0.1
os.system("clear")
print("StatusServer 0.5")
print("Starting in 1 second")
time.sleep(1)
with open("END","w") as file:
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
        while ((len(LStat)== 5) and (LStat[4] == "1")) and ((len(RStat) == 5) and (RStat[4] == "1")):
            markq = markq + delay
            LStat = GetLStat()
            RStat = GetRStat()
            with open("END","w") as file:
                file.write("11")
            time.sleep(delay)
            # print("[DEBUG], InnerLSTAT IS:",LStat)
            if markq >= 3:
                print("The game was completed")
                print("Please keep the server running until the room is ready to reset")
                print("When the room is ready to reset, press CTRL + C to terminate the server")
                print("and then restart the server")
                while True:
                    with open("END","w") as file:
                        file.write("12")
                    time.sleep(2)
        time.sleep(delay)
except KeyboardInterrupt:
    print("StatusServer is informing clients of shutdown")
    with open("END", "w") as file:
        file.write("00")
    print("StatusServer has stopped due to manually initated shutdown")
    exit()

