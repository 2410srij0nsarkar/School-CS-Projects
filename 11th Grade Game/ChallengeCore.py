"""ChallengeCore :- Handles challenges for Act III"""

import random
import word
import sudoku
import mind

# import wordle
global schals
global e
e = " "
# test
schals = [0, 1, 2, 3, 4, 5, 6, 7]


def SChal():
    global schals
    if len(schals) == 0:
        print("[ERROR] Too many authentication failures, cannot continue")
        while True:
            try:
                pass
            except Exception:
                continue
    s = random.randrange(0, len(schals))
    chal = schals[s]
    if chal == 0:
        status = stub(
            [
                [5, 2, 4, 6, 1, 3],
                [1, 3, 6, 4, 5, 2],
                [],
                [2, 6, 1, 5, 3, 4],
                [3, 4, 5, 2, 6, 1],
                [],
                [6, 1, 2, 3, 4, 5],
                [4, 5, 3, 1, 2, 6],
                [],
            ],
            [
                [5, e, 4, e, 1, e],
                [1, 3, e, 4, e, 2],
                [],
                [2, e, 1, e, 3, e],
                [e, e, e, 2, e, e],
                [],
                [6, e, 2, e, 4, e],
                [e, 5, e, e, e, 6],
                [],
            ],
        )
    elif chal == 1:
        status = wordle("virtual", "Hint : can be considered not real")
    elif chal == 2:
        status = stub(
            [
                [1, 4, 2, 5, 3, 6],
                [5, 3, 1, 6, 2, 4],
                [],
                [6, 2, 4, 3, 1, 5],
                [3, 5, 6, 1, 4, 2],
                [],
                [4, 1, 5, 2, 6, 3],
                [2, 6, 3, 4, 5, 1],
                [],
            ],
            [
                [e, e, 2, e, 3, e],
                [5, e, 1, 6, 2, e],
                [],
                [6, e, 4, 3, e, e],
                [3, e, e, e, 4, e],
                [],
                [e, 1, e, e, e, e],
                [2, 6, 3, e, e, 1],
                [],
            ],
        )
    elif chal == 3:
        status = wordle("keyboard", "Hint : One of the input devices")
    elif chal == 4:
        status = stub(
            [
                [4, 1, 2, 5, 3, 6],
                [5, 3, 6, 4, 1, 2],
                [],
                [6, 4, 3, 2, 5, 1],
                [2, 5, 1, 6, 4, 3],
                [],
                [1, 2, 5, 3, 6, 4],
                [3, 6, 4, 1, 2, 5],
                [],
            ],
            [
                [e, 1, e, 5, 3, e],
                [e, e, e, 4, 1, e],
                [],
                [e, e, e, e, e, e],
                [2, 5, e, e, 4, e],
                [],
                [1, e, e, e, e, 4],
                [e, 6, e, 1, e, e],
                [],
            ],
        )
    elif chal == 5:
        status = wordle("mouse", "Hint : One of the input devices")
    elif chal == 6:
        status = wordle("ethernet", "Hint : Faster internet")
    elif chal == 7:
        status = wordle("nvidia", "Hint : One of the trillion dollar companies")
    schals = schals[0:s:1] + schals[s + 1 : :]
    print(schals)
    return status


def RChal(rid):
    """Ensure all passwords are 6 digits for uniformity, if otherwise, literally any string should work fine"""
    RPasses = [
        "197635",
        "208515",
        "397531",
        "409852",
        "537935",
        "649274",
        "719573",
        "824964",
    ]
    la = "admin@192.168.100.12" + str(rid + 1) + "'s password > "
    lepass = input(la)
    if lepass == RPasses[rid]:
        return True
    else:
        print("Permission Denied")
        return False


def MChal():
    return mind.password_game()


def stub(ans, board):
    # word.MAIN()
    return sudoku.inp(ans, board)


def wordle(lword, hint):
    return word.MAIN(lword, hint)
