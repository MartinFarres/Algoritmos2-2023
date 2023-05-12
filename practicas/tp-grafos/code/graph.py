class Node:
    def __init__(self, vertex, pos, flag1=None):
        self.vertex = vertex
        self.pos = pos
        self.flag1 = flag1


class Graph:
    slots = None
    dic = {}

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.slots = [[] for i in range(len(vertices))]

        for i in range(len(vertices)):
            vertex = Node(vertices[i], i)
            self.dic[vertices[i]] = vertex

        for i in edges:
            vertex1 = self.dic[i[0]]
            vertex2 = self.dic[i[1]]
            self.slots[vertex1.pos].append(vertex2)
            self.slots[vertex2.pos].append(vertex1)

# ------------------------------------ Exercise 2 ---------------------------------


def existPath(G, v1, v2):
    toVisitNodes = [v1]
    nodeV1 = G.dic[toVisitNodes[0]]
    nodeV1.flag1 = "Black"
    while len(toVisitNodes) != 0:
        currentNode = G.dic[toVisitNodes[0]]
        for node in G.slots[currentNode.pos]:
            if node.vertex == v2:
                return True
            if node.flag1 == None:
                toVisitNodes.append(node.vertex)
                node.flag1 = "Grey"
        currentNode.flag1 = "Black"
        toVisitNodes.pop(0)
    return False


# ------------------------------------ Exercise 3 ---------------------------------
def isTree(G):
    if len(G.edges) != len(G.vertices) - 1:
        return False

    visited = {vertex: False for vertex in G.vertices}
    startNode = G.vertices[0]

    if isCyclic(G, startNode, visited):
        return False

    for vertex in G.vertices:
        if not visited[vertex]:
            return False

    return True


# ------------------------------------ Exercise 4 ---------------------------------
def isConnected(G):
    visited = {vertex: False for vertex in G.vertices}
    startNode = G.vertices[0]

    dfs(G, startNode, visited)

    for vertex in G.vertices:
        if not visited[vertex]:
            return False

    return True


# ------------------------------------ Exercise 5 ---------------------------------
def isComplete(G):
    numV = len(G.vertices)
    numE = len(G.edges)

    expected_edges = (numV * (numV - 1)) // 2
    if numE != expected_edges:
        return False

    vertices_with_edges = set()

    for edge in G.edges:
        vertex1, vertex2 = edge
        vertices_with_edges.add(vertex1)
        vertices_with_edges.add(vertex2)

    if len(vertices_with_edges) != numV:
        return False
    return True


# ------------------------------------ Exercise 6 ---------------------------------
def convertTree(G):
    toVisitNodes = [G.vertices[0]]
    edgesToDelete = []
    nodeStart = G.dic[toVisitNodes[0]]
    nodeStart.flag1 = "Grey"
    while len(toVisitNodes) != 0:
        currentNode = G.dic[toVisitNodes[0]]
        for node in G.slots[currentNode.pos]:
            if node.flag1 == None:
                toVisitNodes.append(node.vertex)
                node.flag1 = "Grey"
            elif node.flag1 == "Grey":
                edgesToDelete.append([currentNode.vertex, node.vertex])
        currentNode.flag1 = "Black"
        toVisitNodes.pop(0)
    return edgesToDelete


def countConnections(G):
    visited = {vertex: False for vertex in G.vertices}
    cc = 1
    dfs(G, G.vertices[0], visited)
    for vertex, visit in visited.items():
        if visit == False:
            dfs(G, vertex, visited)
            cc += 1

    return cc


# ------------------------------------ Auxiliar Functions  ---------------------------------


def printGP(G):
    for i in range(len(G.slots)):
        if G.slots[i] == None:
            print("||", G.vertices[i], "|| ---> ", G.slots[i.vertex], end=" ")
        else:
            print("||", G.vertices[i], "|| ---> ",
                  [i.vertex for i in G.slots[i]], end=" ")
        print("")


def dfs(G, vertex, visited):
    if not visited[vertex]:
        visited[vertex] = True
        for adjVertex in G.slots[G.dic[vertex].pos]:
            dfs(G, adjVertex.vertex, visited)


def isCyclic(G, vertex, visited, parent=None):
    visited[vertex] = True

    for adjacentNode in G.slots[G.dic[vertex].pos]:
        adjacentNode = adjacentNode.vertex
        if visited[adjacentNode] == False:
            if isCyclic(G, adjacentNode, visited, vertex):
                return True
        elif adjacentNode != parent:
            return True
    return False


# ------------------------------------ Test ---------------------------------
vertex = [1, 2, 3, 4, 5, 6, 7]
edges = [[1, 2], [1, 3], [2, 4], [7, 5]]

test = Graph(vertex, edges)
print(countConnections(test))
