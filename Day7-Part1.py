import math

with open('Day7-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('.\n', ''), inputs))

# exemple
# rows = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
#         'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#         'bright white bags contain 1 shiny gold bag.',
#         'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#         'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#         'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#         'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#         'faded blue bags contain no other bags.',
#         'dotted black bags contain no other bags.']

bags = {}
for row in rows:
    rowParts = row.split(' bags contain ')
    containerBag = rowParts[0]
    containedBags = rowParts[1].split(', ')
    containedBags = list(map(lambda x: x.replace('no other bags', '').replace(
        ' bags', '').replace(' bag', '').replace('.', '').split(' ', 1), containedBags))
    if(containerBag in bags):
        raise Exception('bag already in')
    bags[containerBag] = containedBags


def findContainersOf(pMyBag):
    containers = []
    for bag in bags:
        for bagContained in bags[bag]:
            if bagContained[0] != '' and bagContained[1] == pMyBag:
                # print(bag, bagContained)
                containers.append(bag)
    return containers


def recursiveFindContainers(pCurrentContainers):
    for bagColor in pCurrentContainers:
        temp = findContainersOf(bagColor)
        for tempItem in temp:
            if tempItem not in pCurrentContainers:
                containerList.append(tempItem)


containerList = ['shiny gold']
recursiveFindContainers(containerList)
print(containerList)
print('nb Bags', len(containerList) - 1)
