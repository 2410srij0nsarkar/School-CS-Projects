# SUB
import random as rand
import os

global s
global letter
letter = ""
s = False


def display(password):
    lenp = len(password)
    print(f"{'┌'}{'─' * 100}{'┐'}")
    print(f"{'│'}{password}{' ' * (100 - lenp)}{'│'}")
    print(f"{'└'}{'─' * 100}{'┘'}")


# Srijon
def check1(password):
    # 1. Password must be of minimum 8 character length and maximum 75.")
    lenp = len(password)
    if lenp <= 125 and lenp >= 8:
        return True
    else:
        return False


def check2(password):
    # 2. Password must include a capital letter")
    for ch in password:
        # print(ch)
        if ch.isupper():
            return True
    else:
        return False


def check3(password):
    # 3. Password must include any number")
    for ch in password:
        if ch.isdigit():
            return True
    else:
        return False


def check4(password):
    # 4. Password must include 3 special characters")
    count = 0
    for ch in password:
        if not ch.isalnum() and not ch.isspace():
            count += 1

    if count >= 3:
        return True
    else:
        return False


def check5(password):
    # 5. Numbers in the Password must add up to 70") #creator x 2 = 80x2=160 haha cool stuff
    add = 0
    for ch in password:
        if ch.isdigit():
            add += int(ch)
            # print(add)

    if add == 70:
        return True
    else:
        return False


def check6(password):
    # 6. Password must have the current year in Roman Numerals (Without spaces)")
    if "MMXXV" in password:
        return True
    else:
        return False


def check7(password):
    # 7. Password must include element with atomic number 27 (2 letter notation)")
    if "co" in password.lower():
        return True
    else:
        return False


def check8(password):
    # 8. Which colour model is primarily used in computers?(3 letters)")
    if "rgb" in password.lower():
        return True
    else:
        return False


def check9(password):
    # 9. Password must include the word 'cyber' in morse code (use . and -)")
    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-.",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }
    key = ""
    for iter in "CYBER":
        key += morse_dict[iter]

    if key in password:
        return True
    else:
        return False


def check10(password):
    # 10. The password must have the first 6 digits of π")
    L = [3, 1, 4, 1, 5, 9]

    for ch in password:
        if ch.isdigit() and int(ch) in L:
            L.remove(int(ch))

    if L == []:
        return True
    else:
        return False


def check11(password):
    # 11.Password must include letters of the old name of Japan's capital city (Hint: 3 letters)")
    if "eniac" in password.lower():
        return True
    else:
        return False


def check12(password):
    # 12.Password must include the sum of roots of given cubic: x³ - 6x² + 11x - 6 = 0")
    if "6" in password:
        return True
    else:
        return False


def check13(password):
    # 13.Password must end with 'Creator'")
    len(password)
    # print(password[:-8:-1])
    if password[:-8:-1] == "Creator"[::-1]:
        return True
    else:
        return False


def check14(password):
    # 14.Individual Roman Numerals in Password must sum up to 5000")
    Roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    add = 0
    for ch in password:
        if ch.isupper() and ch in Roman_dict.keys():
            add += Roman_dict[ch]

    if add == 5000:
        return True
    else:
        return False


def check15(password):
    # 15.Your password must include the length of your password.")
    x = len(password)
    # print(x)
    if str(x) in password:
        return True
    else:
        return False


def check16(password):
    # 16.Your password must include the name of this symbol(one word): Φ")
    x = "phi"
    if x in password.lower():
        return True
    else:
        return True


def check17(password):
    # 17.Your password must include the initials of the event name.(in capital)")
    x = "BV"
    if x in password:
        return True
    else:
        return True


def check18(password):
    # 18.Your password must include the answer to this cryptic code: Ǽɱʨϣʥ")
    x = "AEmt6wdz"
    if x in password:
        return True
    else:
        return True


def check19(password):
    # 19.Your password must include the first name of the Father of computer science.(Analytical Engine)")
    x = "charles"
    if x in password.lower():
        return True
    else:
        return True


def check20(password):
    # 20.Your password must include the password used to enter the system in Act I")
    x = ["111cr34t0r", "222th3cr34tor222", "321cr34t0rr123", "111cr34t0r111"]
    for i in x:
        if i in password.lower():
            return True
        else:
            return True


"""def check21A(password):
    global s
    if s == True:
        if letter in password:
            print("Password has",letter)
            return (False, 1)
            
        else:
            return (True, 1)
    else:
        return (False,0)

def check21(password):
    global letter
    global s
    print(s)
    #Permanent removal of access to a letter
    if s == False:
        s=True
        x=input("21.A sacrifice must be made. Pick 1 letter that you will no longer be able to use.")
        letter = x[0]
    print("21 shall return",check21A(password)[0])
    return check21A(password)[0]"""


