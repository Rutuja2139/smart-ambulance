import math
from heapq import heappush, heappop

def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def astar(grid, start, goal, weather_factor):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heappush(open_set, (euclidean(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heappop(open_set)
        if current == goal:
            return path, g
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_g = g + 1 * weather_factor
                new_f = new_g + euclidean((nx, ny), goal)
                heappush(open_set, (new_f, new_g, (nx, ny), path + [(nx, ny)]))
    return None, None
