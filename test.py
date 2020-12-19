seat = 0
for [left, right] in [[0, 1], [0, 2], [1, 0], [2, 0]]:
    print('left', left, 'right', right)
    leftHand = seat - left if seat - left >= 0 else seat - i
    rightHand = seat + i + 1 if i >= 0 else seat - i - 1
    print('[', leftHand, ',', rightHand, ']')
