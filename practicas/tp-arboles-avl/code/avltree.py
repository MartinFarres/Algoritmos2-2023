class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None


def rotateLeft(tree, node):
    BNode = node.rightnode
    node.rightnode = BNode.leftnode
    if BNode.leftnode is not None:
        BNode.leftnode.parent = node
    BNode.parent = node.parent
    if node.parent is None:
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
    if BNode.rightnode is not None:
        BNode.rightnode.parent = node
    BNode.parent = node.parent
    if node.parent is None:
        tree.root = BNode
    else:
        if node.parent.rightnode == node:
            node.parent.rightnode = BNode
        elif node.parent.leftnode == node:
            node.parent.leftnode = BNode
    BNode.rightnode = node
    node.parent = BNode
    return BNode


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


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.rightnode, level+1)
        print(' ' * 4 * level + '->', node.key, f"(bf={node.bf})")
        print_tree(node.leftnode, level+1)


def insert(B, element, key):
    current = B.root
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if current == None:
        B.root = newNode
        return key
    insertR(newNode, B.root)


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
