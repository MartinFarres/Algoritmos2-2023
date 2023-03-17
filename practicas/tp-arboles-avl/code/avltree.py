class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None


# Ejercicio 1

def rotateLeft(tree, node):
    BNode = node.rightnode
    node.rightnode = BNode.leftnode
    if BNode.leftnode != None:
        BNode.leftnode.parent = node
    BNode.parent = node.parent
    if node.parent == None:
        tree.root = BNode
    else:
        if node.parent.rightnode == node:
            node.parent.rightnode = BNode
        elif node.parent.leftnode == node:
            node.parent.leftnode = BNode
    BNode.leftnode = node
    node.parent = BNode
    return BNode


def rotateRight(tree, node):
    BNode = node.leftnode
    node.leftnode = BNode.rightnode
    if BNode.rightnode != None:
        BNode.rightnode.parent = node
    BNode.parent = node.parent
    if node.parent == None:
        tree.root = BNode
    else:
        if node.parent.rightnode == node:
            node.parent.rightnode = BNode
        elif node.parent.leftnode == node:
            node.parent.leftnode = BNode
    BNode.rightnode = node
    node.parent = BNode
    return BNode


# Ejercicio 2

def calculateBalance(tree):
    calculateBalance_R(tree.root)
    return tree


def calculateBalance_R(node):
    if node == None:
        return
    node.bf = height(node.leftnode) - height(node.rightnode)
    calculateBalance_R(node.leftnode)
    calculateBalance_R(node.rightnode)


def height(node):
    if node == None:
        return 0
    rightH = height(node.rightnode)
    leftH = height(node.leftnode)
    return max(rightH, leftH) + 1


# Ejercicio 3


def reBalance(tree):
    calculateBalance(tree)
    reBalance_R(tree, tree.root)
    return tree


def reBalance_R(tree, node):
    if node == None:
        return
    if node.bf > 1:
        if node.leftnode.bf < 0:
            rotateLeft(tree, node.leftnode)
            node = rotateRight(tree, node)
        else:
            node = rotateRight(tree, node)
        calculateBalance(tree)
    elif node.bf < -1:
        if node.rightnode.bf > 0:
            rotateRight(tree, node.rightnode)
            node = rotateLeft(tree, node)
        else:
            node = rotateLeft(tree, node)
        calculateBalance(tree)
    reBalance_R(tree, node.rightnode)
    reBalance_R(tree, node.leftnode)

# Ejercicio 4


def insert(B, element, key):
    current = B.root
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if current == None:
        B.root = newNode
        return key
    insertR(newNode, B.root)
    reBalance(B)


def insertR(newNode, current):
    if newNode.key > current.key:
        if current.rightnode == None:
            current.rightnode = newNode
            newNode.parent = current
            return newNode.key
        insertR(newNode, current.rightnode)
    elif newNode.key < current.key:
        if current.leftnode == None:
            current.leftnode = newNode
            newNode.parent = current
            return newNode.key
        insertR(newNode, current.leftnode)
    else:
        return None


# Ejercicio 5
def delete(B, key):
    current = searchKey(B, key)
    if current == None:
        return
    if current.leftnode == None:
        transplant(B, current, current.rightnode)
    elif current.rightnode == None:
        transplant(B, current, current.leftnode)
    else:
        nodeMin = treeMin(current.rightnode)
        if nodeMin.parent != current:
            transplant(B, nodeMin, nodeMin.rightnode)
            nodeMin.rightnode = current.rightnode
            nodeMin.parent.rightnode = nodeMin
        transplant(B, current, nodeMin)
        nodeMin.leftnode = current.leftnode
        nodeMin.leftnode.parent = nodeMin
    reBalance(B)
    return current.key

# ////////////////////////////////////////////////////////////////////////////////////////
# Funciones Auxiliares


def transplant(B, current, new):
    # Transplanta el nodo 'Current' con el nuevo nodo 'New'
    if current.parent == None:
        B.root = current
    elif current == current.parent.leftnode:
        current.parent.leftnode = new
    else:
        current.parent.rightnode = new
    if new != None:
        new.parent = current.parent


def treeMin(current):
    if current.leftnode == None:
        return current
    else:
        return treeMin(current.leftnode)


def searchKey(B, key):
    current = B.root
    if current.key == key:
        return current
    if current == None:
        return
    return searchKeyR(current, key)


def searchKeyR(node, key):
    if node.key == key:
        return node
    if node.key > key:
        if node.leftnode != None:
            return searchKeyR(node.leftnode, key)
        return
    else:
        if node.rightnode != None:
            return searchKeyR(node.rightnode, key)
        return


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.rightnode, level+1)
        print(' ' * 4 * level + '->', node.key, f"(bf={node.bf})")
        print_tree(node.leftnode, level+1)


# /////////////////////////////////////////////////////////////////////////////////////////////////////
# Test


test = AVLTree()

insert(test, 5, 5)
insert(test, 7, 7)
insert(test, 10, 10)
insert(test, 12, 12)
insert(test, 15, 15)
calculateBalance(test)
print_tree(test.root)
reBalance(test)
print("")
print_tree(test.root)
