import os

import src.effects.lyrics as lyrics

import src.mos_events.a1_0_beginning as a1_0



def generate_storyboard():
    """Generate font sets / images here. As well as generating the storyboard json code here from events."""

    path = os.path.dirname(__file__) + '/resources/fonts/'

    font = "kelmscott.ttf"

    kelmscott_out_path = "sb/font/"

    kelmscott_dict = lyrics.generate_image_files(path + font, 140, kelmscott_out_path)

    storyboard = [*a1_0.generate_storyboard(kelmscott_dict)]

    return storyboard