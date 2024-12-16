# controllers/game_controller.py
from typing import List
import json
from models.ai_engine import AIEngine
from utils.logger import get_logger

class GameController:
    """Controller managing game logic and state."""

    def __init__(self, game_board):
        self.logger = get_logger()
        self.game_board = game_board
        self.game_board.controller = self
        self.board_state = [''] * 9
        self.current_player = 'X'
        self.ai_engine = AIEngine()
        self.game_history = []
        self.scores = {'X': 0, 'O': 0, 'draw': 0}
        self.load_game_state()

    def handle_move(self, position: int) -> None:
        """Handle player move and trigger AI response."""
        if self._is_valid_move(position):
            # Player move
            self._make_move(position)
            
            # Check game state after player move
            if self._check_game_end():
                return

            # AI move
            self._make_ai_move()
            self._check_game_end()

    def _make_move(self, position: int) -> None:
        """Execute a move on the board."""
        self.board_state[position] = self.current_player
        self.game_board.update_cell(position, self.current_player)
        self.game_history.append(self.board_state.copy())
        self._switch_player()

    def _make_ai_move(self) -> None:
        """Execute AI move."""
        ai_position = self.ai_engine.get_move(self.board_state)
        if ai_position != -1:
            self._make_move(ai_position)

    def _is_valid_move(self, position: int) -> bool:
        """Check if the move is valid."""
        return 0 <= position < 9 and self.board_state[position] == ''

    def _switch_player(self) -> None:
        """Switch current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def _check_game_end(self) -> bool:
        """Check if game has ended and update scores."""
        winner = self.ai_engine._check_winner(self.board_state)
        if winner:
            self.scores[winner if winner != 'draw' else 'draw'] += 1
            self._handle_game_end(winner)
            return True
        return False

    def _handle_game_end(self, winner: str) -> None:
        """Handle game end state."""
        self.logger.info(f"Game ended. Winner: {winner}")
        # Implement win/lose/draw animations and notifications here

    def reset_game(self) -> None:
        """Reset the game state."""
        self.board_state = [''] * 9
        self.current_player = 'X'
        self.game_history = []
        self.game_board.reset_board()

    def set_difficulty(self, difficulty: str) -> None:
        """Set AI difficulty level."""
        self.ai_engine = AIEngine(difficulty)

    def save_game_state(self) -> None:
        """Save game state to file."""
        state = {
            'scores': self.scores,
            'current_game': self.board_state,
            'history': self.game_history
        }
        try:
            with open('game_state.json', 'w') as f:
                json.dump(state, f)
        except Exception as e:
            self.logger.error(f"Error saving game state: {e}")

    def load_game_state(self) -> None:
        """Load game state from file."""
        try:
            with open('game_state.json', 'r') as f:
                state = json.load(f)
                self.scores = state['scores']
                self.board_state = state['current_game']
                self.game_history = state['history']
        except FileNotFoundError:
            self.logger.info("No saved game state found")
        except Exception as e:
            self.logger.error(f"Error loading game state: {e}")