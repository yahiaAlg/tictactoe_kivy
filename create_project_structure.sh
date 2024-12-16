#!/bin/bash

# Create main project directory
mkdir -p TicTacToe

# Create project structure
cd TicTacToe

# Create main directories
mkdir -p models controllers views utils tests docs logs

# Create subdirectories
mkdir -p tests/unit tests/integration

# Create model files
touch models/__init__.py
touch models/ai_engine.py
touch models/game_board.py

# Create controller files
touch controllers/__init__.py
touch controllers/game_controller.py

# Create view files
touch views/__init__.py
touch views/ui_components.py
touch views/game_view.py

# Create utility files
touch utils/__init__.py
touch utils/config_manager.py
touch utils/logger.py

# Create test files
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py
touch tests/unit/test_ai_engine.py
touch tests/unit/test_game_board.py
touch tests/unit/test_game_controller.py
touch tests/integration/test_game_flow.py

# Create documentation files
touch docs/README.md
touch docs/CONTRIBUTING.md
touch docs/CHANGELOG.md

# Create configuration files
touch config.yml
touch requirements.txt
touch .gitignore
touch main.py
touch README.md

# Create empty logs directory
touch logs/.gitkeep

# Add basic .gitignore content
echo "# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual Environment
venv/
env/
ENV/

# IDE
.idea/
.vscode/

# Logs
logs/*
!logs/.gitkeep

# Distribution
dist/
build/
*.egg-info/

# Local configuration
config.yml

# System files
.DS_Store" > .gitignore

# Make the script executable
chmod +x create_project_structure.sh

echo "Project structure created successfully!"

# Print the directory structure
echo -e "\nProject structure:"
tree -a