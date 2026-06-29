"""MSH - Mad Bourne Shell Left
For Breaking Virtual Act III Phase I

Made for NPS HSR
Credits:
    RouterCore (Left and Right) - Everytab (Gautham K)
    RouterServer - Everytab (Gautham K) and Srijon S
    ChallengeCore - Srijon S

"""

# Module Imports
import time
import os
import random
import ChallengeCore


# Status
stat = [0, 0, 0, 0, 0]
IP = ["192.168.100.121", "192.168.100.122", "192.168.100.123", "192.168.100.124"]
mark = 0
run = 0
filed = "LR"


def Status(mark, run):
    while True:
        master = open("ENDR", "a")
        master.close()
        master = open("ENDR", "r")
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
        with open(filed, "w") as status:
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
    print("[SYSTEM] Establishing connection...")
    while run == 2:
        try:
            mark, run = Status(mark, run)
        except KeyboardInterrupt:
            continue
    if run == 3:
        os.system("clear")
        print("=======================================")
        print("CONNECTION WAS ESTABLISHED SUCCESSFULLY")
        print("=======================================")
        time.sleep(5)
        os.system("python LS.py")
        with open(filed, "w") as file:
            file.write("OFFLINE")
        exit()

    print("[SYSTEM] mind.service has restarted")


def sChal(rid):
    """TODO : Wait for ChallengeCore to be completed then do the corresponding function call here"""
    if ChallengeCore.RChal(rid):
        return True
    else:
        return False


# App Functions
def RouterConsole(rid):
    print("\nLogged in to", str(IP[rid]), "as admin")
    while True:
        try:
            leout = "admin@" + str(IP[rid]) + "> "
            console = input(leout)
            if console.lower() == "shutdown" or console.lower() == "poweroff":
                print("Broadcast from admin\n\nThe system is going down NOW\n")
                time.sleep(2)
                break
            else:
                print(console, ": inaccessible or not found", sep="")
        except KeyboardInterrupt:
            continue


def armChal(health):
    if sChal(0):
        RouterConsole(0)
        print("Lost connection to ", IP[0], sep="")
        health = health - 10
        stat[0] = 1
    else:
        print("Not Authorised")
    return health


def legChal(health):
    if sChal(1):
        RouterConsole(1)
        print("Lost connection to ", IP[1], sep="")
        health = health - 10
        stat[1] = 1
    else:
        print("Not Authorised")
    return health


def heartChal(health):
    if sChal(2):
        RouterConsole(2)
        print("Lost connection to ", IP[2], sep="")
        health = health - 10
        stat[2] = 1
    else:
        print("Not Authorised")
    return health


def lungChal(health):
    if sChal(3):
        RouterConsole(3)
        print("Lost connection to", IP[3], sep="")
        health = health - 10
        stat[3] = 1
    else:
        print("Not Authorised")
    return health


def finalChalDone():
    mark = 0
    run = 1
    stat[4] = 1
    z = 0
    time.sleep(0.5)
    delay = 0.1
    while True:
        mark, run = Status(mark, run)
        try:
            if mark == 1:
                TheEnd(mark, run)
                time.sleep(5)
            else:
                z = z + delay
                time.sleep(delay)
                stat[4] = 1
                if (int(z * 10)) % 10 == 0:
                    print("[SYSTEM] Awaiting other routers to shut down")
                    z = 0
        except KeyboardInterrupt:
            print()
            continue


# Shell Functions


def EasterEgg():
    print('''
            _,met$$$$$gg.          temp_user@thinkpad
         ,g$$$$$$$$$$$$$$$P.       ------------------
       ,g$$P""       """Y$$.".     OS: Debian GNU/Linux 12 (bookworm) x86_64
      ,$$P'              `$$$.     Host: 20CLS12607 (ThinkPad X250)
    ',$$P       ,ggs.     `$$b:    Kernel: Linux 6.1.0-36-amd64
    `d$$'     ,$P"'   .    $$$     Uptime: 1 hour, 2 mins
     $$P      d$'     ,    $$P     Packages: 2048 (dpkg)
     $$:      $$.   -    ,d$$'     Shell: MSH 0.6b
     $$;      Y$b._   _,d$P'       Display : 1366x768 @ 60 Hz in 12" [Built-in]
     Y$$.    `.`"Y$$$$P"'          WM: dtwm (X11)
     `$$b      "-.__               Theme: Crux [GTK2/3]
      `Y$$b                        Icons: gnome [GTK2/3]
       `Y$$.                       Font: Sans (11pt) [GTK2/3]
         `$$b.                     Cursor: core
           `Y$$b.                  Terminal: dtterm
             `"Y$b._               CPU: Intel(R) Core(TM) i5-5300U (4) @ 2.90 GHz
                 `""""             GPU: Intel HD Graphics 5500 @ 0.90 GHz [Integrated]
                                   Memory: 1.44 GiB / 7.62 GiB (19%)
                                   Swap: 0 B / 8.25 GiB (0%)
                                   Disk (/): 41.13 GiB / 76.92 GiB (53%) - xfs
                                   Local IP (wlo1): 192.168.100.35/24
                                   Locale: C
    ''')


