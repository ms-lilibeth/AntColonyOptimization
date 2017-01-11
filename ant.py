import random


class Ant:
    def __init__(self, graph, current_node):
        self._curr_node = current_node
        self._path_len = 0
        self._graph = graph
        self.pheromone_influence = 0.8
        # path influence = 1 - pheromone_influence

    def move(self):
        adj_nodes = self._graph.get_adjacent_nodes(self._curr_node)
        probabilities = {}
        denominator = self._graph.get_denominator(self.pheromone_influence)
        for n in adj_nodes:
            ph = self._graph.get_pheromone(self._curr_node, n)
            probabilities[n] = (ph**self.pheromone_influence * (1/adj_nodes[n])**(1-self.pheromone_influence))\
                / denominator
        random.seed()
        interval_len = sum(probabilities.values())
        r = random.uniform(0, interval_len)
        tmp_sum = 0

        for i in range(len(probabilities)):
            tmp_sum += probabilities[i]
            if tmp_sum > r:
                move_to = i
                break
        self._path_len += self._graph.get_weight(self._curr_node, move_to)
        self._graph.update_pheromone(self._curr_node, move_to, self._path_len)
        self._curr_node = move_to
