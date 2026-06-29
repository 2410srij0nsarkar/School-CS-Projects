# SUB
import os


def Wordle(kW="", W="", firstgen=1):

    kl = []
    for let in kW:
        kl.append(let)

    templ = kl.copy()

    lenkw = len(kW)
    print("╔═══╗" * lenkw)

    if firstgen:
        print(f"║ {' '} ║" * lenkw, end="")

    else:
        for i in range(lenkw):
            if W[i] == kl[i]:
                print("║ ", end="")
                print(f"\x1b[92m{W[i]}\x1b[0m", end="")
                print(" ║", end="")
                templ.remove(W[i])

            elif W[i] != kW[i] and W[i] not in templ:
                print("║ ", end="")
                print(f"\x1b[35m{W[i]}\x1b[0m", end="")
                print(" ║", end="")

            elif W[i] != kW[i] and W[i] in templ:
                print("║ ", end="")
                print(f"\x1b[33m{W[i]}\x1b[0m", end="")
                print(" ║", end="")

    print()
    print("╚═══╝" * lenkw)

    if W == kW:
        win = True

    else:
        win = False

    return win


def MAIN(leword, hint):
    flag = True
    while flag:
        os.system("clear")
        print("-" * 50)
        print(
            "Authentication is required to pass\n\nGUIDE\nPurple - not present\nOrange - present but wrong position\nGreen - Correct Position\n\n",
            hint,
        )
        keyWord = leword.upper()
        tempW = ""
        Wordle(keyWord, tempW, 1)
        att = 0
        while att < 8:
            att += 1
            print("Attempt:", att)
            Word = input("Enter Guess: ").upper()
            if len(Word) != len(keyWord):
                print("Wrong length of word!")
                Wordle(keyWord, tempW, 1)
                continue
            print("-" * 50)
            win = Wordle(keyWord, Word, 0)
            if win:
                print("Challenge Complete.")
                print("Attempts Taken:", att)
                print("Redirecting...")
                flag = False
                return True
                break
        return False

    else:
        return False
