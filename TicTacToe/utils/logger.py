# utils/logger.py
import logging
from pathlib import Path
from typing import Optional
import sys

class GameLogger:
    """Custom logger for the TicTacToe game."""

    _instance: Optional['GameLogger'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self) -> None:
        """Initialize logging configuration."""
        self.logger = logging.getLogger('TicTacToe')
        self.logger.setLevel(logging.DEBUG)

        # Create logs directory if it doesn't exist
        Path('logs').mkdir(exist_ok=True)

        # File handler for debug logs
        file_handler = logging.FileHandler('logs/game.log')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        # Console handler for info logs
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        console_handler.setFormatter(console_formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message: str) -> None:
        """Log debug message."""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log error message."""
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Log critical message."""
        self.logger.critical(message)

def get_logger() -> GameLogger:
    """Get logger instance."""
    return GameLogger()