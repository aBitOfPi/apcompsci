def degrees(graph):
    return sum(len(neighbors) for neighbors in graph.values())


def connected(graph):
    start_node = list(graph.keys())[0]
    visited = set()

    def grapher(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                grapher(neighbor)


    grapher(start_node)
    return len(visited) == len(graph)


def euler(graph):
    if not (graph):
        return False

    for node, neighbors in graph.items():
        if len(neighbors) % 2 == 1:
            return False
    return True


def userGraph():

    print("Enter the graph as an adjacency list.")
    graph = {}
    print("\nEnter the adjacency list (blank line to stop):")
    while True:
        line = input()
        if not line.strip():
            break
        node, neighbors = line.split(":")
        node = int(node.strip())
        neighbors = list(map(int, neighbors.split(","))) if neighbors.strip() else []
        graph[node] = neighbors
    return graph

inputGraph = userGraph()

degreeSum = degrees(inputGraph)
print(f"Total Degrees: {degreeSum}")


if connected(inputGraph):
    print("Connected")
else:
    print("Not Connected")

if euler(inputGraph):
    print("Eulerian")
else:
    print("Not Eulerian")
