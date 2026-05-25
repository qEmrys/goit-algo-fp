import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 5, 'D': 10},
        'C': {'E': 3},
        'D': {'F': 11},
        'E': {'B': 4, 'D': 4},
        'F': {}
    }

    start = 'A'
    distances = dijkstra(graph, start)

    print(f"Найкоротші відстані від вершини '{start}':")
    for node, dist in distances.items():
        print(f"  {start} -> {node}: {dist}")
