from pixel_font_builder import opentype

from tools.config import paths
from tools.font.feature.thai import create_thai_feature


def create_feature_program() -> opentype.FeatureProgram:
    return opentype.FeatureProgram([
        opentype.FeatureFile(
            paths.CONFIGS_FEATURES_DIR.joinpath('calt.fea'),
            include_dir=paths.CONFIGS_FEATURES_DIR,
        ),
        create_thai_feature(),
    ])
