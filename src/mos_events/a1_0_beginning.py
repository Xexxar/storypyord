import src.effects.lyrics as lyrics
import src.common.effects as effects

def generate_storyboard(char_dict):
    text = lyrics.generate_text("Can it generate text?\n\nMaybe!", char_dict, 10, 0)
    text_effect = effects.init_simple_effect(text, {"start": 10000, "end": 30000}, 0.15, [320, 240])

    mosbg_go_away = {"type": "Sprite",
                     "filepath": "mosbg.jpg",
                     "layer": "Background",
                     "tether": "Centre",
                     "position": [320, 240],
                     "functions": [{"function": "F",
                                    "start": 0,
                                    "easing": 0,
                                    "arguments": [0]}]}

    return [*text_effect]