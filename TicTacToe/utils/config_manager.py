# utils/config_manager.py
import yaml
from typing import Dict, Any
from pathlib import Path

class ConfigManager:
    """Manage application configuration settings."""

    DEFAULT_CONFIG = {
        'display': {
            'window_width': 800,
            'window_height': 600,
            'fps': 60,
            'animations_enabled': True
        },
        'game': {
            'default_difficulty': 'medium',
            'sound_enabled': True,
            'save_games': True,
            'max_undo_steps': 10
        },
        'ai': {
            'max_response_time': 1.0,
            'easy_depth': 1,
            'medium_depth': 3,
            'hard_depth': 9
        },
        'theme': {
            'primary_color': '#2C3E50',
            'secondary_color': '#E74C3C',
            'accent_color': '#3498DB',
            'background_color': '#ECF0F1',
            'grid_line_width': 2
        }
    }

    def __init__(self):
        self.config_path = Path('config.yml')
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default."""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    config = yaml.safe_load(f)
                return self._merge_with_defaults(config)
            return self._create_default_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            return self.DEFAULT_CONFIG.copy()

    def _create_default_config(self) -> Dict[str, Any]:
        """Create and save default configuration."""
        try:
            with open(self.config_path, 'w') as f:
                yaml.dump(self.DEFAULT_CONFIG, f)
            return self.DEFAULT_CONFIG.copy()
        except Exception as e:
            print(f"Error creating default config: {e}")
            return self.DEFAULT_CONFIG.copy()

    def _merge_with_defaults(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Merge loaded config with defaults to ensure all keys exist."""
        merged = self.DEFAULT_CONFIG.copy()
        for section, values in config.items():
            if section in merged:
                merged[section].update(values)
        return merged

    def get(self, section: str, key: str) -> Any:
        """Get configuration value."""
        return self.config.get(section, {}).get(key, 
               self.DEFAULT_CONFIG[section][key])

    def update(self, section: str, key: str, value: Any) -> None:
        """Update configuration value and save to file."""
        if section in self.config:
            self.config[section][key] = value
            self._save_config()

    def _save_config(self) -> None:
        """Save current configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f)
        except Exception as e:
            print(f"Error saving config: {e}")