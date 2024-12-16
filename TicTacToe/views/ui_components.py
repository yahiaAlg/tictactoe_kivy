# views/ui_components.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex
from kivy.animation import Animation

class GameControls(BoxLayout):
    """Control panel for game settings and actions."""

    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10
        self._init_ui()

    def _init_ui(self):
        """Initialize UI components."""
        # Score display
        self.score_label = Label(
            text='Score: X: 0  O: 0  Draw: 0',
            size_hint_y=None,
            height='40dp'
        )
        self.add_widget(self.score_label)

        # Difficulty selector
        self.difficulty_spinner = Spinner(
            text='Medium',
            values=('Easy', 'Medium', 'Hard'),
            size_hint_y=None,
            height='40dp'
        )
        self.difficulty_spinner.bind(text=self._on_difficulty_change)
        self.add_widget(self.difficulty_spinner)

        # Control buttons
        buttons_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height='40dp',
            spacing=5
        )
        
        self.new_game_btn = CustomButton(
            text='New Game',
            on_press=self._on_new_game
        )
        self.undo_btn = CustomButton(
            text='Undo',
            on_press=self._on_undo
        )
        self.settings_btn = CustomButton(
            text='Settings',
            on_press=self._on_settings
        )

        buttons_layout.add_widget(self.new_game_btn)
        buttons_layout.add_widget(self.undo_btn)
        buttons_layout.add_widget(self.settings_btn)
        self.add_widget(buttons_layout)

    def _on_difficulty_change(self, spinner, text):
        """Handle difficulty change."""
        self.controller.set_difficulty(text.lower())

    def _on_new_game(self, instance):
        """Handle new game button press."""
        self.controller.reset_game()

    def _on_undo(self, instance):
        """Handle undo button press."""
        self.controller.undo_move()

    def _on_settings(self, instance):
        """Handle settings button press."""
        SettingsPopup(self.controller).open()

    def update_score(self, scores):
        """Update score display."""
        self.score_label.text = (
            f"Score: X: {scores['X']}  O: {scores['O']}  "
            f"Draw: {scores['draw']}"
        )

class CustomButton(Button):
    """Styled button for game controls."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = get_color_from_hex('#3498DB')
        self.color = get_color_from_hex('#FFFFFF')
        self.bind(on_press=self._on_press, on_release=self._on_release)

    def _on_press(self, instance):
        """Animate button press."""
        Animation(background_color=get_color_from_hex('#2980B9'), 
                 duration=0.1).start(self)

    def _on_release(self, instance):
        """Animate button release."""
        Animation(background_color=get_color_from_hex('#3498DB'), 
                 duration=0.1).start(self)

class SettingsPopup(Popup):
    """Settings popup dialog."""

    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.title = 'Settings'
        self.size_hint = (0.8, 0.8)
        self.content = self._create_content()

    def _create_content(self):
        """Create settings content."""
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Sound toggle
        sound_layout = BoxLayout(size_hint_y=None, height='40dp')
        sound_layout.add_widget(Label(text='Sound:'))
        sound_btn = CustomButton(
            text='On',
            size_hint_x=None,
            width='100dp'
        )
        sound_layout.add_widget(sound_btn)
        layout.add_widget(sound_layout)

        # Animation toggle
        anim_layout = BoxLayout(size_hint_y=None, height='40dp')
        anim_layout.add_widget(Label(text='Animations:'))
        anim_btn = CustomButton(
            text='On',
            size_hint_x=None,
            width='100dp'
        )
        anim_layout.add_widget(anim_btn)
        layout.add_widget(anim_layout)

        # Close button
        close_btn = CustomButton(
            text='Close',
            size_hint_y=None,
            height='40dp'
        )
        close_btn.bind(on_press=self.dismiss)
        layout.add_widget(close_btn)

        return layout