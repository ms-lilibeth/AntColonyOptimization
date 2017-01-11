import random
from collections import defaultdict


# represents nondirected graph
class Graph:
    def __init__(self, filename):
        self._container = defaultdict(lambda : None)
        self.destination = None
        self.start == 1
        self.nodes_num = 0
        self._create_from_file(filename)

        self.pheromone_default_value = 1/self.nodes_num
        self._pheromones = {}
        self.pheromone_vapor_speed = 0.1
        random.seed()
        pass

    def get_node_list(self):
        return [key for key in self._container]

    def _create_from_file(self, filename):
        with open(filename, 'r') as f:
            # Reading nodes num and destination node
            line = f.readline()
            vals = [int(s) for s in line.split() if s.isdigit()]
            self.nodes_num = vals[0]
            self.start = vals[1]
            self.destination = vals[2]

            # Reading list of edges
            for line in f:
                weight = random.randint(1, 10)
                vals = [int(s) for s in line.replace('\n', '').split('-') if s.isdigit()]
                node_from = vals[0]
                node_to = vals[1]
                if node_from not in self._container:
                    self._container[node_from] = defaultdict(lambda : None)
                self._container[node_from][node_to] = weight

            if node_from not in self._pheromones:
                self._pheromones[node_from] = defaultdict(lambda: None)
            self._pheromones[node_from][node_to] = self.pheromone_default_value

    # returns None if the edge does not exist
    def get_weight(self, node_from, node_to):
        return self._container[node_from][node_to]

    def get_adjacent_nodes(self, node_from):
        return self._container[node_from]

    def update_pheromone(self, node_from, node_to, path_len):
        self._pheromones[node_from][node_to] = (1 - self.pheromone_vapor_speed) * \
            self._pheromones[node_from][node_to] + 1/path_len
        if self._pheromones[node_from][node_to] < self.pheromone_default_value:
            self._pheromones[node_from][node_to] = self.pheromone_default_value

    def get_pheromone(self, node_from, node_to):
        return self._pheromones[node_from][node_to]

    def get_denominator(self, pheromone_influence):
        # returns sum(pheromone^pheromone_influence * edge_len^(1 - pheromone_influence) over all edges
        result = 0
        for node_from in self._pheromones:
            result += sum([self._pheromones[node_to]**pheromone_influence *
                           self._container[node_to]**(1-pheromone_influence)
                           if self._container[node_to] is not None and self._pheromones[node_to] is not None else 0
                           for node_to in self._pheromones[node_from]])
        return result
