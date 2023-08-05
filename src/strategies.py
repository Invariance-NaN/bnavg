import dag
from hillclimb import HillClimbSearchAll

from pgmpy.models.BayesianNetwork import BayesianNetwork
from pgmpy.estimators import HillClimbSearch


def random_networks(data, count):
    nodes = list(data.columns)

    for _ in range(count):
        yield BayesianNetwork(dag.random_dag(nodes))


def hc_path_networks(data, count):
    return HillClimbSearchAll(data).hill_path(tabu_length=0, max_iter=count)


def tabu_path_networks(data, count):
    return HillClimbSearchAll(data).hill_path(tabu_length=100, max_iter=count)


def hc_best_networks(data, count):
    s = HillClimbSearch(data)
    for _ in range(count):
        yield s.estimate(tabu_length=0, show_progress=False)


def tabu_best_networks(data, count):
    s = HillClimbSearch(data)
    for _ in range(count):
        yield s.estimate(tabu_length=100, show_progress=False)
