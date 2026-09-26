from pixel_font_builder import opentype

from tools.config import path_define
from tools.font.feature.thai import create_thai_feature


def create_feature_program() -> opentype.FeatureProgram:
    return opentype.FeatureProgram([
        opentype.FeatureFile(
            path_define.CONFIGS_FEATURES_DIR.joinpath('calt.fea'),
            include_dir=path_define.CONFIGS_FEATURES_DIR,
        ),
        create_thai_feature(),
    ])
