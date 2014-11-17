class DirectedGraph():

    def __init__(self, name):

        self.name = name
        self.edges = {}

    def add_edge(self, node_a, node_b):

        if node_b not in self.edges.keys():
            self.edges[node_b] = []
        if node_a not in self.edges.keys():
            self.edges[node_a] = []
            self.edges[node_a].append(node_b)
        else:
            self.edges[node_a].append(node_b)

    def get_neighbors_for(self, node):

        return self.edges[node]

    def path_between(self, node_a, node_b):

        if node_a not in self.edges or node_b not in self.edges:
            return False

        elif node_b in self.get_neighbors_for(node_a):
            return True

        for node in self.get_neighbors_for(node_a):
            if self.path_between(node, node_b):
                return True
        return False

    def __str__(self):

        for edge in self.edges:
            print (edge, self.edges[edge])
