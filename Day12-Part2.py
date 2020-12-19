import math

with open('Day12-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

#exemple
# rows = ['F10',
#     'N3',
#     'F7',
#     'R90',
#     'F11']

north = 'N'
south = 'S'
east = 'E'
west = 'W'
left = 'L'
right = 'R'
forward = 'F'

class Position:
    def __init__(self, order, boatX, boatY, waypointX, waypointY):
        self.order = order
        self.boatX = boatX
        self.boatY = boatY
        self.waypointX = waypointX
        self.waypointY = waypointY

    def __repr__(self):
        return 'B X'+str(self.boatX)+' Y'+str(self.boatY)+' | W X'+str(self.waypointX)+' Y'+str(self.waypointY)

#Initial pos
positions = [Position(0,0,0,1,10)]

for move in rows:
    currentPosition = positions[len(positions)-1]
    direction = move[0]
    amount =int(move[1:])
    print(currentPosition, '| move', direction, amount)

    newPosition = Position(currentPosition.order+1, currentPosition.boatX, currentPosition.boatY, currentPosition.waypointX, currentPosition.waypointY)
    if direction == north : 
        newPosition.waypointX += amount
    if direction == south:
        newPosition.waypointX -= amount
    if direction == east:
        newPosition.waypointY += amount
    if direction == west:
        newPosition.waypointY -= amount
    
    if direction == right:
        newDirectionAngle = int(amount / 90)
        northWP = currentPosition.waypointX if currentPosition.waypointX > 0 else 0
        southWP = abs(currentPosition.waypointX) if currentPosition.waypointX < 0 else 0
        eastWP = currentPosition.waypointY if currentPosition.waypointY > 0 else 0
        westWP = abs(currentPosition.waypointY) if currentPosition.waypointY < 0 else 0
        for i in range(newDirectionAngle):
            tempNorthWP = northWP
            northWP = westWP
            westWP = southWP
            southWP = eastWP
            eastWP = tempNorthWP
        newPosition.waypointX = -southWP if southWP > 0 else northWP
        newPosition.waypointY = -westWP if westWP > 0 else eastWP 
    if direction == left:
        newDirectionAngle = int(amount / 90)
        northWP = currentPosition.waypointX if currentPosition.waypointX > 0 else 0
        southWP = abs(currentPosition.waypointX) if currentPosition.waypointX < 0 else 0
        eastWP = currentPosition.waypointY if currentPosition.waypointY > 0 else 0
        westWP = abs(currentPosition.waypointY) if currentPosition.waypointY < 0 else 0
        for i in range(newDirectionAngle):
            tempNorthWP = northWP
            northWP = eastWP
            eastWP = southWP
            southWP = westWP
            westWP = tempNorthWP
        newPosition.waypointX = -southWP if southWP > 0 else northWP
        newPosition.waypointY = -westWP if westWP > 0 else eastWP 
    
    if direction == forward:
        waypointX =  currentPosition.waypointX
        waypointY = currentPosition.waypointY
        newPosition.boatX += waypointX * amount
        newPosition.boatY += waypointY * amount

    positions.append(newPosition)

lastPosition = positions[len(positions)-1]
res = abs(lastPosition.boatX)+abs(lastPosition.boatY)
print(lastPosition, ' || Manhattan distance', res)
