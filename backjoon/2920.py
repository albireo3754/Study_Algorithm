

def isAscending():
    musics = list(map(int, input().split(" ")))
    if musics[0] == 1:
        direction = 1
        before = 0
    elif musics[0] == 8:
        direction = -1
        before = 9
    else:
        print("mixed")
        return

    for music in musics:
        if before + direction == music:
            before = music
        else:
            print("mixed")
            return

    if music == 8:
        print("ascending")
    elif music == 1:
        print("descending")

isAscending()