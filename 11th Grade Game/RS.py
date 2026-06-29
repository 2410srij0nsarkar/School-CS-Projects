"""MSH - Mad Bourne Shell Right
For Breaking Virtual Act III Phase II and III (May add Phase I)

Made for NPS HSR
Credits:
    Core (Left and Right) - Everytab (Gautham K)
    StatusServer - Everytab (Gautham K)
    ChallengeCore - Others (put your names here once its ready)

"""

# Module Imports
import time
import os
import ChallengeCore


# Status
stat = [0, 0, 0, 0, 0]
mark = 0
run = 0


def Status(mark, run):
    while True:
        master = open("END", "a")
        master.close()
        master = open("END", "r")
        master.seek(0)
        boss = master.read(2)
        if boss == "11":
            mark = 1
            run = 2
        elif boss == "12":
            mark = 1
            run = 3
        elif boss == "10":
            run = 1
            mark = 0
        elif (boss == "00") or (boss == "01"):
            mark = 0
            run = 0
        else:
            mark = ""
        master.close()
        with open("RS", "w") as status:
            towrite = ""
            for i in stat:
                towrite = towrite + str(i) + ","
            status.write(towrite)
        if (mark != "") and (run != ""):
            break
        else:
            # print("[DEBUG] ReadError (Server updated value)")
            pass
    return mark, run


def TheEnd(mark, run):
    print("[SYSTEM] CRITICAL : mind.service is not running")
    while run == 2:
        try:
            mark, run = Status(mark, run)
        except KeyboardInterrupt:
            continue
    if run == 3:
        os.system("clear")
        print("The system cannot continue")
        print("")
        print("=======================================")
        print("IT IS NOW SAFE TO TURN OFF THE COMPUTER")
        print("=======================================")
    while run == 3:
        try:
            mark, run = Status(mark, run)
        except KeyboardInterrupt:
            continue
    print("[SYSTEM] mind.service has restarted")


# App Functions
def armChal(health):
    print("[SYSTEM] arm.service has been disabled")
    health = health - 10
    stat[0] = 1
    return health


def legChal(health):
    print("[SYSTEM] leg.service has been disabled")
    health = health - 10
    stat[1] = 1
    return health


def heartChal(health):
    print("[SYSTEM] heart.service has been disabled")
    health = health - 10
    stat[2] = 1
    return health


def lungChal(health):
    print("[SYSTEM] lung.service has been disabled")
    health = health - 10
    stat[3] = 1
    return health


def finalChal():
    if ChallengeCore.MChal():
        finalChalDone()


def finalChalDone():
    mark = 0
    run = 1
    stat[4] = 1
    print("[SYSTEM] mind.service has stopped responding.")
    print("[SYSTEM] mind2.service is still running, will try to recover")
    print("[SYSTEM] Attempting to restart mind.service...")
    z = 0
    time.sleep(0.5)
    delay = 0.1
    while z <= 60:
        mark, run = Status(mark, run)
        try:
            if mark == 1:
                TheEnd(mark, run)
                time.sleep(5)
            else:
                time.sleep(delay)
                z = z + delay
                stat[4] = 1
                if (int(z * 10)) % 10 == 0:
                    print("[RECOVERY]", (60 - (int(z * 10) / 10)), "seconds left")
        except KeyboardInterrupt:
            print()
            continue
    stat[4] = 0
    print("[RECOVERY] mind.service was restarted succesfully")
    print("[SYSTEM] System integrity has been restored")


# Shell Functions


def EasterEgg():
    print('''
            _,met$$$$$gg.          tempuser@CreatorSystem
         ,g$$$$$$$$$$$$$$$P.       ---------------------------
       ,g$$P""       """Y$$.".     OS: Debian GNU/Linux 12 (bookworm) x86_64
      ,$$P'              `$$$.     Host: CustomBoard v7
    ',$$P       ,ggs.     `$$b:    Kernel: Linux 6.1.0-35-amd64
    `d$$'     ,$P"'   .    $$$     Uptime: 72 days, 23 hours, 38 mins
     $$P      d$'     ,    $$P     Packages: 2066 (dpkg)
     $$:      $$.   -    ,d$$'     Shell: MSH 0.6b
     $$;      Y$b._   _,d$P'       Display : 800x600 @ 60 Hz in 14" [External]
     Y$$.    `.`"Y$$$$P"'          WM: dtwm (X11)
     `$$b      "-.__               Theme: Crux [GTK2/3]
      `Y$$b                        Icons: gnome [GTK2/3]
       `Y$$.                       Font: Sans (11pt) [GTK2/3]
         `$$b.                     Cursor: core
           `Y$$b.                  Terminal: dtterm
             `"Y$b._               CPU: AMD Ryzen 5 5500 (12) @ 3.60 GHz
                 `""""             GPU: NVIDIA GeForce GT 710 [Discrete]
                                   Memory: 2.13 GiB / 15.48 GiB (14%)
                                   Swap: 0 B / 8.25 GiB (0%)
                                   Disk (/): 35.76 GiB / 102.66 GiB (35%) - jfs
                                   Local IP (wlo1): 192.168.1.35/24
                                   Locale: C
    ''')


