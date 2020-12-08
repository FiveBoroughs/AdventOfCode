import math

with open('Day7-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('.\n', ''), inputs))

# exemple
rows = ['shiny gold bags contain 2 dark red bags.',
        'dark red bags contain 2 dark orange bags.',
        'dark orange bags contain 2 dark yellow bags.',
        'dark yellow bags contain 2 dark green bags.',
        'dark green bags contain 2 dark blue bags.',
        'dark blue bags contain 2 dark violet bags.',
        'dark violet bags contain no other bags.']

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


def findContainedOf(pMyBag):
    return bags[pMyBag]


def recursiveFindContained(pCurrentContained):
    newContainedList = []
    for contained in pCurrentContained:
        temp = findContainedOf(contained[1])
        for tempItem in temp:
            if tempItem[0] != '' and tempItem not in pCurrentContained:
                newContainedList.append(tempItem)
    for listItem in newContainedList:
        print(pCurrentContained, '👉', listItem)
        recursiveFindContained([listItem])
    return newContainedList


containedList = [['1', 'shiny gold']]
containedList = recursiveFindContained(containedList)
print(containedList)

total = 0
for item in containedList:
    total = total +

# Fail