def NotFound(item):
    print(item, ": inaccessible or not found", sep="")


def ProgError(item):
    time.sleep(random.randint(1, 10))
    print(item, ": Timed out", sep="")


def UserError(item):
    print(
        item,
        ": User is not a superuser, or does not have permission to run the executable",
        sep="",
    )


def RunProgram(item, health):
    if item == "ssh 192.168.100.121" and stat[0] == 0:
        time.sleep(random.randint(1, 3))
        health = armChal(health)
    elif item == "ssh 192.168.100.122" and stat[1] == 0:
        time.sleep(random.randint(1, 3))
        health = legChal(health)
    elif item == "ssh 192.168.100.123" and stat[2] == 0:
        time.sleep(random.randint(1, 3))
        health = heartChal(health)
    elif item == "ssh 192.168.100.124" and stat[3] == 0:
        time.sleep(random.randint(1, 3))
        health = lungChal(health)
    elif "arp-scan" in item:
        arpScan(item)
    else:
        ProgError(item)
    return health


def arpScan(item):
    arguement = (item.split())[1].lower()
    if arguement == "--localnet":
        print("Starting arp-scan 1.2.0")
        time.sleep(2)
        lenstat = 0
        for i in range(len(stat) - 1):
            if stat[i] == 0:
                print(IP[i], "\tMA:AC:AD:DR:ES:S1\tLinux Powered Router")
                lenstat += 1
        print("\n", lenstat, " packets received.", sep="")
    elif arguement == "invalid":
        print(
            "ERROR: No target hosts on command line and neither --file or --localnet options given"
        )
    else:
        time.sleep(0.5)
        print(
            '''WARNING: get_host_address failed for "''',
            arguement,
            """": Temporary failure in name resolution - target ignored\nERROR: No hosts to process""",
            sep="",
        )


"""VARIABLES, DICTIONARIES AND OTHER SUCH VALUES

The following lines are crucial for the program
DO NOT TOUCH
"""

files = {
    "/": [
        "bin [FOLDER]",
        "boot [FOLDER]",
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
    "/home/temp_user/": [
        "README.TXT [TEXT FILE]",
        """[Use 'cat "filename"' to see its contents, "filename" refers to the name of any kind of file]""",
    ],
}
global health
health = 50
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
]
DIR = "/home/temp_user/"
programs = ["ssh", "arp-scan"]
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
while True:
    mark, run = Status(mark, run)
    try:
        assert run == 1

    except AssertionError:
        try:
            print("[DEBUG] RouterServer is not running...run is", run)
            time.sleep(1)
            continue
        except KeyboardInterrupt:
            print("Shall inform server of quit")
            with open(filed, "w") as file:
                file.write("OFFLINE")
                exit()

    try:
        if health == 10:
            print("[SYSTEM] Preparing to establish connection")
            finalChalDone()

        prompt = "\x1b[92mtemp_user@thinkpad\x1b[0m:\x1b[92m" + DIR + "\x1b[0m$ "
        command = input(prompt).lower()
        args = command.split()
        if args != []:
            if args[0] == "cd":
                if len(args) == 2:
                    QDir = DIR + args[1] + "/"
                    if QDir in files.keys():
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
                elif len(args) == 0:
                    print()
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
            elif args[0] in programs:
                if len(args) == 1:
                    args.append("invalid")
                health = RunProgram((args[0] + " " + args[1]), health)

            elif args[0] == "fastfetch":
                EasterEgg()

            elif args[0] == "cat":
                if len(args) == 1:
                    args.append("invalid")
                if args[1] == "readme.txt":
                    print(
                        """How to shutdown those pesky routers\n\nSo firstly type 'arp-scan --localnet' to see what all routers are online and are accessible to you.\nThen, get its local IP Address, and run 'ssh "IP Address"' (Replace "IP Address" with one of the IP addresses from the arp-scan output)\nThen enter the correct password, it should be scattered around in bits of paper nearby.\nOnce you log in, type 'shutdown' or 'poweroff' to disable the router.\n\nWe can only hope that you will take down that maniac"""
                    )
                else:
                    NotFound(args[1])
            elif args[0] == "debugskipphase2":
                for i in range(0, 4, 1):
                    stat[i] = 1
                health = 10
                print("[DEBUG] skipped phase 2")

            elif args[0] in Dapps:
                UserError(args[0])

            else:
                print(args[0], ": command not found", sep="")

    except KeyboardInterrupt:
        print()
        continue
