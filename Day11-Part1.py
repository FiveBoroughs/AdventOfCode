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
        seats.append(rows[i][j])
    seatRows.append(seats)
seatMaps.append(seatRows)


def nbAdjascentOccupied(pSeats):
    total = 0
    for tempSeat in range(len(pSeats)):
        if pSeats[tempSeat] == occupiedSeat:
            total += 1
        else:
            break
    return total


def getRange(pSeat, pLeft, pRight):
    if pLeft > 0:
        return list(range(pSeat - pLeft, pSeat))
    if pRight > 0:
        return list(range(pSeat + 1, pSeat + 1 + pRight))
    return [pSeat]


def findAdjascent(pCurrentSeatMap, pSeatRowIndex, pSeatIndex, pUp=0, pDown=0,  pLeft=0, pRight=0):
    print('find start row, seat', pSeatRowIndex, pSeatRowIndex,
          '| Up, down, left , right', pUp, pDown, pLeft, pRight)
    res = []

    # TopLeft
    if pUp > 0 and pLeft > 0:
        for tempUp in getRange(pSeat, pUp, pDown):
            for

    rowsRange = getRange(pSeatRowIndex, pUp, pDown)
    seatsRange = getRange(pSeatIndex, pLeft, pRight)
    print('ranges', rowsRange, seatsRange)

    for tempRowIndex in rowsRange:
        if tempRowIndex >= 0 and tempRowIndex < mapLength:
            for tempSeatIndex in seatsRange:
                if tempSeatIndex >= 0 and tempSeatIndex < rowLength:
                    if
                    print('row', tempRowIndex, 'col', tempSeatIndex, '=',
                          pCurrentSeatMap[tempRowIndex][tempSeatIndex])
                    res.append(
                        pCurrentSeatMap[tempRowIndex][tempSeatIndex])
    return res


# If the map doesn't change, we done
while len(seatMaps) < 2 or seatMaps[len(seatMaps)-1] != seatMaps[len(seatMaps)-2]:
    currentSeatMap = seatMaps[len(seatMaps)-1]
    print('map', len(seatMaps))
    newSeatMap = []
    for seatRowIndex in range(len(currentSeatMap)):
        seatRow = currentSeatMap[seatRowIndex]
        print('row', seatRow)
        newSeatMapRow = []
        for seatIndex in range(len(seatRow)):
            seat = seatRow[seatIndex]
            newSeat = seat

            # If seat is empty and no occupied seats adjacent
            # Seat becomes occupied
            if seat == emptySeat:
                adjacentLeftOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pLeft=1))
                adjacentRightOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pRight=1))
                adjacentUpOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pUp=1))
                adjacentDownOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pDown=1))
                adjacentUpLeftOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pUp=1, pLeft=1))
                adjacentUpRightOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pUp=1, pRight=1))
                adjacentDownLeftOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pDown=1, pLeft=1))
                adjacentDownRightOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pDown=1, pRight=1))

                if (adjacentLeftOccupied == 0 and
                    adjacentRightOccupied == 0 and
                    adjacentUpOccupied == 0 and
                    adjacentDownOccupied == 0 and
                    adjacentUpLeftOccupied == 0 and
                    adjacentUpRightOccupied == 0 and
                    adjacentDownLeftOccupied == 0 and
                    adjacentDownRightOccupied == 0
                    ):
                    newSeat = occupiedSeat

            # If seat is occupied and >4 occupied seats adjacent
            # Seat becomes empty
            if seat == occupiedSeat:
                adjacentLeftOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pLeft=4))
                adjacentRightOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pRight=4))
                adjacentUpOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pUp=4))
                adjacentDownOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pDown=4))
                adjacentUpLeftOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pUp=4, pLeft=4))
                adjacentUpRightOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pUp=4, pRight=4))
                adjacentDownLeftOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pDown=4, pLeft=4))
                adjacentDownRightOccupied = nbAdjascentOccupied(findAdjascent(
                    currentSeatMap, seatRowIndex, seatIndex, pDown=4, pRight=4))

                if adjacentLeftOccupied + adjacentRightOccupied == 4:
                    newSeat = emptySeat

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
