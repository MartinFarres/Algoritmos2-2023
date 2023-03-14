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
    node.rightnode.leftnode = node.rightnode
    node.rightnode.parent = None
    node.parent = node.rightnode
    node.rightnode = None
    tree.root = node.parent
    return tree.root


def rotateRight(tree, node):
    node.leftnode.rightnode = node.leftnode
    node.leftnode.parent = None
    node.parent = node.leftnode
    node.leftnode = None
    tree.root = node.parent
    return tree.root


def calculateBalance(tree):
    calculateBalance_R(tree.root)
    return tree


def calculateBalance_R(node):
    if node == None:
        return
    node.bf = (height(node.leftnode) - height(node.rightnode))
    calculateBalance_R(node.leftnode)
    calculateBalance_R(node.rightnode)


def height(node, i):
    if node != None:
        height(node.rightnode, i + 1)
        height(node.leftnode, i + 1)
    return i


def reBalance(tree):
    calculateBalance(tree)
    reBalance_R(tree.root, tree)
    return tree


def reBalance_R(tree, node):
    treeR = AVLTree()
    treeR.root = node
    if node.bf > 1:
        if node.leftnode.bf < 0:
            rotateLeft(treeR, node.leftnode)
            rotateRight(treeR, node)
            calculateBalance(treeR)
            node = treeR.root
            # reBalance_R(tree, node.rightnode)
            # reBalance_R(tree, node.leftnode)
        else:
            rotateRight(treeR)
            node = treeR.root
    elif node.bf < -1:
        if node.rightnode.bf > 0:
            rotateRight(treeR, node.rightnode)
            rotateLeft(treeR, node)
