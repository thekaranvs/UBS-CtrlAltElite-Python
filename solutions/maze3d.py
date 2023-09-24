def solve_3d_maze(maze):
    rows = len(maze) // 10
    cols = 10

    # Parse the input string into a 2D maze representation
    maze_grid = [[maze[i+j] for j in range(cols)] for i in range(0, rows*cols, cols)]

    start = None
    target = None
    for i in range(rows):
        for j in range(cols):
            if maze_grid[i][j] == 'X':
                target = (i, j, 0)  # Target location at level 0
            elif maze_grid[i][j] in ['^', 'v', '<', '>']:
                start = (i, j, 0)  # Starting location at level 0

    # Define the valid moves based on the maze size
    if rows <= 10 and cols <= 10:
        valid_moves = {'^': (-1, 0, 0), 'v': (1, 0, 0), '<': (0, -1, 0), '>': (0, 1, 0)}
    else:
        valid_moves = {'F': (-1, 0, 0), 'B': (1, 0, 0), 'L': (0, -1, 0), 'R': (0, 1, 0)}

    # Define the rotation directions for accessing different levels
    rotation_directions = {'D': 1, 'U': -1}

    # Initialize the cost and moves
    total_cost = 0
    moves = ""

    curr_pos = start
    while curr_pos != target:
        min_dist = float('inf')
        next_pos = None
        next_move = None

        # Iterate over valid moves and calculate the Manhattan distance to the target
        for move, direction in valid_moves.items():
            new_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1], curr_pos[2] + direction[2])
            if is_valid_move(new_pos, maze_grid):
                dist = manhattan_distance(new_pos, target)
                if dist < min_dist:
                    min_dist = dist
                    next_pos = new_pos
                    next_move = move

        if next_pos:
            # Calculate the cost based on the move and update the total cost
            move_cost = calculate_move_cost(next_move)
            total_cost += move_cost

            # Update the maze grid and current position
            maze_grid[curr_pos[0]][curr_pos[1]] = '#'
            curr_pos = next_pos

            # Update the moves string
            moves += next_move

            # Rotate the maze grid if necessary
            if next_move in rotation_directions:
                rotate_maze_grid(maze_grid, rotation_directions[next_move])

        else:
            # No valid moves found, cannot reach the target
            break

    return {'maze': maze, 'moves': moves}


def is_valid_move(position, maze_grid):
    rows = len(maze_grid)
    cols = len(maze_grid[0])
    x, y, z = position

    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False

    if maze_grid[x][y] == '#':
        return False

    return True


def manhattan_distance(position1, position2):
    x1, y1, _ = position1
    x2, y2, _ = position2
    return abs(x1 - x2) + abs(y1 - y2)


def calculate_move_cost(move):
    if move in ['^', 'v']:
        return 1
    elif move in ['<', '>']:
        return 2
    else:
        return 1


def rotate_maze_grid(maze_grid, direction):
    rows = len(maze_grid)
    cols = len(maze_grid[0])

    if rows <= 10:
        if direction == '^':
            rotated_grid = [list(row) for row in zip(*reversed(maze_grid))]
        elif direction == 'v':
            rotated_grid = [list(row) for row in reversed(list(zip(*maze_grid)))]
        elif direction == '<':
            rotated_grid = [list(row[::-1]) for row in maze_grid]
        elif direction == '>':
            rotated_grid = [list(row) for row in maze_grid[::-1]]
    else:
        if direction == 'F':
            rotated_grid = [list(row) for row in zip(*reversed(maze_grid))]
        elif direction == 'B':
            rotated_grid = [list(row) for row in reversed(list(zip(*maze_grid)))]
        elif direction == 'L':
            rotated_grid = [list(row[::-1]) for row in maze_grid]
        elif direction == 'R':
            rotated_grid = [list(row) for row in maze_grid[::-1]]
        elif direction == 'D':
            rotated_grid = [list(row) for row in zip(*reversed(maze_grid))]
            rotated_grid = [list(row) for row in zip(*reversed(rotated_grid))]
        elif direction == 'U':
            rotated_grid = [list(row) for row in zip(*maze_grid[::-1])]
            rotated_grid = [list(row) for row in zip(*rotated_grid[::-1])]

    for i in range(rows):
        for j in range(cols):
            maze_grid[i][j] = rotated_grid[i][j]

def maze3DEntry(input):
    return solve_3d_maze(input['maze'])
