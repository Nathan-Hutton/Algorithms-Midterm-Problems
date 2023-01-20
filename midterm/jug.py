
'''
@author: Jingsai Liang
'''

class jugs():
    def __init__(self, water, capacity, goal):
        self.water = water
        self.capacity = capacity
        self.goal = goal
        self.visited = [] # node has been explored 
        self.child_parent = {} # child is key and parent is value

    def solve(self):    
        node = self.BFS()
        result = []
        # retrieve a path from root to the solution node
        # your code goes here:
        result.append(node)
        while node in self.child_parent:
            node = self.child_parent[node]
            result.insert(0, node)

        return result

    def BFS(self):
        queue = []
        # develop a BFS algorithm based on the instructions 
        # return the node if there is a goal in it
        # your code goes here:
        queue = [self.water]
        self.visited.append(self.water)

        while queue:
            node = queue.pop(0)
            self.visited.append(node)
            if self.goal in node:
                return node

            for i in range(len(node)):
                for j in range(len(node)):
                    if i == j:
                        continue

                    # Check if node[j] can be filled with node[i]
                    if node[j] != self.capacity[j] and self.capacity[j] - node[j] <= node[i]:
                        child = [value for value in node]
                        child[i] -= (self.capacity[j] - child[j])
                        child[j] = self.capacity[j]
                        if tuple(child) not in self.visited:
                            queue.append(tuple(child))
                            self.child_parent[tuple(child)] = node

                    # Check if you can empty node[i] into node[j] even if this doesn't fill node[j] completely
                    if node[j] + node[i] <= self.capacity[j] and node[i] != 0:
                        child = [value for value in node]
                        child[j] += child[i]
                        child[i] = 0
                        if tuple(child) not in self.visited:
                            queue.append(tuple(child))
                            self.child_parent[tuple(child)] = node


if __name__ == '__main__':

    capacity = (8,5,3)
    water = (8,0,0)
    goal = 4

    # another group of values
    # capacity = (9,5,4)
    # water = (9,0,0)
    # goal = 3

    j = jugs(water, capacity, goal)
    print(j.solve())
