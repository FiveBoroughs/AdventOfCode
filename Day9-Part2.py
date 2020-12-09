import math

with open('Day9-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

preambleLength = 25
lookBackLength = 25
stackIndex = 631

# Exemple
# rows = ['35',
#         '20',
#         '15',
#         '25',
#         '47',
#         '40',
#         '62',
#         '55',
#         '65',
#         '95',
#         '102',
#         '117',
#         '150',
#         '182',
#         '127',
#         '219',
#         '299',
#         '277',
#         '309',
#         '576']
# preambleLength = 5
# lookBackLength = 5
# stackIndex = 14


def findMultiPreambleSum(pPreambleStack, pStackItem):
    for startPreamble in pPreambleStack:
        sumSinceStartPreamble = startPreamble[1]
        testedPreamble = [startPreamble]
        for i in range(startPreamble[0], len(pPreambleStack)):
            restPreamble = pPreambleStack[i]
            if startPreamble[0] != restPreamble[0]:
                sumSinceStartPreamble += restPreamble[1]
                testedPreamble.append(restPreamble)
                # print(testedPreamble)
                # print(sumSinceStartPreamble)
                if sumSinceStartPreamble > pStackItem[1]:
                    print('overshooting',
                          pStackItem[1], '<', sumSinceStartPreamble)
                    break
                if sumSinceStartPreamble == pStackItem[1]:
                    print('      %s until %s = %s ✅' %
                          (startPreamble[1], restPreamble[1], sumSinceStartPreamble))
                    return testedPreamble
                # else:
                    # print('      %s until %s = %s' %
                    #       (startPreamble[1], restPreamble[1], sumSinceStartPreamble))
    raise Exception('no preamble sum comes to %s' % pStackItem)


# Stack is [index, value]
stack = []
for i in range(len(rows)):
    stack.append([i, int(rows[i])])

stackItem = stack[stackIndex]
print('👉', stackItem)
preambleStack = [x for x in stack if x[0] in range(
    (stackIndex-preambleLength if stackIndex-preambleLength > 0 else 0), stackIndex)]
print(' 👉', preambleStack)
res = findMultiPreambleSum(stack, stackItem)
print(res)
res.sort(key=(lambda x: x[1]))
minVal = res[0][1]
res.sort(key=(lambda x: x[1]), reverse=True)
maxVal = res[0][1]
print('min', minVal, 'max', maxVal, '🎉', minVal+maxVal, )
