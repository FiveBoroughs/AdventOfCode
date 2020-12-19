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
    def __init__(self, order, direction, x, y):
        self.order = order
        self.direction = direction
        self.x = x
        self.y = y

    def __repr__(self):
        return 'X'+str(self.x)+' | Y'+str(self.y)+' | dir '+self.direction

#Initial pos
positions = [Position(0,east,0,0)]

for move in rows:
    currentPosition = positions[len(positions)-1]
    direction = move[0]
    amount =int(move[1:])
    print(currentPosition, '| move', direction, amount)

    newPosition = Position(currentPosition.order+1, currentPosition.direction, currentPosition.x, currentPosition.y)
    if direction == north : 
        newPosition.x += amount
    if direction == south:
        newPosition.x -= amount
    if direction == east:
        newPosition.y += amount
    if direction == west:
        newPosition.y -= amount
    
    if direction == right:
        newDirectionAngle = int(amount / 90)
        currentDirection = [north, east, south, west].index(currentPosition.direction)
        nextDirectionAngle = currentDirection+newDirectionAngle if currentDirection+newDirectionAngle <= 3 else currentDirection+newDirectionAngle-4  
        nextDirection = [north, east, south, west][nextDirectionAngle]
        newPosition.direction = nextDirection
    if direction == left:
        newDirectionAngle = int(amount / 90)
        currentDirection = [north, east, south, west].index(currentPosition.direction)
        nextDirectionAngle = currentDirection-newDirectionAngle if currentDirection-newDirectionAngle >= 0 else currentDirection-newDirectionAngle+4  
        nextDirection = [north, east, south, west][nextDirectionAngle]
        newPosition.direction = nextDirection
    
    if direction == forward:
        if currentPosition.direction == north : 
            newPosition.x += amount
        if currentPosition.direction == south:
            newPosition.x -= amount
        if currentPosition.direction == east:
            newPosition.y += amount
        if currentPosition.direction == west:
            newPosition.y -= amount

    positions.append(newPosition)

lastPosition = positions[len(positions)-1]
res = abs(lastPosition.x)+abs(lastPosition.y)
print(lastPosition, ' || Manhattan distance', res)
