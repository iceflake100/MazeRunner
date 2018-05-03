import heapq
import time


def alg(graph, entrance, exit):
    path = []

    visited = [False for i in range(len(graph))]
    distance = [9999999999 for i in range(len(graph))]    
    distance[entrance] = 0
    previous = [0 for i in range(len(graph))]


    print("[*] solving using djikstra")
    djikstra_time = time.time()


    # priority queue
    pqueue = []
    heapq.heappush(pqueue, (0, entrance))

    while pqueue:
        # distance and vertex
        d, v = heapq.heappop(pqueue)

        if not visited[v]:
            for i in range(1, len(graph[v])):
                if distance[graph[v][i]] > d + 1:
                    distance[graph[v][i]] = d + 1
                    heapq.heappush(pqueue, (d+1, graph[v][i]))

                    previous[graph[v][i]] = v

                visited[v] = True

    v = previous[exit]
    while not v == entrance:
        path.append(graph[v][0])
        v = previous[v]


    print("solved in", len(path)+2, "steps") # +2 because it lacks entrance and
                                            # exit
    print("[#] finished in", time.time() - djikstra_time, "seconds")

    return path
