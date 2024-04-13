import src.effects.lyrics as lyrics
import src.common.effects as effects

import src.common.osb_converter as convert


def generate_storyboard(char_dict):
    text = lyrics.generate_text("To His Glory Alone", char_dict, 10, 25)
    text = effects.align_objects_h(text, "center")
    text_effect = effects.init_simple_effect(text, {"start": 10000, "end": 30000}, 0.15, [320, 420])

    bg_go_away = convert.convert_osb_element_to_object("""Sprite,Background,Centre,"mosaic_bg.jpg",320,240\n F,0,0,0,0""")

    # mosbg_go_away = {"type": "Sprite",
    #                  "filepath": "mosbg.jpg",
    #                  "layer": "Background",
    #                  "tether": "Centre",
    #                  "position": [320, 240],
    #                  "functions": [{"function": "F",
    #                                 "start": 0,
    #                                 "easing": 0,
    #                                 "arguments": [0]}]}

    return [*text_effect, bg_go_away]
