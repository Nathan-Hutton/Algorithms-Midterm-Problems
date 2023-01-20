from itertools import permutations
import math
import numpy as np

class GraphAlgorithms:

    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices and the cost
            '''
            (firstVertex, secondVertex, cost) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            # Update self.adjacencyList with a cost from city i to city j
            # Your code goes here:
            if firstVertex in self.adjacencyList:
                self.adjacencyList[firstVertex][secondVertex] = int(cost)
            else:
                self.adjacencyList[firstVertex] = {secondVertex: int(cost)}

        graphFile.close()

        self.vertices = list(set(self.vertices))
    
    def solve(self):
        min_cost = np.inf # initialize global min_cost as infinity
        min_path = "" # initialize min_path as empty
        # Your code goes here:

        permutation_list = permutations([city for city in self.adjacencyList])
        for permutation in permutation_list:
            cost = 0
            current_city = permutation[0]
            route = [current_city]

            # add next city to route and add cost between current city and next city
            for next_city in permutation[1:]:
                route.append(next_city)
                cost += self.adjacencyList[current_city][next_city]
                current_city = next_city

            route.append(permutation[0])
            cost += self.adjacencyList[current_city][permutation[0]]

            if cost < min_cost:
                min_cost = cost
                min_path = ' '.join(route)

        return min_cost, min_path

if __name__ == '__main__':
    
    g = GraphAlgorithms('vt.txt')
    print(g.solve())
    