import math

with open('Day9-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

preambleLength = 25
lookBackLength = 25

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


def findPreambleSum(pPreambleStack, pStackItem):
    for tempA in preambleStack:
        for tempB in preambleStack:
            if tempB[1] != tempA[1]:
                calc = tempA[1] + tempB[1]
                if calc == stackItem[1]:
                    print('      %s + %s = %s ✅' % (tempA[1], tempB[1], calc))
                    return [tempA, tempB]
                else:
                    print('      %s + %s = %s' % (tempA[1], tempB[1], calc))
    raise Exception('no preamble sum comes to %s' % pStackItem)


# Stack is [index, value]
stack = []
for i in range(len(rows)):
    stack.append([i, int(rows[i])])
print(stack)

for stackIndex in range(preambleLength, len(stack)):
    stackItem = stack[stackIndex]
    print('👉', stackItem)

    preambleStack = [x for x in stack if x[0] in range(
        (stackIndex-preambleLength if stackIndex-preambleLength > 0 else 0), stackIndex)]
    print(' 👉', preambleStack)

    preambleSum = findPreambleSum(preambleStack, stackItem)
    print('  👍', preambleSum)
