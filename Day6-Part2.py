import math

with open('Day6-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

# exemple
# rows = ['abc', '', 'a', 'b', 'c', '', 'ab',
#         'ac', '', 'a', 'a', 'a', 'a', '', 'b', '']

groupAnswers = []
draftGroupAnswers = []
groupCommonAnswers = []
for row in rows:
    print(row)
    if row != '':
        # for char in row:
        # if char not in draftGroupAnswers:
        draftGroupAnswers.append([char for char in row])

    else:
        # end of group

        # Merge answers
        flatAnswers = sum(draftGroupAnswers, [])
        commonAnswers = []
        for answer in flatAnswers:
            if flatAnswers.count(answer) == len(draftGroupAnswers) and answer not in commonAnswers:
                commonAnswers.append(answer)

        print('group', draftGroupAnswers)
        print('common answers', commonAnswers)
        groupAnswers.append(draftGroupAnswers)
        groupCommonAnswers.append(commonAnswers)
        draftGroupAnswers = []

print('all groups', groupAnswers)
print('all common answers', groupCommonAnswers)
counter = 0
for group in groupCommonAnswers:
    print(len(group))
    counter += len(group)
print(counter)
