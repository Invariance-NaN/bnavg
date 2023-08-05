def has_edge(node_1, node_2, directed=True):
    def has_directed_edge(g):
        return g.has_edge(node_1, node_2)

    def has_undirected_edge(g):
        return g.has_edge(node_1, node_2) or g.has_edge(node_2, node_1)

    return has_directed_edge if directed else has_undirected_edge
