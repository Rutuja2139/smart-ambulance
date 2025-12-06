import math
import random
from heapq import heappush, heappop
from datetime import datetime
import os
import time

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


def print_grid(grid):
    os.system('clear' if os.name != 'nt' else 'cls')
    print("\n CURRENT CITY MAP\n")
    for row in grid:
        print(" ".join(str(c) for c in row))


def main():
    print("\n SMART AMBULANCE A* SIMULATOR (Dynamic Edition) \n")
    rows = int(input("Enter grid rows (e.g. 6): "))
    cols = int(input("Enter grid columns (e.g. 6): "))

    
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

  
    obstacle_count = (rows * cols) // 5
    obstacles = set()
    while len(obstacles) < obstacle_count:
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        obstacles.add((x, y))
    for (x, y) in obstacles:
        grid[x][y] = 1

    sx, sy = map(int, input("\nEnter Ambulance Start (x y): ").split())
    gx, gy = map(int, input("Enter Hospital Destination (x y): ").split())
    start = (sx, sy)
    goal = (gx, gy)

  
    print("\nChoose Weather Condition:")
    print("1. Normal\n2. Rain\n3. Fog\n4. Storm")
    choice = int(input("Enter choice (1-4): "))
    weather_conditions = {
        1: ("Normal", 1.0),
        2: ("Rain", 1.3),
        3: ("Fog", 1.6),
        4: ("Storm", 2.0)
    }
    weather, factor = weather_conditions.get(choice, ("Normal", 1.0))

  
    doctor = (0, cols - 2)
    police = (rows - 1, 1)
    if grid[doctor[0]][doctor[1]] == 0:
        grid[doctor[0]][doctor[1]] = "D"
    if grid[police[0]][police[1]] == 0:
        grid[police[0]][police[1]] = "P"

    while True:
      
        temp_grid = [[0 if c == "*" else c for c in row] for row in grid]
        path, cost = astar(temp_grid, start, goal, factor)

        if path:
            for (x, y) in path:
                if (x, y) not in [start, goal] and temp_grid[x][y] == 0:
                    temp_grid[x][y] = "*"
            temp_grid[start[0]][start[1]] = "A"
            temp_grid[goal[0]][goal[1]] = "H"

            print_grid(temp_grid)
            print(f"\nWeather: {weather} | Cost Factor: {factor}")
            print(f"Path Length: {len(path)-1} | Total Cost: {round(cost,2)}")
        else:
            print_grid(grid)
            print("\n No route found! Obstacles may block all paths.")

       
        print("\nActions:")
        print("1. Add obstacle")
        print("2. Remove obstacle")
        print("3. Change weather")
        print("4. Exit simulation")
        action = input("Enter choice: ")

        if action == "1":
            x, y = map(int, input("Enter obstacle coordinates (x y): ").split())
            if (x, y) not in [start, goal]:
                grid[x][y] = 1
                print(" Obstacle added!")
        elif action == "2":
            x, y = map(int, input("Enter coordinates to clear (x y): ").split())
            if grid[x][y] == 1:
                grid[x][y] = 0
                print(" Obstacle removed!")
        elif action == "3":
            print("\nNew Weather:")
            for i, (w, f) in weather_conditions.items():
                print(f"{i}. {w}")
            choice = int(input("Enter choice (1-4): "))
            weather, factor = weather_conditions.get(choice, ("Normal", 1.0))
        elif action == "4":
            print("\n FINAL REPORT")
            print("="*45)
            print(f"Start Location       : {start}")
            print(f"Destination          : {goal}")
            print(f"Weather Condition    : {weather}")
            print(f"Total Obstacles      : {sum(row.count(1) for row in grid)}")
            print(f"Timestamp            : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*45)
            print("✅ Simulation Ended Successfully")
            break

        time.sleep(1)

if __name__ == "__main__":
    main()