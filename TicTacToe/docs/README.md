# TicTacToe Mobile Game

## 🎮 Overview

A modern implementation of the classic TicTacToe game built with Python and Kivy, featuring AI opponents, cross-platform support, and mobile-first design. This project demonstrates clean architecture, AI algorithms, and responsive UI design principles.

![TicTacToe Game](game_screenshot.png)

## ✨ Features

### Core Game Features

- Single-player mode against AI with multiple difficulty levels
- Two-player local multiplayer mode
- Responsive design for various screen sizes
- Animated game elements and transitions
- Game state persistence
- Move history with undo capability
- Score tracking and statistics

### AI Features

- Three difficulty levels:
  - Easy: Random moves with basic blocking
  - Medium: Minimax algorithm with limited depth
  - Hard: Unbeatable AI using full Minimax with alpha-beta pruning
- Adaptive AI response time
- Learning mode (AI improves based on player patterns)

### Technical Features

- Cross-platform compatibility (Android, iOS, Desktop)
- Efficient resource management
- Configurable settings
- Comprehensive logging system
- Unit and integration tests
- Clean architecture (MVC pattern)

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# pip package manager
pip --version

# Virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tictactoe.git
cd tictactoe
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

### Android Build

```bash
# Install Buildozer
pip install buildozer

# Initialize Buildozer
buildozer init

# Build APK
buildozer android debug

# Build and deploy to connected device
buildozer android debug deploy run
```

## 🏗️ Project Structure

```
TicTacToe/
├── models/                 # Game logic and data structures
│   ├── ai_engine.py       # AI implementation
│   └── game_board.py      # Game state management
├── views/                  # UI components
│   ├── game_view.py       # Main game interface
│   └── ui_components.py   # Reusable UI elements
├── controllers/           # Game flow control
│   └── game_controller.py # Core game controller
├── utils/                 # Helper utilities
│   ├── config_manager.py  # Configuration handling
│   └── logger.py         # Logging system
├── tests/                 # Test suites
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
├── docs/                 # Documentation
├── logs/                 # Log files
└── main.py              # Application entry point
```

## 🔧 Configuration

### config.yml

```yaml
display:
  window_width: 800
  window_height: 600
  fps: 60
  animations_enabled: true

game:
  default_difficulty: "medium"
  sound_enabled: true
  save_games: true
  max_undo_steps: 10

ai:
  max_response_time: 1.0
  easy_depth: 1
  medium_depth: 3
  hard_depth: 9

theme:
  primary_color: "#2C3E50"
  secondary_color: "#E74C3C"
  accent_color: "#3498DB"
  background_color: "#ECF0F1"
```

## 🎮 Game Controls

### Mobile Controls

- Tap: Make a move
- Swipe left: Undo move
- Two-finger tap: Open menu
- Long press: Show move hints

### Desktop Controls

- Left Click: Make a move
- Right Click: Show move hints
- Ctrl+Z: Undo move
- Esc: Open menu

## 🧠 AI Implementation

### Minimax Algorithm

The AI uses the Minimax algorithm with alpha-beta pruning for optimal move selection:

```python
def minimax(board, depth, alpha, beta, is_maximizing):
    if board.is_winner():
        return -1 if is_maximizing else 1
    if board.is_draw():
        return 0
    if depth == 0:
        return evaluate_position(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in board.get_available_moves():
            eval = minimax(board, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.get_available_moves():
            eval = minimax(board, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
```

## 📊 Performance Optimization

### Memory Management

- Efficient board state representation
- Resource pooling for UI elements
- Cached calculations for AI moves
- Optimized sprite handling

### CPU Usage

- Throttled AI calculations
- Efficient rendering pipeline
- Background processing for AI moves
- Lazy loading of resources

## 🔍 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test category
python -m pytest tests/unit/
python -m pytest tests/integration/

# Run with coverage report
python -m pytest --cov=.
```

## 📱 Mobile Development Tips

### Android

- Enable Developer Options on your device
- Enable USB Debugging
- Install Android Studio for SDK management
- Use Logcat for debugging

### iOS

- Install Xcode
- Join Apple Developer Program
- Configure certificates and provisioning profiles
- Use Xcode for debugging

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes:

```bash
git commit -m 'Add some AmazingFeature'
```

4. Push to the branch:

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Kivy development team
- Python community
- Contributors and testers
- Open source projects that inspired this work

## 📞 Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/tictactoe](https://github.com/yourusername/tictactoe)

## 🔄 Version History

- 1.0.0
  - Initial release
  - Basic game functionality
  - AI implementation
- 1.1.0
  - Added mobile support
  - UI improvements
  - Performance optimizations
- 1.2.0
  - Enhanced AI
  - Added multiplayer mode
  - Bug fixes

---

Made with ❤️ for Meriem

```

This README provides:
1. Comprehensive project overview
2. Detailed installation instructions
3. Project structure explanation
4. Configuration details
5. Game controls documentation
6. Technical implementation details
7. Performance optimization guidelines
8. Testing procedures
9. Mobile development tips
10. Contributing guidelines
11. Version history
12. Contact information

Would you like me to elaborate on any specific section or add more details?
```
