class Graph:
    slots = None
    dic = {}

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.slots = [[] for i in range(len(vertices))]

        for i in range(len(vertices)):
            self.dic[vertices[i]] = i

        for i in edges:
            self.slots[self.dic[i[0]]].append(i[1])
            self.slots[self.dic[i[1]]].append(i[0])


def printGP(G):
    for i in range(len(G.slots)):
        if G.slots[i] == None:
            print("||", G.vertices[i], "|| ---> ", G.slots[i], end=" ")
        else:
            print("||", G.vertices[i], "|| ---> ",
                  [i for i in G.slots[i]], end=" ")
        print("")


vertex = [1, 24, 3, 43, 5, 6]
edges = [[1, 24], [3, 43], [1, 6]]

test = Graph(vertex, edges)
printGP(test)
