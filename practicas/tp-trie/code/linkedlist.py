class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


def add(L, element):
    newNode = Node()
    newNode.value = element
    if L.head == None:
        L.head = newNode
    else:
        newNode.nextNode = L.head
        L.head = newNode


def search(L, element):
    currentNode = L.head
    position = 0
    while currentNode != None:
        if currentNode.value == element:
            return position
        position += 1
        currentNode = currentNode.nextNode
    return


def searchTrie(L, element):
    currentNode = L.head
    position = 0
    while currentNode != None:
        if currentNode.value.key == element:
            return position
        position += 1
        currentNode = currentNode.nextNode
    return


def insert(L, element, position):
    current = L.head
    currentPos = 0
    if position == 0:
        add(L, element)
        return position

    elif position > 0:
        if current == None:
            return
        newNode = Node()
        newNode.value = element

        while current.nextNode != None:
            if currentPos + 1 != position:
                current = current.nextNode
                currentPos += 1
            else:
                newNode.nextNode = current.nextNode
                current.nextNode = newNode
                return position
        current.nextNode = newNode
        return currentPos + 1
    return


def length(L):
    currentNode = L.head
    len = 0
    while currentNode != None:
        len += 1
        currentNode = currentNode.nextNode
    return len


def delete(L, element):
    position = search(L, element)
    if position == None:
        return
    currentNode = L.head
    if position == 0:
        L.head = currentNode.nextNode
        return position
    for i in range(0, position - 1):
        currentNode = currentNode.nextNode
    currentNode.nextNode = currentNode.nextNode.nextNode
    return position


def deleteTrie(L, element):
    position = searchTrie(L, element)
    if position == None:
        return False
    currentNode = L.head
    if position == 0:
        L.head = currentNode.nextNode
        return True
    for i in range(0, position - 1):
        currentNode = currentNode.nextNode
    currentNode.nextNode = currentNode.nextNode.nextNode
    return True


def access(L, position):
    len = length(L)
    currentNode = L.head
    if len > 0 and position <= (len - 1):
        for i in range(0, position):
            currentNode = currentNode.nextNode
        return currentNode.value


def getNode(L, position):
    len = length(L)
    currentNode = L.head
    if position == None:
        return False
    if len > 0 and position <= (len - 1):
        for i in range(0, position):
            currentNode = currentNode.nextNode
        return currentNode


def getNodeTrie(L, position):
    len = length(L)
    currentNode = L.head
    if position == None:
        return False
    if len > 0 and position <= (len - 1):
        for i in range(0, position):
            currentNode = currentNode.nextNode
        return currentNode.value


def update(L, element, position):
    current = L.head
    if position >= 0:
        i = 0
        while current != None and i <= position - 1:
            current = current.nextNode
            i += 1
        if current == None:
            return
        current.value = element
        return position
    return


def move(L, pos_origin, pos_dest):
    # Catching Errors
    len = length(L)
    if pos_origin < 0 or pos_origin > len:
        return
    if pos_dest < 0 or pos_dest > len:
        return
    if pos_dest == pos_origin:
        return

    nodeDisplaced = getNode(L, pos_dest)
    nodeBeforeDisplaced = getNode(L, pos_dest - 1)
    nodeToMove = getNode(L, pos_origin)
    nodeBeforeMoved = getNode(L, pos_origin - 1)
    # Left To Right
    if pos_origin < pos_dest:
        if pos_origin == 0:
            L.head = nodeToMove.nextNode
        else:
            nodeBeforeMoved.nextNode = nodeToMove.nextNode
        nodeToMove.nextNode = nodeDisplaced.nextNode
        nodeDisplaced.nextNode = nodeToMove
    # Right To Left
    else:
        if pos_origin == length(L) - 1:
            nodeBeforeMoved.nextNode = None
        else:
            nodeBeforeMoved.nextNode = nodeToMove.nextNode
        nodeToMove.nextNode = nodeDisplaced
        if pos_dest != 0:
            nodeBeforeDisplaced.nextNode = nodeToMove
        else:
            L.head = nodeToMove
    return pos_origin


def revert(L):
    newL = LinkedList()
    len = length(L)
    current = L.head

    for i in range(len):
        len -= 1
        add(newL, current.value)
        current = current.nextNode
    return newL


def recorrerLista(S):
    currentNode = S.head
    while currentNode != None:
        if (currentNode.nextNode != None):
            print('|', currentNode.value, '|->', end=" ")
        else:
            print('|', currentNode.value, '|-> None')
        currentNode = currentNode.nextNode
    print('')


def recorrerListaTrie(S):
    currentNode = S.head
    while currentNode != None:
        if (currentNode.nextNode != None):
            print('|', currentNode.value.key,
                  currentNode.value.isEndOfWord, '|->', end=" ")
        else:
            print('|', currentNode.value.key,
                  currentNode.value.isEndOfWord, '|-> None')
        currentNode = currentNode.nextNode
    print('')
