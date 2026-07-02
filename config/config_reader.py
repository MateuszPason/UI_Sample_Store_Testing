from pathlib import Path
import yaml

_SETTINGS_PATH = Path(__file__).parent / "settings.yaml"
def get_config() -> dict:
    with open(_SETTINGS_PATH) as f:
        settings = yaml.safe_load(f)

    return settings