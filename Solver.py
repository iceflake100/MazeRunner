import time
import os
from PIL import Image
import solve_dfs
import solve_dji

def save(filename, path, entrance, exit, algorithm):
    solve = (204, 52, 53)
    point = (57, 129, 237)

    print("[#] generating image")
    saving_time = time.time()

    solved = Image.open(filename)
    solved.mode = 'RGB'
    solved_matrix = solved.load()

    for i in range(len(path)):
        solved_matrix[path[i]] = solve

    solved_matrix[entrance] = point
    solved_matrix[exit] = point

    filename = os.path.splitext(os.path.basename(filename))[0]+algorithm+".png"
    solved.save(filename)

    print("saved", filename)

    print("[#] finished in", time.time()-saving_time, "seconds")


def generate_graph(maze, width, height):
    wall = (0, 0, 0)
    verticies = 0
    edges = 0
    graph = [[] for i in range(width*height)]

    print("[*] generating graph")
    graph_time = time.time()

    for x in range(width):
        for y in range(height):
            if not maze[x, y] == wall:
                verticies += 1

                # vertex's number
                v = x*width+y

                # append position
                graph[v].append((x, y))

                if not x < 1:
                    if not maze[x-1, y] == wall:
                        graph[v].append(v-width)
                        edges += 1
                if x+1 < width:
                    if not maze[x+1, y] == wall:
                        graph[v].append(v+width)
                        edges += 1
                if not y < 1:
                    if not maze[x, y-1] == wall:
                        graph[v].append(v-1)
                        edges += 1
                if y+1 < height:
                    if not maze[x, y+1] == wall:
                        graph[v].append(v+1)
                        edges += 1

    print(verticies, "verticies")
    print(edges, "edges")
    print("[#] finished in", time.time()-graph_time, "seconds")

    return graph

def get_entrance_and_exit(maze, width, height):
    wall = (0, 0, 0)

    entrance = (0, 0)
    exit = (0, 0)

    print("[*] searching for entrance and exit")
    entry_time = time.time()

    for x in range(width):
        if not maze[x, 0] == wall:
            entrance = (x, 0)
            break
    for x in range(width):
        if not maze[x, height-1] == wall:
            exit = (x, height-1)
            break
    for y in range(height):
        if not maze[0, y] == wall:
            entrance = (0, y)
            break
    for y in range(height):
        if not maze[width-1, y] == wall:
            exit = (width-1, y)
            break

    print("found entrance at", entrance)
    print("found exit at", exit)

    print("[#] finished in", time.time()-entry_time, "seconds")

    return entrance, exit

def solve(filename, dfs, dji):
    print("[*] solving", filename)
    solve_time = time.time()

    print("opening image file")

    try:
        maze = Image.open(filename)
    except:
        print("unable to open file, quiting")
        return

    width, height = maze.size
    print("size =", width, "x", height)
    maze.mode = 'RGB'
    maze_matrix = maze.load()

    graph = generate_graph(maze_matrix, width, height)
    entrance, exit = get_entrance_and_exit(maze_matrix, width, height)

    if dfs:
        path = solve_dfs.alg(graph, entrance[0]*width+entrance[1], exit)
        save(filename, path, entrance, exit, "DFS")
    if dji:
        path = solve_dji.alg(graph, entrance[0]*width+entrance[1]
                            , exit[0]*width+ exit[1])
        save(filename, path, entrance, exit, "DJIKSTRA")

    print("[#] finished in", time.time()-solve_time, "seconds")
