def onKeyHold(keys):
    global Xvel, Yvel
    print(keys)
    for key in keys:
        change = [*control[key]]
        if change[0] == "x":
            if change[1] == "+":
                player.centerX += int(change[2])
            else:
                player.centerX -= int(change[2])
        else:
            if change[1] == "+":
                player.centerY += int(change[2])
            else:
                player.centerY -= int(change[2])