def check21(password):
    # 22.Your pasword must include the smallest number with most factors under 100 in binary.
    # 60
    x = 111100
    if str(x) in password:
        return True
    else:
        return True


def check22(password):
    # 23.Your password must include the answer to this riddle: Tiny yet powerful, I may be positive, negative but never neutral. What am I?
    x = "bit"
    if x in password.lower():
        return True
    else:
        return True


def check23(password):
    count = 0
    # 24.Your password must include the number of capital letters in the password.
    for ch in password:
        if ch.isupper():
            count += 1
    cc = str(count)
    print(cc)
    if cc in password:
        return True
    else:
        return True


def check24(password, c):
    if c:
        y = input(
            "Final Rule.Are you 100 percent certain that this is your final password? Enter it exactly.(Yes/No)"
        )
        if y == "Yes":
            return True
        else:
            print("Be sure next time...")
            m = rand.randint(0, len(password))
            password.replace(password[m], "")
            return False


# MAIN
global Ruledict
Ruledict = {
    "1. Password must be of minimum 8 character length and maximum 100.": "check1(password)",
    "2. Password must include a capital letter": "check2(password)",
    "3. Password must include any number": "check3(password)",
    "4. Password must include 3 special characters": "check4(password)",
    "5. Numbers in the Password must add up to 70": "check5(password)",
    """"6.The password must contain current year in Roman Numerals(Without spaces)

I:1, V:5, X:10, L:50, C:100, D:500, M:1000 """: "check6(password)",
    "7. Password must include element with atomic number 27 (2 letter notation)": "check7(password)",
    "8. Which colour model is primarily used in computers?(3 letters)": "check8(password)",
    """9. Password must include the word 'CYBER' in morse code (use . and -)

'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
'U':'..-.','V':'...-','W':'.--','X':'-..-','Y':'-.--',
'Z':'--..',""": "check9(password)",
    "10. The password must have the first 6 digits of π": "check10(password)",
    "11.Password must include name of a computer from the 1930s, which is considered to be the first computer.": "check11(password)",
    "12.Password must include the sum of roots of given cubic: x³ - 6x² + 11x - 6 = 0": "check12(password)",
    "13.Password must end with 'Creator'": "check13(password)",
    """14.Individual Roman Numerals in Password must sum up to 5000

I:1, V:5, X:10, L:50, C:100, D:500, M:1000 """: "check14(password)",
    "15.Your password must include the length of your password.": "check15(password)",
    "16.Your password must include the name of this symbol(one word): Φ": "check16(password)",
    "17.Your password must include the initials of the event name.(in capital)": "check17(password)",
    "18.Your password must include the answer to this cryptic code: Ǽɱʨϣʥ": "check18(password)",
    "19.Your password must include the first name of the Father of computer science.(Analytical Engine)": "check19(password)",
    "20.Your password must include the password used to enter the system in Act I": "check20(password)",
    "21.Your pasword must include the smallest number with most factors under 100 in binary.": "check21(password)",
    "22.Your password must include the answer to this riddle: Tiny yet powerful, I may be positive, negative but never neutral. What am I?": "check22(password)",
    "23.Your password must include the number of capital letters in the password": "check23(password)",
    "Final Rule.Are you 100 percent certain that this is your final password? Enter it exactly.(Yes/No):": "check24(password)",
}


def password_game():
    status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    c = 0
    password = ""
    while c < 23:
        # Runs all checks and assigns 0 or 1 to status
        for i in range(len(status) - 1):
            if eval(f'check{i + 1}("{password}")'):
                status[i] = 1
            else:
                status[i] = 0
                break
        else:
            if eval(f'check{24}("{password}",1)'):
                status[i] = 1
                return True
            else:
                print("-" * 110)
                status = [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ]
                print(list(Ruledict.keys())[c])
                password = input("Enter Password> ")
                display(password)

        """for j in range(len(status)-1):
            if status[j] == 0:
                c=0
                while True:
                    if eval(f'check{j+1}("{password}")'):
                        status[j] = 1
                        print(status)
                        break
                    else:
                        print(list(Ruledict.keys())[j])
                        password=input("Enter Password> ")
                        display(password)
            else:
                c+=1"""
        if status[c] == 0:
            while True:
                if eval(f'check{c + 1}("{password}")'):
                    status[c] = 1
                    c = 0
                    break
                else:
                    os.system("clear")
                    print("-" * 110)
                    print(list(Ruledict.keys())[c])
                    password = input("Enter Password> ")
                    display(password)

        else:
            c += 1
