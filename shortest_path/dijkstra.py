import heapq
import math

def dijkstra(adjList, start):
    pq = [(0,start)]
    size = len(adjList)
    distances = [math.inf] * size
    distances[start] = 0
    prev = [None] * size

    while pq:
        weight_vertice, vertice = heapq.heappop(pq)
        if weight_vertice > distances[vertice]:
            continue

        for neighbor, weight in adjList[vertice]:
            distance = weight_vertice + weight
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                prev[neighbor] = vertice
    
    return distances, prev

def main():
    graph = [
        [(1, 5), (2, 9),(3, 10)],   
        [(0, 5), (2, 3), (4, 2)],  
        [(1, 3), (5, 8)],    
        [(0, 10), (6, 4)],    
        [(1, 2), (7, 6)],     
        [(2, 8), (7, 1)],     
        [(3, 4)],             
        [(4, 6), (5, 1)]      
    ]
    print(dijkstra(graph, 0))

main()