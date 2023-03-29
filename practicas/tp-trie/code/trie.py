import linkedlist as linkedlist


class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


# Descripción: insert un elemento en T, siendo T un Trie.
# Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y
# el valor del elemento (palabra) a  agregar.
# Salida:  No hay salida definida

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

# search(T,element)
# Descripción: Verifica que un elemento se encuentre dentro del Trie
# Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
# Salida: Devuelve False o True  según se encuentre el elemento.


def search(T, element):
    currentNode = T.root
    searchR(currentNode, element)


def searchR(currentNode, element):
    childrenList = currentNode.children
    newNode = linkedlist.getNodeTrie(
        childrenList, linkedlist.searchTrie(childrenList, element[i]))
    if newNode == False:
        return False
    if i == len(element) and newNode.isEndOfWord == True:
        return True
    currentNode = newNode


test = Trie()
insert(test, "Pero")
insert(test, "Perro")
print(search(test, "Perro"))
# print(test.root.children.head.value.children.head.value.children.head.value.children.head.value.isEndOfWord)
# print(test.root.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.children.head.value.isEndOfWord)
# linkedlist.recorrerListaTrie(
#     test.root.children.head.value.children.head.value.children.head.value.children)
