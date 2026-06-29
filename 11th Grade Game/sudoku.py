# SUB
# │─┌┐└┘║├┤┬┴┼═║╔╗╚╝╟╢╤╧╠╬╦╩╣╪╙╜
global e
e = " "
"""board=[[5,e,4,e,1,e],[1,3,e,4,e,2],[],
         [2,e,1,e,3,e],[e,e,e,2,e,e],[],
         [6,e,2,e,4,e],[e,5,e,e,e,6],[]]
"""
ans_board = [
    [5, 2, 4, 6, 1, 3],
    [1, 3, 6, 4, 5, 2],
    [],
    [2, 6, 1, 5, 3, 4],
    [3, 4, 5, 2, 6, 1],
    [],
    [6, 1, 2, 3, 4, 5],
    [4, 5, 3, 1, 2, 6],
    [],
]


# init_board=board
def display(L):
    print(f"{'  1 2 3 4 5 6'}")
    print(f"{' ╔═╤═╤═'}{'╦═╤═╤═'}{'╗'}")
    for i in range(len(L)):
        if (i + 1) % 3 != 0:
            if (i + 1) <= 2:
                print(f"{i + 1}{'║'}", end="")
            elif 2 < (i + 1) < 6:
                print(f"{i}{'║'}", end="")
            else:
                print(f"{i - 1}{'║'}", end="")
            for j in range(len(L[i])):
                if (j + 1) % 3 == 0:
                    print(f"{L[i][j]}{'║'}", end="")
                else:
                    print(f"{L[i][j]}{'│'}", end="")
            print()

        elif i == (len(L) - 1):
            print(f"{' ╚═╧═╧═'}{'╩═╧═╧═'}{'╝'}")

        elif (i + 1) % 3 == 0:
            print(f"{' ╠═╪═╪═'}{'╬═╪═╪═'}{'╣'}")


def check(board):
    if board == ans_board:
        return True


def inp(ans_board, board):
    init_board = board
    display(board)
    print(
        "IMPORTANT INFORMATION ",
        "\n",
        "Enter inputs by choosing row, column then input.(blanks represent input fields)",
        "\n",
        "Once done, simply enter without any input in all three fields to submit.",
    )
    lives = 5
    print("Total Lives: ", lives)
    while lives > 0:
        print("-" * 80)
        r = input("Choose Row (1-6)")
        c = input("Choose Column (1-6)")
        n = input("Enter number (1-6)")

        if not r or not c or not n:
            nn = input("Are you sure this is your final answer? (y/n)")
            if nn == "y":
                if check(board):
                    print("You WIN")
                    break
                else:
                    print("Something's wrong, Try Again.")
                    continue
            else:
                continue
        try:
            r = int(r)
            c = int(c)
            n = int(n)
            if r > 2:
                r += 1
            if r > 5:
                r += 1
        except Exception:
            print("Invalid input. Try again.")
            lives -= 1
            print("Lives left: ", lives)
            continue

        if (
            n < 7
            and n > 0
            and r < 9
            and r > 0
            and c < 7
            and c > 0
            and init_board[r - 1][c - 1] == e
        ):
            if n == ans_board[r - 1][c - 1]:
                board[r - 1][c - 1] = n
            else:
                print("Invalid input. Try again. (Incorrect input)")
                lives -= 1
                print(f"Lives left: {lives}")
        else:
            print(
                "Invalid input, try again. (Row no. or Column no. or Input not within 1-6)"
            )
            lives -= 1
            print(f"Lives left: {lives}")

        display(board)
