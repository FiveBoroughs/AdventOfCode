import math

with open('Day10-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

preambleLength = 25
lookBackLength = 25

# Exemple
rows = ['28',
        '33',
        '18',
        '42',
        '31',
        '14',
        '46',
        '20',
        '48',
        '47',
        '24',
        '23',
        '49',
        '45',
        '19',
        '38',
        '39',
        '11',
        '1',
        '32',
        '25',
        '35',
        '8',
        '17',
        '7',
        '9',
        '4',
        '2',
        '34',
        '10',
        '3']

# Adapters is [value]
adapters = []
for i in range(len(rows)):
    adapters.append(int(rows[i]))
print(adapters)

startJolts = 0
currentJolts = startJolts
adapters.sort(reverse=True)
deviceJots = adapters[0] + 3
builtInAdapter = deviceJots
adapters.append(builtInAdapter)
lowerInputJolts = 3
adapters.sort()

usedAdapters = []
# while currentJolts not in [deviceJots - x for x in range(1, lowerInputJolts+1)]:
# for adapter in adapters:
#     adapterInputRange = [adapter[1] -
#                          x for x in range(1, lowerInputJolts+1)]
#     if currentJolts in adapterInputRange:
#         print('Adding adapter', adapter, 'to current jolts', currentJolts)
#         usedAdapters.append([adapter, currentJolts])
#         currentJolts = adapter[1]
#     if currentJolts == deviceJots - lowerInputJolts:
#         print('builtin adapter', builtInAdapter,
#               'to current jolts', currentJolts)
#         usedAdapters.append([builtInAdapter, currentJolts])
#         currentJolts = deviceJots
#         break


# print('jolts', currentJolts)
# print(usedAdapters)
# nb1joltDiffAdapters = len(
#     [x for x in usedAdapters if x[0][1] - x[1] == 1])
# nb3joltDiffAdapters = len(
#     [x for x in usedAdapters if x[0][1] - x[1] == 3])
# print('1 jolt diff adapters', nb1joltDiffAdapters)
# print('3 jolt diff adapters', nb3joltDiffAdapters)
# print('result', nb1joltDiffAdapters*nb3joltDiffAdapters)

def find_paths(remaining):
    print('start path', remaining)
    paths = []
    if remaining == 0:
        print('end path', remaining)
        paths.append([])
    for step in range(1, 3+1):
        if step <= remaining:
            subpaths = find_paths(remaining - step)
            for subpath in subpaths:
                print('found subpath', subpath, 'for', remaining)
                paths.append([step] + subpath)
    print('returning', paths, 'for', remaining)
    return paths


def find_paths_2(pRemaining):
    print('start path', pRemaining)
    paths = []
    if len(pRemaining) == 0:
        print('end path', pRemaining)
        paths.append([])
    for step in [x for x in adapters if x in [pRemaining[0] + y for y in range(1, lowerInputJolts+1) if len(pRemaining) > 0]]:
        subpaths = find_paths_2(pRemaining[pRemaining.index(step)+1:])
        for subpath in subpaths:
            print('found subpath', subpath, 'for', pRemaining)
            paths.append([step] + subpath)
    print('returning', paths, 'for', pRemaining)
    return paths


def myFindPath(pCurrentPath):
    print('start path', pCurrentPath)
    paths = []
    nextPaths = [x for x in adapters if x in [
        pCurrentPath[len(pCurrentPath) - 1] + y for y in range(1, lowerInputJolts+1)]]
    if len(nextPaths) == 0:
        print('end path', pCurrentPath)
        paths.append(pCurrentPath)
    for nextPath in nextPaths:
        pCurrentPath.append(nextPath)
        subpaths = myFindPath(pCurrentPath)
        for subpath in subpaths:
            print('found subpath', subpath, 'for', pCurrentPath)
            paths.append(subpath)
    return paths


def findPath(currentPath):
    # print(currentPath)
    nextPaths = [x for x in adapters if x in [
        currentPath[len(currentPath) - 1] + y for y in range(1, lowerInputJolts+1)]]
    if len(nextPaths) == 0:
        finalPaths.append(currentPath)
        # print('end', currentPath)
    if len(nextPaths) > 1:
        print('split', currentPath, nextPaths)
    for nextPath in nextPaths:
        currentPath.append(nextPath)
        findPath(currentPath)


# test = find_paths(4)
test2 = find_paths_2(adapters)
# test3 = myFindPath([adapters[0]])
# for t2 in test2:
print(len(test2))

# for adapter in adapters:
# paths = [x for x in adapters if x[1] in [
#     adapter[1] + y for y in range(1, lowerInputJolts+1)]]
# print(adapter, paths)
# finalPaths = []
# findPath([adapters[0]])
# print('res', len(finalPaths))
# for fin in finalPaths:
#     print(fin)
# groupby(finalPaths[0], lambda: x: x == 22)
