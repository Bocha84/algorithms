import math


def shortest_distance(start, end, graph, distances):
    n = len(graph)
    distance = {node: 0 if node == start else math.inf for node in graph}
    visited = []
    u = start
    while len(visited) < n:
        visited.append(u)
        not_visited = (v for v in graph[u] if v not in visited)
        found = None
        greedy = math.inf
        for v in not_visited:
            new_distance = distance[u] + distances[u, v]
            if new_distance < greedy:
                greedy = new_distance
                found = v
        distance[found] = greedy
        u = found

    return distance[end]
