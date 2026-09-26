from pixel_font_builder import opentype

from tools.config import path_define


def create_thai_feature() -> opentype.FeatureFile:
    return opentype.FeatureFile(
        path_define.CONFIGS_FEATURES_THAI_DIR.joinpath('layout.fea'),
        include_dir=path_define.CONFIGS_FEATURES_THAI_DIR,
    )
