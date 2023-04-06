import linkedlist as linkedlist


class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


# ---------------------------------- Insert ----------------------------------------------------------

def insert(T, element):
    if T.root == None:
        newRoot = TrieNode()
        T.root = newRoot
    currentNode = T.root
    for i in range(0, len(element)):
        childrenList = currentNode.children
        newNode = False
        if childrenList != None:
            newNode = linkedlist.getNodeTrie(
                childrenList, linkedlist.searchTrie(childrenList, element[i]))
        else:
            childrenList = linkedlist.LinkedList()
            currentNode.children = childrenList
        if newNode == False:
            newNode = TrieNode()
            newNode.parent, newNode.key = currentNode, element[i]
            linkedlist.add(childrenList, newNode)
        if i == len(element)-1:
            newNode.isEndOfWord = True
        currentNode = newNode


# ---------------------------------- Search ----------------------------------------------------------

def search(T, element):
    currentNode = T.root
    return searchR(currentNode, element)


def searchR(currentNode, element):
    childrenList = currentNode.children
    newNode = linkedlist.getNodeTrie(
        childrenList, linkedlist.searchTrie(childrenList, element[0]))
    if newNode == False:
        return False
    if len(element) == 1 and newNode.isEndOfWord == True:
        return True
    element = element[1:]
    return searchR(newNode, element)


# ---------------------------------- Delete ----------------------------------------------------------

def delete(T, element):
    currentNode = T.root
    nodeToDelete = [None, None]
    # Searching and saving the last letter that is the end of a word inside the element
    for i in range(0, len(element)):
        childrenList = currentNode.children
        newNode = linkedlist.getNodeTrie(
            childrenList, linkedlist.searchTrie(childrenList, element[i]))
        # Saving the first node to delete if no other is found
        if i == 0:
            nodeToDelete[0], nodeToDelete[1] = newNode, i
        if newNode == False:
            return False
        # Saving node to delete if it isEndOfWord and not the last
        if newNode.isEndOfWord == True and i != len(element):
            nodeToDelete[0], nodeToDelete[1] = newNode, i
        currentNode = newNode
    # Deleting the Node
    if newNode.children == None:  # Last Node of our elemnt has no children, we delete the whole element
        if nodeToDelete[1] == 0:
            linkedlist.deleteTrie(T.root.children, element[0])
            nodeToDelete[0].children = None
        else:
            linkedlist.deleteTrie(
                nodeToDelete[0].children, element[nodeToDelete[1]+1])
            nodeToDelete[0].children = None
    else:
        newNode.isEndOfWord = False
    return True

# ------------------------ Search by Pattern -------------------------------------------------


def searchByPattern(T, p, n):
    currentNode = searchPatternR(T.root, p)
    if currentNode == False:
        return False
    newTree = Trie()
    newTree.root = currentNode
    listWords = printTrie(newTree, p)
    listWords = [i for i in listWords if len(i) == n]
    return listWords


def searchPatternR(currentNode, element):
    childrenList = currentNode.children
    newNode = linkedlist.getNodeTrie(
        childrenList, linkedlist.searchTrie(childrenList, element[0]))
    if newNode == False:
        return False
    if len(element) == 1:
        return newNode
    element = element[1:]
    return searchPatternR(newNode, element)

# ------------------------ Print Words in Trie ----------------------------------------------


def printTrie(T, pattern=""):
    listWords = []
    letters = "" + pattern
    node = T.root
    printTrieR(node.children.head, listWords, letters)
    return listWords


def printTrieR(listNode, listWords,  letters):
    if listNode == None:
        return
    letters = letters + listNode.value.key
    if listNode.value.isEndOfWord == True:
        listWords.append(letters)
    if listNode.value.children != None:
        printTrieR(listNode.value.children.head, listWords, letters)
        letters = letters[:-1]
    return printTrieR(listNode.nextNode, listWords, letters)


# ------------------------------ Tries Iguales --------------------------------------------------

def triesIguales(T, P):
    Tlist = printTrie(T)
    Plist = printTrie(P)
    if Tlist == Plist:
        return True
    return False


# ------------------------------ Palabras Invertidas -----------------------------------------------

# def palInvertidas(T):


test = Trie()
insert(test, "Martin")
insert(test, "Argentina")
insert(test, "Hola")
insert(test, "Holapos")
insert(test, "Holan")
insert(test, "Holanda")

test1 = Trie()
insert(test1, "Hola")
insert(test1, "Holapos")
insert(test1, "Holan")
insert(test1, "Argentina")
insert(test1, "Martin")
insert(test1, "Holanda")

print(printTrie(test))
print(printTrie(test1))
