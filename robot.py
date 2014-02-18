class robot:
    def __init__(x, y, world_map, goal):
    """
        Input:
            x, y - Starting coordinates of the robot
            world_map - Map of the obstacle course as a 2d array
                'o' - Water
                'x' - Obstacle
                'R', 'W', 'G' - Gate (red, white, and green)
                    [[R o x o o o o o R],
                     [W o x o o x x o W],
                     [G o o o o x x o G]]
            goal - The end gate the robot needs to go to (1, 2, or 3)
    """
        self.x = x
        self.y = y
        self.world_map = world_map
        self.goal = goal
        
    def find_end():
    """
        Output:
            Returns the coordinates of the end gate as a set of lists
    """    
    length = length(self.world_map)
    width = length(self.world_map[0])
    
    if self.goal == 1:
        return world_map[99][width]
    if self.goal == 2:
        return world_map[299][width]
    if self.goal == 3:
        return world_map[499][width]
        
    def algorithm():
    """
        Output:
            Returns a set of positions and velocities for the robot
    """
        pass
    
    def simulation(positions, velocities):
    """
        Input:
            positions - Positions of the robot in the water
            velocities - Velocities of the robot at specific positions
        Output:
            Produces a simulation of the robot, given a specific path
    """
        pass