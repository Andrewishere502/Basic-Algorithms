import random
from collections import deque, OrderedDict
import os


class Target:
    def __str__(self):
        return "!"


class Player:
    def __init__(self, name, position, target=None):
        self.name = name
        self.position = position  # index of player in grid
        self.target_i = position if target == None else target  # player won't try to move as default
        return

    def __str__(self):
        return "@"
    
    def survey_grid(self, grid):
        # calculate and save movement values for each cell in grid
        self.cell_values = self.calculate_cell_values(grid)
        return
    
    def set_target_i(self, target_i):
        self.target_i = target_i
        return

    def calculate_cell_values(self, grid):
        # Key: index of spot in grid, value is the g and h value
        # of the index.
        cell_values = {i: "+" for i in range(len(grid.cells))}
        # Queue of indecies in grid to calclulate the value for.
        current_is = deque([self.target_i])
        while len(current_is) > 0:
            # Index in grid to calculate movement value.
            i = current_is.popleft()
            # Tiles adjacent to i.
            adj_is = self.get_adj_tiles(i, grid)
            # Only queue i if it's movement value has not been
            # calculated yet, and it is not in the queue.
            for j in adj_is:
                if cell_values[j] == "+" and j not in current_is:
                    current_is.append(j)

            if i == self.target_i:
                # This index is the target, so it has no
                # movement cost to reach itself.
                cell_values[i] = (0, 0)  # g = 0, h = 0
            else:
                # Calculate the sum movement cost to the
                # target through adjacent tiles by creating
                # a dict of movement value keys which reference
                # their index.
                adj_is_values = {sum(cell_values[i]): i for i in adj_is if isinstance(cell_values[i], tuple)}
                if len(adj_is_values) > 0:
                    # Find the lowest total movement cost from the
                    # adjacent tiles. Our goal is to find only the
                    # g value though.
                    best_i_value = min(adj_is_values)
                    # Gets the index of this tile with the lowest
                    # movement cost.
                    best_i = adj_is_values[best_i_value]
                    # Get the g and h components.
                    best_i_g_h = cell_values[best_i]

                    # The real time it would take to move from i
                    # to the target i.
                    g = best_i_g_h[0] + 1

                    # The distance ƒrom i to the target i.
                    x = self.target_i % grid.cols - i % grid.cols
                    y = self.target_i // grid.cols - i // grid.cols
                    h = (x ** 2 + y ** 2) ** 0.5
                    cell_values[i] = (g, h)

        cell_values = {i: round(sum(val), 2) if isinstance(val, tuple) else "+" for i, val in cell_values.items()}
        return cell_values

    def get_adj_tiles(self, pos, grid):
        """Return a list of cells that pos is adjacent to. Takes the
        boarders of the grid into account.

        pos -- index, in cells, to get adjacent tiles to
        cells -- a list of tiles, should be able to become
                 a rectangle
        cols -- number of columns in cells
        rows -- number of rows in cells
        """
        adj_tiles = []

        move = pos - grid.cols  # tile above
        if not pos // grid.cols == 0:  # pos isn't on the top row
            adj_tiles.append(move)

        move = pos + grid.cols  # tile below
        if not pos // grid.cols == grid.rows - 1:  # pos isn't on
                                                   # the bottom row
            adj_tiles.append(move)

        move = pos - 1  # tile left
        if not pos % grid.cols == 0:  # pos isn't on the left col
            adj_tiles.append(move)

        move = pos + 1  # tile right
        if not pos % grid.cols == grid.cols - 1:  # pos isn't on the
                                                  # right col
            adj_tiles.append(move)

        adj_tiles = [move for move in adj_tiles if grid.cells[move] != "+"]
        return adj_tiles

    def get_valid_moves(self, grid):
        """Return a list of indicies in grid.cells that the player
        could move to.

        grid -- the grid object in which player is located
        """
        valid_moves = self.get_adj_tiles(self.position, grid)
        return valid_moves  # indicies in grid that player can move to

    def choose_move(self, grid):
        if self.position == self.target_i:
            return None

        # all available moves for player, a move corresponds to the
        # index of a tile in the grid
        valid_moves = self.get_valid_moves(grid)

        # movement values for each valid move
        #
        # NOTE: the index of the movement value corresponds to the
        # tile of the valid move
        valid_move_values = [self.cell_values[i] for i in valid_moves if self.cell_values[i] != "+"]
        # in this case, the player has no where to move
        if len(valid_move_values) == 0:
            return None

        # value of the best move
        best_move_value = min(valid_move_values)

        # the index of the valid move in valid_moves with the best
        # movement cost
        best_move_index = valid_move_values.index(best_move_value)

        # the best move the player can make
        best_move = valid_moves[best_move_index]
        return best_move
    
    def move(self, move_to):
        self.position = move_to
        return


class Grid:
    def __init__(self, cols, rows, target_i, player_i):
        self.cols = cols
        self.rows = rows

        self.cells = ["." if random.randint(0, 2) else "+" for _ in range(cols * rows)]
        # self.cells = ["." for _ in range(cols * rows)]
        # row = 3
        # for i in range(cols - 2):
        #     self.cells[(row - 1) * cols + i] = "+"

        self.cells[target_i] = Target()

        player = Player("alice", player_i, target_i)
        player.survey_grid(self)
        self.player_i = player_i
        self.cells[player_i] = player
        return

    def tick(self):
        self.move_player()
        return

    def move_player(self):
        player = self.cells[self.player_i]  # don't pop yet!
        player_move = player.choose_move(self)
        if player_move != None:
            self.cells.pop(self.player_i)
            self.cells.insert(self.player_i, ".")
            self.cells[player_move] = player

            self.player_i = player_move

            player.move(player_move)
        return


def draw_grid(cells, cols):
    on_col = 0
    pad = max(set([len(str(cell)) for cell in cells]))
    for cell in cells:
        print("|" + " " + str(cell) + " " * (pad - len(str(cell))) + " ", end="")
        on_col += 1
        if on_col == cols:
            print("|")
            on_col = 0
    return


width = 23
height = 35
target_i = width + 1
player_i = width * (height - 1) - 2
grid = Grid(width, height, target_i, player_i)

while True:
    os.system("clear")
    draw_grid(grid.cells, grid.cols)
    print("-" * 50)
    print("n) next")
    print("v) view movement value tiles")
    print("r) reset")
    print("qq) quit")
    action = input("> ").lower().strip()

    if action == "qq":
        quit("Goodbye :)")
    elif action.count("n") == len(action):
        for _ in range(len(action)):
            grid.tick()
    elif action == "v":
        os.system("clear")
        # Visualize the way the @ sees the grid:
        draw_grid(grid.cells[grid.player_i].cell_values.values(), grid.cols)
        input("Return to continue")
    elif action == "r":
        grid = Grid(width, height, target_i, player_i)
