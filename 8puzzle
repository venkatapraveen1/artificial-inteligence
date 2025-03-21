import numpy as np
import heapq
class PuzzleState:
    def __init__(self, board, empty_tile, moves=0, previous=None):
        self.board = board
        self.empty_tile = empty_tile
        self.moves = moves
        self.previous = previous
        self.size = int(np.sqrt(len(board)))

    def is_goal(self):
        return self.board == list(range(1, self.size * self.size)) + [0]

    def get_possible_moves(self):
        x, y = self.empty_tile
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                moves.append((new_x, new_y))

        return moves

    def move(self, new_empty_tile):
        new_board = self.board[:]
        x, y = self.empty_tile
        new_x, new_y = new_empty_tile
        new_board[x * self.size + y], new_board[new_x * self.size + new_y] = new_board[new_x * self.size + new_y], new_board[x * self.size + y]
        return PuzzleState(new_board, new_empty_tile, self.moves + 1, self)
    def heuristic(self):
        # Using Manhattan distance as the heuristic
        distance = 0
        for i in range(len(self.board)):
            if self.board[i] != 0:
                target_x = (self.board[i] - 1) // self.size
                target_y = (self.board[i] - 1) % self.size
                current_x = i // self.size
                current_y = i % self.size
                distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance
    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())
def a_star_search(initial_state):
    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return current_state

        closed_set.add(tuple(current_state.board))

        for move in current_state.get_possible_moves():
            new_state = current_state.move(move)

            if tuple(new_state.board) not in closed_set:
                heapq.heappush(open_set, new_state)

    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous
    for state in reversed(path):
        print(np.array(state).reshape(3, 3))

if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # Example initial state
    empty_tile = (2, 0)  # Position of the empty tile (0)
    initial_state = PuzzleState(initial_board, empty_tile)

    solution = a_star_search(initial_state)

    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")
