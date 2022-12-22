from collections import deque
from colored import fg, bg, attr

with open('in.txt', 'r') as f:
    lines = f.readlines()

#parse input into 2d grid
grid = []
for line in lines:
    grid.append([x for x in line.strip()])

for row in grid:
    for r in row:
        #replace string with int
        ind = row.index(r)
        row[ind] = ord(r)
    #print(row)

#implement BFS to find shortest path from the cell with 83 to the cell with 69
# can only move from cell A to cell B if A - B > -2

start = (0,0)
graph = {}
for i in range (0,len(grid)):
    for j in range(0,len(grid[i])):
        graph[(i,j)] = []
#convert the grid to a graph dictionary
for i in range (0,len(grid)):
    for j in range(0,len(grid[i])):
        # neighbour to the north
        if grid[i][j] == 69:
            goal = (i,j)
            grid[i][j] = ord('z')
        if grid[i][j] == 83:
            start = (i,j)
            grid[i][j] = ord('a')
for i in range (0,len(grid)):
    for j in range(0,len(grid[i])):
        if i > 0:
            if grid[i][j] - grid[i-1][j] > -2:
                graph[(i,j)].append((i-1,j))
        # neighbour to the south
        if i < len(grid)-1:
            if grid[i][j] - grid[i+1][j] > -2:
                #print((i,j), 'with value', grid[i][j]  ,'is neighbours with ', (i+1,j), 'with value', grid[i+1][j])
                graph[(i,j)].append((i+1,j))
        # neighbour to the west
        if j > 0:
            if grid[i][j] - grid[i][j-1] > -2:
                graph[(i,j)].append((i,j-1))
        # neighbour to the east
        if j < len(grid[i])-1:
            if grid[i][j] - grid[i][j+1] > -2:
                graph[(i,j)].append((i,j+1))

def breadth_first_search(graph, root, goal):
    """
    Find the shortest path from the root node to the goal node in a graph
    using breadth-first search.

    Args:
    graph: a dictionary representing the graph, where the keys are the nodes
           and the values are a list of the node's neighbors.
    root: the node at which to start the search.
    goal: the node at which to end the search.

    Returns:
    A dictionary containing the predecessor of each node in the search.
    """
    predecessor = {root: None}    # store the predecessor of each node
    queue = deque([root])    # use a queue to store the nodes to visit

    while queue:
        node = queue.popleft()
        if node == goal:    # return the predecessor dictionary if the goal is reached
            return predecessor

        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in predecessor:
                predecessor[neighbor] = node
                queue.append(neighbor)

    return predecessor
#print('goal ', goal)
#print('graph', graph)
shortest_path = []
node = 'F'

# reconstruct the shortest path from the predecessor dictionary
predecessor = breadth_first_search(graph, start, goal)
shortest_path = []
node = goal
while node is not None:
    shortest_path.append(node)
    node = predecessor[node]
shortest_path.reverse()
print('shortest path part 1')
print(len(shortest_path) - 1)  
#print(shortest_path)
#print the shortest path colored in on the grid
# for i in range(0, len(grid)):
#     for j in range(0, len(grid[i])):
#         if (i,j) in shortest_path:
#             #print(fg('green') + chr(grid[i][j]) + attr('reset'), end='')
#         else:
#             #print(chr(grid[i][j]), end='')
    #print()

#part 2 - find the shortest path from all squares that have value ord(a) to the goal

paths = []
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == ord('a'):
            #print('checking path starting from', (i,j))
            cstart = (i,j)
            cpredecessor = breadth_first_search(graph, cstart, goal)
            shortest_path = []
            node = goal
            if node not in cpredecessor:
                continue
            else:
                while node is not None:
                    #print(node)
                    shortest_path.append(node)
                    node = cpredecessor[node]
                shortest_path.reverse()
                paths.append(len(shortest_path) - 1)

print('part 2')
print(min(paths))
