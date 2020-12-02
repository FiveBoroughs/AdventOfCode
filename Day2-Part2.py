import json
with open('Day2-Part1-input.json') as f:
    inputs = json.load(f)

uncorruptedPasswords = []

for inputItem in inputs:
    [condition, password] = inputItem.split(': ')
    [conditionPositions, conditionContent] = condition.split(' ')
    [conditionPositionA, conditionPositionB] = conditionPositions.split('-')

    conditionA = password[int(conditionPositionA)-1] == conditionContent
    conditionB = password[int(conditionPositionB)-1] == conditionContent

    if (conditionA or conditionB) and not (conditionA and conditionB):
        print('✅', 'required ' + conditionContent + ' in ' + conditionPositionA + ' or ' + conditionPositionB +
              ' got', password[int(conditionPositionA)-1], password[int(conditionPositionB)-1],  password)
        uncorruptedPasswords.append(password)
    else:
        print('🔴', 'required ' + conditionContent + ' in ' + conditionPositionA + ' or ' + conditionPositionB +
              ' got', password[int(conditionPositionA)-1], password[int(conditionPositionB)-1],  password)

print(len(uncorruptedPasswords))
