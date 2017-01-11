from graph import Graph
from AntColony import AntColony

g = Graph("graph18_1.txt")
colony = AntColony(20, g, g.destination)
result = colony.find_best_path(5)
with open("output.txt", 'w') as f:
    f.write("Min path length: " + str(result[0] + "\n"))
    f.write("Possible paths (node - (weight) - node: \n")
    for path in result[1]:
        for i in range(len(path))-1:
            f.write(str(path[i]) + " - (" + str(g.get_weight(path[i], path[i+1])) +
                    ") - ")
        f.write(str(path[-1]) + "\n")

    f.write("All graph (node-from, node-to: weight): \n")
    n = g.get_node_list()
    for i in n:
        for j in n:
            f.write(str(i) + ', ' + str(j) + ': ' + str(g.get_weight(i, j)))


