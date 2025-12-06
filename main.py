import time
from datetime import datetime
from astar import astar
from grid import generate_grid, place_special_points, print_grid

def main():
    print("\n SMART AMBULANCE A* SIMULATOR (Dynamic Edition) \n")
    rows = int(input("Enter grid rows (e.g. 6): "))
    cols = int(input("Enter grid columns (e.g. 6): "))
    grid = generate_grid(rows, cols)

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

    grid = place_special_points(grid)

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
