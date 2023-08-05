import predicates
import strategies

from pgmpy.estimators import BDeuScore
from pgmpy.sampling import BayesianModelSampling
from pgmpy.readwrite import BIFReader

import itertools as it
from os import path
from math import exp


def average(pred, graphs, data):
    yes = 0
    total = 0

    scorer = BDeuScore(data)

    for g in graphs:
        score = scorer.score(g)
        score = exp(score)

        total = total + score

        if pred(g):
            yes = yes + score

    return yes / total


def test_network(network, samples=1000):
    print(network.name)

    sampler = BayesianModelSampling(network)
    samples = sampler.forward_sample(samples, show_progress=False)

    node_1, node_2 = it.islice(network.nodes(), 2)
    pred = predicates.has_edge(node_1, node_2, directed=True)

    print("  Actual", pred(network))

    print("  Rand", average(
        pred,
        strategies.random_networks(samples, 100),
        samples
    ))

    print("  Hc_best", average(
        pred,
        strategies.hc_best_networks(samples, 100),
        samples
    ))

    print("  Hc_path", average(
        pred,
        strategies.hc_path_networks(samples, 100),
        samples
    ))

    print("  Tabu_best", average(
        pred,
        strategies.tabu_best_networks(samples, 100),
        samples
    ))

    print("  Tabu_path", average(
        pred,
        strategies.tabu_path_networks(samples, 100),
        samples
    ))


def main():
    earthquake_reader = BIFReader(path.join("networks", "earthquake.bif"))
    mildew_reader = BIFReader(path.join("networks", "mildew.bif"))
    barley_reader = BIFReader(path.join("networks", "barley.bif"))
    diabetes_reader = BIFReader(path.join("networks", "diabetes.bif"))

    earthquake = earthquake_reader.get_model()
    mildew = mildew_reader.get_model()
    barley = barley_reader.get_model()
    diabetes = diabetes_reader.get_model()

    for k in [100, 1000, 1e6]:
        print(f"== {k} ==")
        test_network(earthquake, 100)
        test_network(mildew, 100)
        test_network(barley, 100)
        test_network(diabetes, 100)


if __name__ == "__main__":
    main()
