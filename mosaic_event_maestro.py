import os

import src.effects.lyrics as lyrics
import src.common.resolver as resolver

import src.mosaic_events.a1_0_intro as a1_0
import src.mosaic_events.a2_0_verse as a2_0
import src.mosaic_events.a2_1_prechorus as a2_1
import src.mosaic_events.a2_2_chorus as a2_2
import src.mosaic_events.a3_2_chorus as a3_2




def generate_storyboard():
    """Generate font sets / images here. As well as generating the storyboard json code here from events."""

    path = os.path.dirname(__file__) + '/resources/fonts/'

    font = "kelmscott.ttf"

    kelmscott_out_path = "sb/font/"

    kelmscott_dict = lyrics.generate_image_files(path + font, 140, kelmscott_out_path)

    storyboard = [*a1_0.generate_storyboard(kelmscott_dict),
                  *a2_0.generate_storyboard(kelmscott_dict),
                  *a2_1.generate_storyboard(kelmscott_dict),
                  *a2_2.generate_storyboard(kelmscott_dict),
                  *a3_2.generate_storyboard(kelmscott_dict),]

    return storyboard