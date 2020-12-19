import math

with open('Day13-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

#exemple
# rows = ['939',
#     '7,13,x,x,59,x,31,19']

earliestTS = int(rows[0])

busIds = []
for item in rows[1].split(','):
    if item != 'x':
        busIds.append(int(item))

busPasses = []
for ts in range(earliestTS, earliestTS*2):
    tsBuses = []
    for bus in busIds:
        if ts == 0 or ts%bus == 0:
            tsBuses.append(bus)
    if len(tsBuses) > 0:
        busPasses.append([ts, tsBuses])

print(busPasses)

earliestBusPass = busPasses[0]
result = (earliestBusPass[0] - earliestTS) * earliestBusPass[1][0]
print('earliest bus', earliestBusPass, 'result', result)

