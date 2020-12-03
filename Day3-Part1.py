import math

with open('Day3-Part1-Input.txt') as f:
    inputs = f.readlines()

# Remove \n and add 10 columns
rows = list(map(lambda x: x.replace('\n', ''), inputs))
print(len(rows), 'rows')
print('we move max 7 chars to the right every row, so',
      7 * len(rows), 'chars wide needed')
print('1 column =', len(rows[0]),
      'chars, so we need', (3 * len(rows)) / len(rows[0]), 'cols')
rows = list(map(lambda x: x * math.ceil((3 * len(rows)) / len(rows[0])), rows))

startingPosition = [0, 0]
currentPosition = startingPosition
slope = [3, 1]
treesEncountered = 0

i = 0
for row in rows:
    newRow = list(row)
    if(i == currentPosition[1]):
        if(newRow[currentPosition[0]] == '.'):
            newRow[currentPosition[0]] = '✅'
        else:
            newRow[currentPosition[0]] = '🔴'
            treesEncountered += 1
    newRow = ''.join(newRow)
    print(newRow)
    i += 1
    currentPosition = [currentPosition[0] +
                       slope[0], currentPosition[1] + slope[1]]

print(treesEncountered, 'Trees encountered')
