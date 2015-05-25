import json
class DirectedGraph:

    def __init__(self):
        self.graph = {} #dictionary with elements nodes:[edges]

    def get_graph(self):
        return self.graph

    def add_node(self,node_a):
        self.__graph[node_a]=[]

    def add_edge(self, node_a, node_b):
        if node_b not in self.__graph:
            self.__graph = self.__graph + {node_b:[]}
        if node_a not in self.__graph:
            self.__graph = self.__graph + {node_a: [node_b]}
        else:
            self.__graph[node_a].append(node_b)

    def get_neighbors_for(self, node):
        return self.__graph[node]

    def path_between(self, node_a, node_b):
        return node_b in self.__graph[node_a]






