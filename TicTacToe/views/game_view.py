# views/game_board.py
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import ListProperty, ObjectProperty
from kivy.utils import get_color_from_hex

class GameCell(Button):
    """Individual cell in the game board."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = get_color_from_hex('#2C3E50')
        self.background_normal = ''
        self.font_size = '40sp'
        self.position = None

    def animate_placement(self, symbol):
        """Animate symbol placement in the cell."""
        self.opacity = 0
        self.text = symbol
        anim = Animation(opacity=1, duration=0.3)
        anim.start(self)

class GameBoard(GridLayout):
    """Main game board widget."""
    
    cells = ListProperty([])
    controller = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.spacing = 5
        self.padding = 10
        self._init_board()

    def _init_board(self):
        """Initialize the game board cells."""
        self.cells = []
        for i in range(9):
            cell = GameCell()
            cell.position = i
            cell.bind(on_release=self._on_cell_press)
            self.cells.append(cell)
            self.add_widget(cell)

    def _on_cell_press(self, instance):
        """Handle cell press events."""
        if self.controller and instance.text == '':
            self.controller.handle_move(instance.position)

    def update_cell(self, position, symbol):
        """Update cell content with animation."""
        cell = self.cells[position]
        cell.animate_placement(symbol)

    def reset_board(self):
        """Reset all cells to empty state."""
        for cell in self.cells:
            cell.text = ''