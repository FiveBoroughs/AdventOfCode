import math

with open('Day6-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

# exemple
# rows = ['abc', '', 'a', 'b', 'c', '', 'ab',
#         'ac', '', 'a', 'a', 'a', 'a', '', 'b', ''] 

groupAnswers = []
draftGroupAnswers = []
for row in rows:
    print(row)

    for char in row:
        if char not in draftGroupAnswers:
            draftGroupAnswers.append(char)

    if row == '':
        # end of group
        print('group', draftGroupAnswers)
        groupAnswers.append(draftGroupAnswers)
        draftGroupAnswers = []

print('all groups', groupAnswers)
counter = 0
for group in groupAnswers:
    print(len(group))
    counter += len(group)
print(counter)
