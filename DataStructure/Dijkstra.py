mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def mydijkstra(graph,start):
    distances={node:float('inf') for node in graph}
    distances[start] = 0
    queue=[]
    heapq.heappush(queue,[distances[start],start])

    while(queue):
        current_distance,current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for adjacent,weight in graph[current_node].items():
            distance = current_distance+weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue,[distance,adjacent])

    return distances

print(mydijkstra(mygraph,'A'))