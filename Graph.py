class graph:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def print_edges(self):
        for node in self.graph_dict:
            edges = list()
            for neighbor in self.graph_dict[node]:
                edges.append((neighbor[0], neighbor[1]))
            print("Connected to '" + str(node)+ "':", edges)


    def minDist(self, unvisited, distances):
        minDist = float('inf')
        minDistNode = ""
        for node in unvisited:
            if distances[node][1] < minDist:
                minDistNode = node
                minDist = distances[node][1]
        return minDistNode 

    def dijsktra(self, start_node, end_node):
        visited = set()
        unvisited = set()
        distances = dict()

        #Initialize dict of shortest paths (distances) with start node/0
        #Add start node to unvisited nodes
        #Initialize every other node as unvisited and with a distance of infinity

        distances[start_node] = ["", 0]
        unvisited.add(start_node)
        for node in self.graph_dict:
            if node is not start_node:
                distances[node] = ["", float('inf')]
                unvisited.add(node)

        while end_node not in visited:
            minDistNode = self.minDist(unvisited, distances)
            for i in range(len(self.graph_dict[minDistNode])):
                if self.graph_dict[minDistNode][i][0] in unvisited:
                    neighbor = self.graph_dict[minDistNode][i][0]
                    neighbors_distance = self.graph_dict[minDistNode][i][1]
                    distances[neighbor] = [minDistNode, neighbors_distance]

                visited.add(minDistNode)
            unvisited.remove(minDistNode)
        
        #Now we trace back
        print("\n")
        pointer = end_node
        best_path = list()
        distance = 0
        while pointer != start_node:
            best_path.append(pointer)
            distance += distances[pointer][1]
            pointer = distances[pointer][0]

        #Top it off with the start node
        best_path.append(start_node)
        distance += distances[pointer][1] 

        #Reverse for readability
        best_path.reverse()
        print("Shortest Path: ", best_path)
        print("Total Distance: ", distance)
        


                    