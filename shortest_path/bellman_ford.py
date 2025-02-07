import heapq
import math

def bellman_ford(adjList, start):
    size = len(adjList)
    distances = [math.inf] * size
    distances[start] = 0
    prev = [None] * size
    
    for _ in range(len(adjList) - 1):
        for i in range(len(adjList)):
            for neighbor, weight in adjList[i]:
                distance = distances[i] + weight
                if distances[neighbor] > distance:
                    distances[neighbor] = distance
                    prev[neighbor] = i

    print(distances)
    for i in range(len(adjList)):
            for neighbor, weight in adjList[i]:
                distance = distances[i] + weight
                if distances[neighbor] > distance:
                    print(i)
                    print(neighbor)
                    return None

    return distances, prev

def main():
    graph = [
        [(1, 5), (2, 9),(3, 10)],   
        [(0, 5), (2, -3), (4, 2)],  
        [(1, 3), (5, 8)],    
        [(0, 10), (6, -4)],    
        [(1, 2), (7, 6)],     
        [(2, 8), (7, 1)],     
        [(3, 4)],             
        [(4, 6), (5, 1)]      
    ]

    graph2 = [
    [(1, 1)],  # Nodo 0 → (1, peso 1)
    [(2, -1)], # Nodo 1 → (2, peso -1)
    [(3, -1)], # Nodo 2 → (3, peso -1)
    [(1, -1)]  # Nodo 3 → (1, peso -1)
]
    print(bellman_ford(graph2, 0))

main()