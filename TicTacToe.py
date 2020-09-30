print("---------")
print(f"|       |")
print(f"|       |")
print(f"|       |")
print("---------")

li = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
dic = {"1 1": li[6], "2 1": li[7], "3 1": li[8], "1 2": li[3], "2 2": li[4], "3 2": li[5], "1 3": li[0], "2 3": li[1],
       "3 3": li[2]}
diction = {"1 1": 6, "2 1": 7, "3 1": 8, "1 2": 3, "2 2": 4, "3 2": 5, "1 3": 0, "2 3": 1, "3 3": 2}

while " " in li:
    ok = True
    while ok:
        word = input("Enter the coordinates: ")
        x, y = word.split()
        if x.isdigit() and y.isdigit():
            if int(x) in range(1, 4) and int(y) in range(1, 4):
                if dic[word] == ' ':
                    li[diction.get(word)] = "X"
                    ok = False
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    print("---------")
    print(f"| {li[0]} {li[1]} {li[2]} |")
    print(f"| {li[3]} {li[4]} {li[5]} |")
    print(f"| {li[6]} {li[7]} {li[8]} |")
    print("---------")

    is_x = False
    is_o = False

    if li[0] == li[1] and li[1] == li[2] and li[2] == 'O':
        is_o = True
    elif li[3] == li[4] and li[4] == li[5] and li[5] == 'O':
        is_o = True
    elif li[6] == li[7] and li[7] == li[8] and li[8] == 'O':
        is_o = True
    elif li[0] == li[3] and li[3] == li[6] and li[6] == 'O':
        is_o = True
    elif li[4] == li[1] and li[1] == li[7] and li[7] == 'O':
        is_o = True
    elif li[2] == li[5] and li[5] == li[8] and li[8] == 'O':
        is_o = True
    elif li[0] == li[4] and li[4] == li[8] and li[8] == 'O':
        is_o = True
    elif li[2] == li[4] and li[4] == li[6] and li[6] == 'O':
        is_o = True

    if li[0] == li[1] and li[1] == li[2] and li[2] == 'X':
        is_ = True
    elif li[3] == li[4] and li[4] == li[5] and li[5] == 'X':
        is_x = True
    elif li[6] == li[7] and li[7] == li[8] and li[8] == 'X':
        is_x = True
    elif li[0] == li[3] and li[3] == li[6] and li[6] == 'X':
        is_x = True
    elif li[4] == li[1] and li[1] == li[7] and li[7] == 'X':
        is_x = True
    elif li[2] == li[5] and li[5] == li[8] and li[8] == 'X':
        is_x = True
    elif li[0] == li[4] and li[4] == li[8] and li[8] == 'X':
        is_x = True
    elif li[2] == li[4] and li[4] == li[6] and li[6] == 'X':
        is_x = True

    if is_x:
        print("X wins")
        break
    elif is_o:
        print("O wins")
        break
else:
    print("Draw")