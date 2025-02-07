import heapq
import math

def heuristic(a, b):
    return abs(a - b)

def a_star(adjList, start, goal):
    pq = [(0,start)]
    size = len(adjList)
    distances = {start: 0} 
    prev = [None] * size

    while pq:
        weight_vertice, vertice = heapq.heappop(pq)

        if vertice == goal:
            return rebuild_path(prev, start, goal)

        for neighbor, weight in adjList[vertice]:
            distance = weight_vertice + weight
            if neighbor not in distances or distances[neighbor] > distance:
                distances[neighbor] = distance
                priority = distance + heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))
                prev[neighbor] = vertice

    return None

def rebuild_path(paths, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = paths[current]
        path.append(start)
        return path[::-1]

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
    print(a_star(graph, 0, 6))

main()