import math

with open('Day10-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

preambleLength = 25
lookBackLength = 25

# Exemple
# rows = ['28',
#         '33',
#         '18',
#         '42',
#         '31',
#         '14',
#         '46',
#         '20',
#         '48',
#         '47',
#         '24',
#         '23',
#         '49',
#         '45',
#         '19',
#         '38',
#         '39',
#         '11',
#         '1',
#         '32',
#         '25',
#         '35',
#         '8',
#         '17',
#         '7',
#         '9',
#         '4',
#         '2',
#         '34',
#         '10',
#         '3']

# Adapters is [index, value]
adapters = []
for i in range(len(rows)):
    adapters.append([i, int(rows[i])])
print(adapters)

startJolts = 0
currentJolts = startJolts
adapters.sort(reverse=True, key=(lambda x: x[1]))
deviceJots = adapters[0][1] + 3
builtInAdapter = [-1, deviceJots]
lowerInputJolts = 3
adapters.sort(key=(lambda x: x[1]))

usedAdapters = []
# while currentJolts not in [deviceJots - x for x in range(1, lowerInputJolts+1)]:
for adapter in adapters:
    adapterInputRange = [adapter[1] -
                         x for x in range(1, lowerInputJolts+1)]
    if currentJolts in adapterInputRange:
        print('Adding adapter', adapter, 'to current jolts', currentJolts)
        usedAdapters.append([adapter, currentJolts])
        currentJolts = adapter[1]
    if currentJolts == deviceJots - lowerInputJolts:
        print('builtin adapter', builtInAdapter,
              'to current jolts', currentJolts)
        usedAdapters.append([builtInAdapter, currentJolts])
        currentJolts = deviceJots
        break


print('jolts', currentJolts)
print(usedAdapters)
nb1joltDiffAdapters = len(
    [x for x in usedAdapters if x[0][1] - x[1] == 1])
nb3joltDiffAdapters = len(
    [x for x in usedAdapters if x[0][1] - x[1] == 3])
print('1 jolt diff adapters', nb1joltDiffAdapters)
print('3 jolt diff adapters', nb3joltDiffAdapters)
print('result', nb1joltDiffAdapters*nb3joltDiffAdapters)
