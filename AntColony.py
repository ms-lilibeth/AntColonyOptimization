from Ant import Ant


class AntColony:
    def __init__(self, size, graph, destination, start=1):
        self._graph = graph
        self._destination = destination
        self._size = size
        self._start = start

    def find_best_path(self, iters_num):
        paths = {}  # key - path length, value - list of paths of this length
        for iteration in range(iters_num):
            ants = [Ant(self._graph, self._start, self._destination, i+iteration) for i in range(self._size)]
            moving_ants = [a for a in ants]
            while len(moving_ants) != 0:
                for ant in moving_ants:
                    ant.move()
                moving_ants = [a for a in moving_ants if not a.is_stopped()]
            finished_ants = [a for a in ants if a.is_stopped() and not a.in_dead_end()]
            ants_in_dead_end = [a for a in ants if a.in_dead_end()]

            for ant in finished_ants:
                lgth = ant.get_path_length()
                if lgth not in paths:
                    paths[lgth] = []
                p = ant.get_path()
                if p not in paths[lgth]:
                    paths[lgth].append(p)

            # Print statistics
            print("Iteration ", iteration, "*************")
            print("    Ants in dead end: ", len(ants_in_dead_end))
            print("    Best path length: ", min(paths))
        min_lgth = min(paths)
        return min_lgth, paths[min_lgth]
