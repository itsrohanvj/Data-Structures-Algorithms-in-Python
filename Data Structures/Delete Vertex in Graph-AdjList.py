class AdjNode(object):
    def __init__(self, data):
        self.vertex = data
        self.next = None

# Adjacency List representation
class AdjList(object):

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    # Function to add an edge from a source vertex
    # to a destination vertex
    def addedge(self,src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to call the above function.
    def addvertex(self, vk, source, destination):
        graph.addedge(source, vk)
        graph.addedge(vk, destination)

    # Function to print the graph
    def print_graph(self):
        for i in range(self.v):
            print(i, end="")
            temp = self.graph[i]
            while temp:
                print("->", temp.vertex, end="")
                temp = temp.next
            print("\n")

        # Function to delete a vertex

    def delvertex(self, k):

        # Iterating through all the vertices of the graph
        for i in range(self.v):
            temp = self.graph[i]
            if i == k:
                while temp:
                    self.graph[i] = temp.next
                    temp = self.graph[i]

                    # Delete the vertex
            # using linked list concept
            if temp:
                if temp.vertex == k:
                    self.graph[i] = temp.next
                    temp = None
            while temp:
                if temp.vertex == k:
                    break
                prev = temp
                temp = temp.next

            if temp == None:
                continue

            prev.next = temp.next
            temp = None


# Driver code
if __name__ == "__main__":
    V = 6
    graph = AdjList(V)
    graph.addedge(0, 1)
    graph.addedge(0, 3)
    graph.addedge(0, 4)
    graph.addedge(1, 2)
    graph.addedge(3, 2)
    graph.addedge(4, 3)

print("Initial adjacency list")
graph.print_graph()

# Add vertex
graph.addvertex(5, 3, 2)
print("Adjacency list after adding vertex")
graph.print_graph()

# Delete vertex
graph.delvertex(4)
print("Adjacency list after deleting vertex")
graph.print_graph()