from pixel_font_builder import opentype

from tools.config import paths


def create_thai_feature() -> opentype.FeatureFile:
    return opentype.FeatureFile(
        paths.CONFIGS_FEATURES_THAI_DIR.joinpath('layout.fea'),
        include_dir=paths.CONFIGS_FEATURES_THAI_DIR,
    )