def NotFound(item):
    print(item, ": inaccessible or not found", sep="")


def ProgError(item):
    print(
        item,
        ": ERROR : ",
        item,
        ".service is not running and is unable to start",
        sep="",
    )


def UserError(item):
    print(
        item,
        ": User is not a superuser, or does not have permission to run the executable",
        sep="",
    )


def RunProgram(item, health):
    if item == "armcore" and stat[0] == 0:
        health = armChal(health)
    elif item == "legcore" and stat[1] == 0:
        health = legChal(health)
    elif item == "heartcore" and stat[2] == 0:
        health = heartChal(health)
    elif item == "lungcore" and stat[3] == 0:
        health = lungChal(health)
    elif item == "mind":
        finalChal()
    else:
        ProgError(item)

    return health


"""VARIABLES, DICTIONARIES AND OTHER SUCH VALUES

The following lines are crucial for the program
DO NOT TOUCH
"""

files = {
    "/": [
        "bin [FOLDER]",
        "boot [FOLDER]",
        "creator [FOLDER]",
        "dev [FOLDER]",
        "etc [FOLDER]",
        "home [FOLDER]",
        "lib64 [FOLDER]",
        "mnt [FOLDER]",
        "opt [FOLDER]",
        "proc [FOLDER]",
        "root [FOLDER]",
        "sys [FOLDER]",
        "tmp [FOLDER]",
        "usr [FOLDER]",
    ],
    "/home/": [".. [GO UP]", "temp_user [FOLDER]"],
    "/creator/": [".. [GO UP]", "body [FOLDER]", "mind [FOLDER]"],
    "/creator/body/": [".. [GO UP]", "internal [FOLDER]", "external [FOLDER]"],
    "/creator/body/external/": [".. [GO UP]", "arm [FOLDER]", "leg [FOLDER]"],
    "/creator/body/external/arm/": [
        ".. [GO UP]",
        "armcore",
        "armcore.conf",
        "assets [FOLDER]",
    ],
    "/creator/body/external/leg/": [
        ".. [GO UP]",
        "legcore",
        "legcore.conf",
        "assets [FOLDER]",
    ],
    "/creator/body/internal/": [".. [GO UP]", "heart [FOLDER]", "lung [FOLDER]"],
    "/creator/body/internal/heart/": [
        ".. [GO UP]",
        "heartcore",
        "heartcore.conf",
        "assets [FOLDER]",
    ],
    "/creator/body/internal/lung/": [
        ".. [GO UP]",
        "lungcore",
        "lungcore.conf",
        "assets [FOLDER]",
    ],
}
global health
health = 50
programs = {
    "armcore": "/creator/body/external/arm/",
    "legcore": "/creator/body/external/leg/",
    "heartcore": "/creator/body/internal/heart/",
    "lungcore": "/creator/body/internal/lung/",
    "mind": "/creator/mind/",
}
Ddirs = [
    "/bin/",
    "/boot/",
    "/dev/",
    "/etc/",
    "/lib64/",
    "/mnt/",
    "/opt/",
    "/proc/",
    "/root/",
    "/sys/",
    "/tmp/",
    "/usr/",
    "/home/temp_user/",
    "/creator/mind/",
    "/creator/body/external/arm/assets/",
    "/creator/body/external/leg/assets/",
    "/creator/body/internal/lung/assets/",
    "/creator/body/internal/heart/assets/",
]
DIR = "/"
Dapps = [
    "apt",
    "systemctl",
    "dpkg",
    "bash",
    "cp",
    "rm",
    "mv",
    "sudo",
    "pkg",
    "uname",
    "cat",
    "whoami",
    "alias",
    "pkill",
    "kill",
    "shutdown",
    "poweroff",
    "reboot",
    "logout",
    "exit",
    "end",
    "echo",
    "fdisk",
    "startx",
    "sh",
    "tar",
    "make",
    "chmod",
    "date",
    "rmdir",
]


