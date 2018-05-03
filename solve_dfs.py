import time


def alg(graph, entrance, exit):
    visited = [False for i in range(len(graph))]
    path = []

    print("[*] solving using dfs")
    dfs_time = time.time()

    def dfs(v):
        if graph[v][0] == exit:
            return True

        visited[v] = True

        for i in range(1, len(graph[v])):
            if not visited[graph[v][i]]:
                if dfs(graph[v][i]):
                    path.append(graph[v][0])
                    return True

        return False

    try:
        dfs(entrance)
    except:
        print("maze is simply to big for recursion, use other algorithm")
        return []
    print("solved in", len(path)+1, "steps") # +1 because it lacks exit

    print("[#] finished in", time.time()-dfs_time, "seconds")
    return path
