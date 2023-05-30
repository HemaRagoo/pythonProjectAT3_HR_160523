### The program should have a name that reflects the adventure’s world.
### The program's world should contain at least 2 locations (if the map is >= 3x3) or 4 locations if the grid equals the map size. Each location should have a unique name, a description, and zero or more objects.
### The player should be able to navigate the world, with options to move North (N), East (E), West (W), and South (S). Available exits should be displayed for each location, and the player can move by typing the corresponding letter.
### There should be at least two different properties of items and/or two characters that the player can interact with. The player should have a "rucksack" or inventory to hold objects.
### The inventory should be able to hold multiple items at a time, with items stored using their unique names. Binary search should be used to search for items.
### The adventure must have at least one conditional action, which can only be performed if a prerequisite is met (e.g., opening a door with a key).
### The adventure should store a simple 2D map in a file, with X's representing visited places and spaces representing unvisited places. Random-access techniques can be implemented for updating the map.
### The adventure must have a specific goal to win the game, with the possibility of losing under certain conditions.
### After winning or losing, players should be able to start a new game.
### The adventure should be developed using an IDE and follow a modular, preferably object-oriented, approach.
### Testing should be done in a useful way, with unit tests and acceptance tests encouraged. Documentation such as docstrings and comments should be included in the code.
### Clear instructions for the player, including how to win the game, should be provided either embedded in the game or in a README.md file.
### The adventure should follow the general gameplay of text adventures, including a starting description, showing available exits, interaction with characters, and simple commands like "look clock" or "get key". Optional features include fixed/not fixed items, visibility, and conditions, and the player's possessions can be listed using the "I" or "Inventory" command.
### The adventure must not include inappropriate jokes, but safe easter eggs are allowed.
### Regular feedback from the student during the assessment process is encouraged.
### The solution should be committed to a GitHub repository with a history of commits.
### The code should be written in Python3, version 3.8 or higher, following PEP 8 guidelines.
### The student's name and ID should be included on the front page of the submission.