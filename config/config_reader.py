import yaml
from config.paths import ROOT_DIR

_SETTINGS_PATH = ROOT_DIR / "config" / "settings.yaml"
def get_config() -> dict:
    with open(_SETTINGS_PATH) as f:
        settings = yaml.safe_load(f)

    return settings