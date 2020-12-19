import math

with open('Day13-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

#exemple
# rows = ['939',
#     '67,7,x,59,61']

earliestTS = int(rows[0])

busIds = []
for item in rows[1].split(','):
    if item != 'x':
        busIds.append(int(item))
    else:
        busIds.append('x')

result=[]
idxTs = 100005872213234
while len(result) <= 0:
    match = True
    for idxBus in range(len(busIds)):
        if busIds[idxBus] != 'x' and (idxTs+idxBus)%busIds[idxBus] != 0:
            match = False
            break
        # else:
        #     print('ts', idxTs)
        #     print('idxTs+idxBus', idxTs+idxBus, 'busIds[idxBus]', busIds[idxBus])
        #     if busIds[idxBus] != 'x':
        #         print('(idxTs+idxBus)%busIds[idxBus]', (idxTs+idxBus)%busIds[idxBus])
        else:
            if idxBus >20:
                print(idxTs, idxBus, 'matches /', len(busIds)) 

    if match == True:
        result.append(idxTs)
    idxTs +=1

print(result)