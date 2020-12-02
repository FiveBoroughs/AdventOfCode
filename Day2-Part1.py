import json
with open('Day2-Part1-input.json') as f:
    inputs = json.load(f)

uncorruptedPasswords = []

for inputItem in inputs:
    [condition, password] = inputItem.split(': ')
    [conditionAmount, conditionContent] = condition.split(' ')
    [conditionAmountMin, conditionAmountMax] = conditionAmount.split('-')

    conditionOccurences = [i for i in range(
        len(password)) if password.startswith(conditionContent, i)]
    if len(conditionOccurences) < int(conditionAmountMin) or len(conditionOccurences) > int(conditionAmountMax):
        print('🔴', conditionContent, conditionAmountMin + ' >=',
              len(conditionOccurences), '<= ' + conditionAmountMax, password)
    else:
        print('✅', conditionContent, conditionAmountMin + ' >=',
              len(conditionOccurences), '<= ' + conditionAmountMax, password)
        uncorruptedPasswords.append(password)

print(len(uncorruptedPasswords))
