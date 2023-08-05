from pgmpy.base import DAG

import networkx.algorithms.dag

import random


def random_dag(nodes):
    # <https://arxiv.org/pdf/cs/0403040.pdf>

    result = DAG()
    result.add_nodes_from(nodes=nodes)

    nodes = list(nodes)

    for _ in range(2 * len(nodes) * len(nodes)):
        x = random.choice(nodes)  # random.randrange(len(nodes))
        y = random.choice(nodes)  # random.randrange(len(nodes))

        if result.has_edge(x, y):
            result.remove_edge(x, y)
        elif x != y:
            result.add_edge(x, y)
            if not networkx.algorithms.dag.is_directed_acyclic_graph(result):
                result.remove_edge(x, y)

    return result
