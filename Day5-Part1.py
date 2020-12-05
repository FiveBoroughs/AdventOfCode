import math

with open('Day5-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ';'), inputs))

# exemple
# rows = ['FBFBBFFRLR;', 'BFFFBBFRRR;', 'FFFBBBFRRR;', 'BBFFBBFRLL;']

seatIdsTaken = []
for row in rows:
    currentRangeL = [0, 127]
    currentRangeW = [0, 7]
    for char in row:
        if char == 'F':
            currentRangeL = [
                currentRangeL[0],
                math.ceil(
                    (currentRangeL[1]-currentRangeL[0])/2+currentRangeL[0])-1
            ]
        if char == 'B':
            currentRangeL = [
                math.ceil(
                    (currentRangeL[1]-currentRangeL[0])/2+currentRangeL[0]),
                currentRangeL[1]
            ]
        if char == 'L':
            currentRangeW = [
                currentRangeW[0],
                math.ceil(
                    (currentRangeW[1]-currentRangeW[0])/2+currentRangeW[0])-1
            ]
        if char == 'R':
            currentRangeW = [
                math.ceil(
                    (currentRangeW[1]-currentRangeW[0])/2+currentRangeW[0]),
                currentRangeW[1]
            ]
        if char == ';':
            if(currentRangeL[0] != currentRangeL[1] or currentRangeW[0] != currentRangeW[1]):
                raise Exception(
                    'Received row end before agreeing on Ranges', row, currentRangeL, currentRangeW)

            seatId = currentRangeL[0] * 8 + currentRangeW[0]
            seatIdsTaken.append(seatId)
            print(row, ': row', currentRangeL[0],
                  'col', currentRangeW[0], 'seat', seatId)

seatIdsTaken.sort(reverse=True)
print(seatIdsTaken)
