import math

with open('Day3-Part1-Input.txt') as f:
    inputs = f.readlines()

# Remove \n and add 10 columns
rows = list(map(lambda x: x.replace('\n', ''), inputs))
print(len(rows), 'rows')

startingPosition = [0, 0]
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
treesEncounteredPerSlope = []

for slope in slopes:
    print('we move', slope[0], 'chars to the right every', slope[1], 'row, so',
          slope[0] * (len(rows) / slope[1]), 'chars wide needed')
    print('1 column =', len(rows[0]),
          'chars, so we need',  (slope[0] * (len(rows) / slope[1])) / len(rows[0]), 'cols')
    rowsSlope = list(
        map(lambda x: x * math.ceil((slope[0] * (len(rows) / slope[1])) / len(rows[0])), rows))

    treesEncountered = 0
    currentPosition = startingPosition
    i = 0
    for row in rowsSlope:
        newRow = list(row)
        if(i == currentPosition[1]):
            if(newRow[currentPosition[0]] == '.'):
                newRow[currentPosition[0]] = '✅'
            else:
                newRow[currentPosition[0]] = '🔴'
                treesEncountered += 1
            currentPosition = [currentPosition[0] +
                               slope[0], currentPosition[1] + slope[1]]
        newRow = ''.join(newRow)
        # print(newRow)
        i += 1

    treesEncounteredPerSlope.append(treesEncountered)
    print(treesEncountered, 'Trees encountered for slope', slope)

tEMultiplied = 1
for tE in treesEncounteredPerSlope:
    tEMultiplied = tEMultiplied * tE

print('answer', tEMultiplied)