os.system("clear")
print("Welcome to CreatorSystem!")
while True:
    mark, run = Status(mark, run)
    try:
        assert run == 1

    except AssertionError:
        try:
            print("[DEBUG] StatusServer is not running...run is", run)
            time.sleep(1)
            continue
        except KeyboardInterrupt:
            print("Shall inform server of quit")
            with open("RS", "w") as file:
                file.write("OFFLINE")
                exit()

    try:
        if health == 10:
            print(
                "[SYSTEM] WARNING : mindsecure.service requires either arm.service, leg.service, heart.service or body.service to be running"
            )
            print("[SYSTEM] /creator/mind/ is now unprotected!")
            print(
                "[SYSTEM] Please use systemctl as a superuser and restart the service to ensure integrity"
            )
            Ddirs.remove("/creator/mind/")
            files["/creator/mind/"] = [".. [GO UP]", "mind [SYSTEM FILE]"]
            health = health - 1

        prompt = "\x1b[92mtemp_user@creatorsystem\x1b[0m:\x1b[92m" + DIR + "\x1b[0m$ "
        command = input(prompt).lower()
        args = command.split()
        if args != []:
            if args[0] == "cd":
                if len(args) == 2:
                    QDir = DIR + args[1] + "/"
                    if (
                        QDir == "/creator/body/internal/"
                        or args[1] == "/creator/body/external/"
                    ):
                        if ChallengeCore.SChal():
                            DIR = QDir
                        else:
                            print("[SYSTEM] Access is denied")
                    elif QDir in files.keys():
                        DIR = QDir
                    elif QDir in Ddirs:
                        print(
                            "cd: failed to switch to '",
                            args[1],
                            "': Permission denied",
                            sep="",
                        )
                    elif args[1] == "..":
                        if DIR != "/":
                            updir = DIR.split("/")
                            updir.pop()
                            updir.pop()
                            DIR = "/"
                            if updir != []:
                                j = 0
                                while j < len(updir):
                                    if updir[j] == "":
                                        del updir[j]
                                    j = j + 1
                                for i in updir:
                                    DIR = DIR + i + "/"

                    else:
                        print("cd: ", args[1], ": No such file or directory", sep="")
                else:
                    print("cd: too many arguements")
            elif args[0] == "pwd":
                print(DIR)
            elif args[0] == "dir" or args[0] == "ls":
                shw = []
                if len(args) == 1:
                    shw.append(DIR)
                else:
                    for i in range(1, len(args), 1):
                        shw.append(args[i])
                for j in shw:
                    if (j[0] != "/") and (
                        ((DIR + j + "/") in files.keys()) or ((DIR + j + "/") in Ddirs)
                    ):
                        j = DIR + j + "/"
                    elif j[0] == "/" and j[-1] != "/":
                        j = j + "/"

                    if j in files.keys():
                        print(j, ":", sep="")
                        for i in files[j]:
                            print("  ", i)
                        print("	", len(files[j]), "file(s)\n")
                    elif j in Ddirs:
                        print("ls: cannot access'", j, "': Permission denied", sep="")
                    elif j in files[DIR]:
                        print(j, ":", sep="")
                        for i in files[DIR]:
                            k = 0
                            if j in i:
                                print("  ", i)
                                k = k + 1
                        print(" ", k, "file(s)\n")
                    else:
                        print(
                            "ls: cannot access '",
                            j,
                            "': No such file or directory",
                            sep="",
                        )
            elif (args[0] in programs) and (DIR == programs[args[0]]):
                health = RunProgram(args[0], health)

            elif args[0] == "fastfetch":
                EasterEgg()

            elif args[0] == "debugskipphase2":
                for i in range(0, 4, 1):
                    stat[i] = 1
                health = 10
                print("[DEBUG] skipped phase 2")

            elif args[0] in Dapps:
                UserError(args[0])

            elif args[0] == "help":
                print("""
               cd <FolderName> - Navigate to that folder
               cd .. - Navigate out of the subfolder
               dir - list all files in a folder
               ls - list all files in a folder
               pwd - print current working directory
	       
               Extra Information :
               Your goal, is to disable all the body parts of the boss, then the mind.
               it is stored in /creator/body/ and /creator/mind/ respectively.
               List of body parts which should be disabled :- heart, lungs, arms and legs.
	       
               There is a "security" system which protects these, but for some reason instead of asking for a password
               or authentication, it gives a challenge, which is a flaw we can exploit.

               Get through these challenges, and disable the creator to end them once and for all.""")

            else:
                print(args[0], ": command not found", sep="")

    except KeyboardInterrupt:
        print()
        continue
