import math

with open('Day11-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

# exemple
rows = ['L.LL.LL.LL',
        'LLLLLLL.LL',
        'L.L.L..L..',
        'LLLL.LL.LL',
        'L.LL.LL.LL',
        'L.LLLLL.LL',
        '..L.L.....',
        'LLLLLLLLLL',
        'L.LLLLLL.L',
        'L.LLLLL.LL']


class Cell:
    def __init__(self, pX, pY, pV):
        self.x = pX
        self.y = pY
        self.v = pV

    def __repr__(self):
        return self.v

    def left(self, pZ):
        if (self.x-pZ >= 0):
            return [self.x-pZ, self.y]

    def right(self, pZ):
        if self.x+pZ < rowLength:
            return [self.x+pZ, self.y]

    def up(self, pZ):
        if self.y-pZ >= 0:
            return [self.x, self.y-pZ]

    def down(self, pZ):
        if self.y+pZ < mapLength:
            return [self.x, self.y+pZ]

    def upLeft(self, pZ):
        if self.x-pZ >= 0 and self.y-pZ >= 0:
            return [self.x-pZ, self.y-pZ]

    def downLeft(self, pZ):
        if self.x-pZ >= 0 and self.y+pZ < mapLength:
            return [self.x-pZ, self.y+pZ]

    def upRight(self, pZ):
        if self.x+pZ < rowLength and self.y-pZ >= 0:
            return [self.x+pZ, self.y-pZ]

    def downRight(self, pZ):
        if self.x+pZ < rowLength and self.y + pZ < mapLength:
            return [self.x+pZ, self.y+pZ]


emptySeat = 'L'
floor = '.'
occupiedSeat = '#'
seatMaps = []

# Build initial seatMap
seatRows = []
rowLength = len(rows[0])
mapLength = len(rows)
for i in range(len(rows)):
    seats = []
    for j in range(len(rows[i])):
        seats.append(Cell(i, j, rows[i][j]))
    seatRows.append(seats)
seatMaps.append(seatRows)


# def nbAdjascentOccupied(pSeats):
#     total = 0
#     for tempSeat in range(len(pSeats)):
#         if pSeats[tempSeat] == occupiedSeat:
#             total += 1
#         else:
#             break
#     return total


# def getRange(pSeat, pLeft, pRight):
#     if pLeft > 0:
#         return list(range(pSeat - pLeft, pSeat))
#     if pRight > 0:
#         return list(range(pSeat + 1, pSeat + 1 + pRight))
#     return [pSeat]


# def findAdjascent(pCurrentSeatMap, pSeatRowIndex, pSeatIndex, pUp=0, pDown=0,  pLeft=0, pRight=0):
#     print('find start row, seat', pSeatRowIndex, pSeatRowIndex,
#           '| Up, down, left , right', pUp, pDown, pLeft, pRight)
#     res = []

#     # TopLeft
#     if pUp > 0 and pLeft > 0:
#         for tempUp in getRange(pSeat, pUp, pDown):
#             for

#     rowsRange = getRange(pSeatRowIndex, pUp, pDown)
#     seatsRange = getRange(pSeatIndex, pLeft, pRight)
#     print('ranges', rowsRange, seatsRange)

#     for tempRowIndex in rowsRange:
#         if tempRowIndex >= 0 and tempRowIndex < mapLength:
#             for tempSeatIndex in seatsRange:
#                 if tempSeatIndex >= 0 and tempSeatIndex < rowLength:
#                     if
#                     print('row', tempRowIndex, 'col', tempSeatIndex, '=',
#                           pCurrentSeatMap[tempRowIndex][tempSeatIndex])
#                     res.append(
#                         pCurrentSeatMap[tempRowIndex][tempSeatIndex])
#     return res


# If the map doesn't change, we done
while len(seatMaps) < 2 or seatMaps[len(seatMaps)-1] != seatMaps[len(seatMaps)-2]:
    currentSeatMap = seatMaps[len(seatMaps)-1]
    print('map', len(seatMaps))
    newSeatMap = []
    for seatRow in currentSeatMap:
        print('row', seatRow)
        newSeatMapRow = []
        for seat in seatRow:
            newSeat = Cell(seat.x, seat.y, seat.v)

            # If seat is empty and no occupied seats adjacent
            # Seat becomes occupied
            if seat.v == emptySeat:
                leftSeats = [seat.left(x) for x in range(1, 2)]
                rightSeats = [seat.right(x) for x in range(1, 2)]
                upSeats = [seat.up(x) for x in range(1, 2)]
                downSeats = [seat.down(x) for x in range(1, 2)]
                upLeftSeats = [seat.upLeft(x) for x in range(1, 2)]
                downLeftSeats = [seat.downLeft(x) for x in range(1, 2)]
                upRightSeats = [seat.upRight(x) for x in range(1, 2)]
                downRightSeats = [seat.downRight(x) for x in range(1, 2)]

                leftOccupied, rightOccupied, upOccupied, downOccupied, upLeftOccupied, downLeftOccupied, upRightOccupied, downRightOccupied = (
                    0,)*8
                for seatItem in leftSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    leftOccupied += 1
                for seatItem in rightSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    rightOccupied += 1
                for seatItem in upSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    upOccupied += 1
                for seatItem in downSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    downOccupied += 1
                for seatItem in upLeftSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    upLeftOccupied += 1
                for seatItem in downLeftSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    downLeftOccupied += 1
                for seatItem in upRightSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    upRightOccupied += 1
                for seatItem in downRightSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    downRightOccupied += 1

                if (len([x for x in [leftOccupied, rightOccupied, upOccupied, downOccupied, upLeftOccupied, downLeftOccupied, upRightOccupied, downRightOccupied] if x != 0]) == 0):
                    newSeat.v = occupiedSeat

            # If seat is occupied and >4 occupied seats adjacent
            # Seat becomes empty
            if seat == occupiedSeat:
                leftSeats = [seat.left(x) for x in range(1, 5)]
                rightSeats = [seat.right(x) for x in range(1, 5)]
                upSeats = [seat.up(x) for x in range(1, 5)]
                downSeats = [seat.down(x) for x in range(1, 5)]
                upLeftSeats = [seat.upLeft(x) for x in range(1, 5)]
                downLeftSeats = [seat.downLeft(x) for x in range(1, 5)]
                upRightSeats = [seat.upRight(x) for x in range(1, 5)]
                downRightSeats = [seat.downRight(x) for x in range(1, 5)]

                leftOccupied, rightOccupied, upOccupied, downOccupied, upLeftOccupied, downLeftOccupied, upRightOccupied, downRightOccupied = (
                    0,)*8
                for seatItem in leftSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    leftOccupied += 1
                for seatItem in rightSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    rightOccupied += 1
                for seatItem in upSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    upOccupied += 1
                for seatItem in downSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    downOccupied += 1
                for seatItem in upLeftSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    upLeftOccupied += 1
                for seatItem in downLeftSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    downLeftOccupied += 1
                for seatItem in upRightSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    upRightOccupied += 1
                for seatItem in downRightSeats:
                    if seatItem == None or currentSeatMap[seatItem[0]][seatItem[1]].v in [emptySeat, floor]:
                        break
                    downRightOccupied += 1

                if leftOccupied + rightOccupied + upOccupied + downOccupied + upLeftOccupied + downLeftOccupied + upRightOccupied + downRightOccupied >= 4:
                    newSeat.v = emptySeat

            newSeatMapRow.append(newSeat)
        newSeatMap.append(newSeatMapRow)
    seatMaps.append(newSeatMap)

seatsOccupied = 0
# How many seats end up occupied
for seatRow in seatMaps[len(seatMaps)-1]:
    for seat in seatRow:
        if seat == occupiedSeat:
            seatsOccupied += 1
print(seatsOccupied, 'seats occupied')
