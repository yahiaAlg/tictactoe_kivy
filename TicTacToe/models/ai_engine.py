# models/ai_engine.py
import random
from typing import List, Tuple, Optional
import math

class AIEngine:
    """AI engine implementing minimax algorithm with alpha-beta pruning."""
    
    def __init__(self, difficulty: str = 'medium'):
        self.difficulty = difficulty
        self.max_depth = {
            'easy': 1,
            'medium': 3,
            'hard': 9
        }.get(difficulty, 3)
        self.ai_symbol = 'O'
        self.player_symbol = 'X'

    def get_move(self, board: List[str]) -> int:
        """Get the next move based on current difficulty level."""
        if self.difficulty == 'easy':
            return self._get_random_move(board)
        elif self.difficulty == 'medium':
            return self._get_medium_move(board)
        else:
            return self._get_best_move(board)

    def _get_random_move(self, board: List[str]) -> int:
        """Generate a random valid move."""
        empty_cells = [i for i, cell in enumerate(board) if not cell]
        return random.choice(empty_cells) if empty_cells else -1

    def _get_medium_move(self, board: List[str]) -> int:
        """Implement medium difficulty strategy."""
        # First check for winning move
        winning_move = self._find_winning_move(board, self.ai_symbol)
        if winning_move is not None:
            return winning_move

        # Then check for blocking player's winning move
        blocking_move = self._find_winning_move(board, self.player_symbol)
        if blocking_move is not None:
            return blocking_move

        # Priority positions (center, corners, edges)
        priority_positions = [4, 0, 2, 6, 8, 1, 3, 5, 7]
        for pos in priority_positions:
            if board[pos] == '':
                return pos
        return -1

    def _get_best_move(self, board: List[str]) -> int:
        """Implement minimax algorithm with alpha-beta pruning."""
        best_score = -math.inf
        best_move = -1
        alpha = -math.inf
        beta = math.inf

        for i in range(9):
            if board[i] == '':
                board[i] = self.ai_symbol
                score = self._minimax(board, 0, False, alpha, beta)
                board[i] = ''
                if score > best_score:
                    best_score = score
                    best_move = i
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break

        return best_move

    def _minimax(self, board: List[str], depth: int, is_maximizing: bool, 
                 alpha: float, beta: float) -> float:
        """Minimax algorithm implementation with alpha-beta pruning."""
        result = self._check_winner(board)
        if result is not None:
            return self._get_score(result, depth)
        if depth >= self.max_depth:
            return self._evaluate_board(board)

        if is_maximizing:
            max_eval = -math.inf
            for i in range(9):
                if board[i] == '':
                    board[i] = self.ai_symbol
                    eval = self._minimax(board, depth + 1, False, alpha, beta)
                    board[i] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(9):
                if board[i] == '':
                    board[i] = self.player_symbol
                    eval = self._minimax(board, depth + 1, True, alpha, beta)
                    board[i] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    @staticmethod
    def _check_winner(board: List[str]) -> Optional[str]:
        """Check if there's a winner or draw."""
        # Winning combinations
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != '':
                return board[line[0]]

        if '' not in board:
            return 'draw'
        return None

    def _get_score(self, result: str, depth: int) -> float:
        """Calculate score based on game result and depth."""
        if result == self.ai_symbol:
            return 100 - depth
        elif result == self.player_symbol:
            return -100 + depth
        return 0

    def _evaluate_board(self, board: List[str]) -> float:
        """Evaluate current board state heuristically."""
        score = 0
        # Evaluate each line
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for line in lines:
            score += self._evaluate_line(board, line)
        return score

    def _evaluate_line(self, board: List[str], line: Tuple[int, int, int]) -> float:
        """Evaluate a single line (row, column, or diagonal)."""
        ai_count = sum(1 for i in line if board[i] == self.ai_symbol)
        player_count = sum(1 for i in line if board[i] == self.player_symbol)
        empty_count = sum(1 for i in line if board[i] == '')

        if ai_count == 2 and empty_count == 1:
            return 5
        elif player_count == 2 and empty_count == 1:
            return -5
        return ai_count - player_count