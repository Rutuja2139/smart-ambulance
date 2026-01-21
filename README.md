# Smart Ambulance A* Simulator (Dynamic Edition)

A real-time pathfinding simulator where an ambulance navigates a dynamic, grid-based city. Environmental factors and obstacles influence movement, demonstrating A* algorithm pathfinding with a Euclidean heuristic.

# Features

- **Dynamic Ambulance Simulation:** The ambulance NPC finds the optimal path to the hospital in real-time.  
- **Dynamic Grid:** Add or remove obstacles on-the-fly. Weather conditions affect movement cost.  
- **Visual Representation:** Real-time paths displayed with clear markers:
  - `A` = Ambulance
  - `H` = Hospital
  - `D` = Doctor
  - `P` = Police
  - `*` = Path  
- Modular Design: Easily extendable for additional NPCs or rules.

# How to Run

1. Clone the repository.  
2. Install Python 3.8+ if not installed.  
3. Run the main simulation:

```bash
python main.py
