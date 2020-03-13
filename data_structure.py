import csv


def isEmpty(collection):
    return collection == None or collection.__len__() == 0


def convertToDistance(string):
    if string is '':
        return None
    return int(string)


def getChildren(distanceList):
    children = []
    index = 0
    for nodeDistance in distanceList:
        if nodeDistance != None and nodeDistance != 0:
            children.append(index)
        index += 1
    return children


def insertInBorder(newNode, parent, border):
    newNode.parent = parent
    newNode.cost = newNode.costFromParent(parent)
    print("- Id:", newNode.id)
    print("- Pai:", newNode.parent.name)
    print("- Custo atual:", newNode.cost)
    print("- Estimativa:", newNode.estimative())
    for node in border:
        # Maintans the border with the best option at the end
        if(node.estimative() <= newNode.estimative()):
            border.insert(border.index(node), newNode)
            return
    border.append(newNode)


class Node:

    cost = None
    children = []
    parent = None

    def __init__(self, id, name, distanceList, straigthDistance=None):
        self.id = id
        self.name = name
        self.distanceList = list(map(convertToDistance, distanceList))
        self.children = getChildren(self.distanceList)
        self.straigthDistance = straigthDistance

    def isTarget(self):
        return self.straigthDistance == 0

    def hasPathTo(self, nodeId):
        return self.distanceList[nodeId] != None

    def distance(self, node):
        return self.distanceList[node.id]

    def estimative(self):
        return self.cost + self.straigthDistance

    def getId(self):
        return self.id

    def costFromParent(self, parent):
        return parent.cost + parent.distance(self)


def printPath(node):
    if(node.parent is None):
        return node.name
    return f'{printPath(node.parent)} -> {node.name}'


def readMap():

    nodeList = []
    nodeCount = 0

    with open('map.csv') as nodeMap:
        csvReader = csv.reader(nodeMap, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                nodeTypeName = row[0]
                row.remove(row[0])
                print(f'{nodeTypeName}: {", ".join(row)}')
            else:
                nodeName = row[0]
                row.remove(row[0])
                nodeList.append(Node(lineCount - 1, nodeName,  row))
            lineCount += 1
        nodeCount = lineCount - 1
        print(f'Total: {nodeCount}')
        print()
        nodeMap.close

    with open('straigthDistance.csv') as straigthDistance:
        csvReader = csv.reader(straigthDistance, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if(lineCount > nodeCount):
                raise "Número diferente de nós."
            nodeList[lineCount].straigthDistance = int(row[0])
            lineCount += 1
        straigthDistance.close

    return nodeList
