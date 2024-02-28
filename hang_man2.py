drawing_list = ["  -----", "  |   |", "  O   |", " ---  |", "/ | \\ |", "  |   |", " ---  |", "/   \\ |", "|   | |", "      |", "-------"]

guessed_letters = 6
print(drawing_list)
if guessed_letters == 6:
    for item in drawing_list:
        print(item)
elif guessed_letters == 5:
    for item in drawing_list[0:8]:
        print(item)
    for item in range(2):
        print(drawing_list[9])
    print(drawing_list[10])
elif guessed_letters == 4:
    for item in drawing_list[0:7]:
        print(item)
    for item in range(3):
        print(drawing_list[9])
    print(drawing_list[10])
elif guessed_letters == 3:
    for item in drawing_list[0:6]:
        print(item)
    for item in range(4):
        print(drawing_list[9])
    print(drawing_list[10])
elif guessed_letters == 2:
    for item in drawing_list[0:5]:
        print(item)
    for item in range(5):
        print(drawing_list[9])
    print(drawing_list[10])
elif guessed_letters == 1:
    for item in drawing_list[0:4]:
        print(item)
    for item in range(6):
        print(drawing_list[9])
    print(drawing_list[10])
elif guessed_letters == 0:
    for item in drawing_list[0:2]:
        print(item)
    for item in range(8):
        print(drawing_list[9])
    print(drawing_list[10])

