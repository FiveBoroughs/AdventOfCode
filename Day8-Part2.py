import math

with open('Day8-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

# Exemple
# rows = ['nop + 0',
#         'acc + 1',
#         'jmp + 4',
#         'acc + 3',
#         'jmp - 3',
#         'acc - 99',
#         'acc + 1',
#         'jmp - 4',
#         # 'nop - 4',
#         'acc + 6']


def flipOp(pOp):
    if pOp == 'nop':
        return 'jmp'
    if pOp == 'jmp':
        return 'nop'
    return pOp


instructions = []
index = 0
for row in rows:
    op = row.split(' ', 1)[0]
    if op not in ['acc', 'jmp', 'nop']:
        raise Exception('invalid operator')
    [argSig, argVal] = row.split(' ', 1)[1].split(' ')
    if argSig not in ['+', '-'] or not argVal.isdigit():
        raise Exception('invalid argument')
    instructions.append([index, op, argSig, argVal])
    index += 1

for offset in range(len(instructions)):
    accumulator = 0
    nextStep = instructions[0]
    stepCounter = []
    while nextStep:
        index = nextStep[0]
        op = nextStep[1] if offset != index else flipOp(nextStep[1])
        argSig = nextStep[2]
        argVal = int(nextStep[3])

        if len([x for x in stepCounter if x == index]) > 0:
            print('infinite loop, instruction %s has already been executed. Final accumulation %s' % (
                index, accumulator))
            break

        if op == 'jmp':
            if argSig == '+':
                try:
                    nextStep = list(
                        filter(lambda x: x[0] == index + argVal, instructions))[0]
                except:
                    print(index, '|',  op, argSig, argVal, '|',
                          accumulator, '|', len(stepCounter), '✅')
                    exit()
            if argSig == '-':
                try:
                    nextStep = list(
                        filter(lambda x: x[0] == index - argVal, instructions))[0]
                except:
                    print(index, '|',  op, argSig, argVal, '|',
                          accumulator, '|', len(stepCounter), '✅')
                    exit()
        else:
            if op == 'acc':
                if argSig == '+':
                    accumulator += argVal
                else:
                    accumulator -= argVal
            try:
                nextStep = list(
                    filter(lambda x: x[0] == index + 1, instructions))[0]
            except:
                print(index, '|',  op, argSig, argVal, '|',
                      accumulator, '|', len(stepCounter), '✅')
                exit()

        # print(index, '|',  op, argSig, argVal, '|',
        #       accumulator, '|', len(stepCounter))
        stepCounter.append(index)
