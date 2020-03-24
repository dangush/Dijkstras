class graph:
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def print_edges(self):
        edges = []
        for node in self.graph_dict:
            for neighbor in self.graph_dict[node]:
                edges.append((node, neighbor[0], neighbor[1]))
        print(edges)
    
    def dijsktra(self, start_node, end_node):
        queue = []
        for node in self.graph_dict:
            if node is not start_node:
                queue.append([node, "INFINITE"])
        print(queue)