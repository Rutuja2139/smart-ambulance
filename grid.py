import os
import random

def print_grid(grid):
    os.system('clear' if os.name != 'nt' else 'cls')
    print("\n CURRENT CITY MAP\n")
    for row in grid:
        print(" ".join(str(c) for c in row))

def generate_grid(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    obstacle_count = (rows * cols) // 5
    obstacles = set()
    while len(obstacles) < obstacle_count:
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        obstacles.add((x, y))
    for (x, y) in obstacles:
        grid[x][y] = 1
    return grid

def place_special_points(grid):
    rows, cols = len(grid), len(grid[0])
    doctor = (0, cols - 2)
    police = (rows - 1, 1)
    if grid[doctor[0]][doctor[1]] == 0:
        grid[doctor[0]][doctor[1]] = "D"
    if grid[police[0]][police[1]] == 0:
        grid[police[0]][police[1]] = "P"
    return grid
