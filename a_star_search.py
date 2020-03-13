import sys
from data_structure import readMap, isEmpty, insertInBorder, Node, printPath

# ALGORITHM:

nodeList = readMap()

if(sys.argv.__len__() > 1):
    initialNode = next(node for node in nodeList if node.name == sys.argv[1])
else:
    initialNode = next(node for node in nodeList if node.name == 'L')

initialNode.cost = 0

border = [initialNode]
explored = []

while(True):

    if isEmpty(border):
        raise "Não existe caminho possível"

    currentNode = border.pop()

    print("Cidade atual:", currentNode.name)
    print()

    if(currentNode.isTarget()):
        print("Objetivo encontrado!!!")
        print()
        print("Caminho:", printPath(currentNode))
        print("Custo total:", currentNode.cost)
        print()
        exit(0)

    print("Filhos:", currentNode.children)
    print()

    explored.append(currentNode)

    for childId in currentNode.children:
        child = nodeList[childId]
        print("Analisando cidade", child.name, "...")
        if (child not in explored and child not in border):
            print(child.name, "incluído na borda")
            insertInBorder(child, currentNode, border)
            print()
        elif (child in border and child.cost > child.costFromParent(currentNode)):
            print(child.name, "atualizado com um custo menor")
            border.remove(child)
            insertInBorder(child, currentNode, border)
            print()
        else:
            print(child.name, "já explorado ou incluído.")
            print()

    print("Nova borda:", list(map(Node.getId, border)))
    print()
    print("=====================================")
    print()
