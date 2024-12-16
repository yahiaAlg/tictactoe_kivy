# main.py
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from views.game_board import GameBoard
from controllers.game_controller import GameController
from utils.logger import setup_logger
from utils.config_manager import load_config

# Configure window and kivy settings
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', True)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class TicTacToeApp(App):
    """Main application class for TicTacToe game."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logger = setup_logger()
        self.config = load_config()
        self.controller = None
        self.game_board = None

    def build(self):
        """Build and return the root widget."""
        # Set window properties
        Window.clearcolor = get_color_from_hex('#ECF0F1')
        Window.minimum_width = 400
        Window.minimum_height = 500

        # Initialize game components
        self.game_board = GameBoard()
        self.controller = GameController(self.game_board)
        
        return self.game_board

    def on_start(self):
        """Called when the application starts."""
        self.logger.info("Application started")
        
    def on_stop(self):
        """Called when the application stops."""
        self.logger.info("Application stopped")
        self.controller.save_game_state()

if __name__ == '__main__':
    TicTacToeApp().run()