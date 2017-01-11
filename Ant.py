import random


class Ant:
    def __init__(self, graph, current_node, destination, rand_seed=None):
        self._curr_node = current_node
        self._path_len = 0
        self._graph = graph
        self.pheromone_influence = 0.8
        # path influence = 1 - pheromone_influence
        self._path = [current_node]
        self._destination = destination
        self._dead_end = False
        random.seed(rand_seed)

    def move(self):
        if self.is_stopped():
            return

        adj_nodes = self._graph.get_adjacent_nodes(self._curr_node)
        if len(adj_nodes) == 0:
            self._dead_end = True
            print("Warning: dead end! Ant stopped.")

        probabilities = {}  # key - node_to, value - probability
        denominator = self._graph.get_denominator(self.pheromone_influence)
        for n in adj_nodes:
            ph = self._graph.get_pheromone(self._curr_node, n)
            probabilities[n] = (ph**self.pheromone_influence * (1/adj_nodes[n])**(1-self.pheromone_influence))\
                / denominator

        interval_len = sum(probabilities.values())
        r = random.uniform(0, interval_len)
        tmp_sum = 0

        for node in probabilities:
            tmp_sum += probabilities[node]
            if tmp_sum > r:
                move_to = node
                break
        self._path_len += self._graph.get_weight(self._curr_node, move_to)
        # self._graph.update_pheromone(self._curr_node, move_to, self._path_len)
        self._curr_node = move_to
        self._path.append(move_to)

    def get_current_node(self):
        return self._curr_node

    def get_path(self):
        return self._path[:]

    def get_path_length(self):
        return self._path_len

    def is_stopped(self):
        return self._curr_node == self._destination or self._dead_end

    def in_dead_end(self):
        return self._dead_end
