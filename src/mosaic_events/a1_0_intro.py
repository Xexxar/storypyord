import src.effects.lyrics as lyrics
import src.common.effects as effects
import src.common.functions as functions
import src.common.osb_converter as convert


def base_lyrics_routine(text, scale, time, position, fade_frac_times, char_dict):
    text = lyrics.generate_text(text, char_dict, 10, 25)
    text = effects.align_objects_h(text, "center")
    text_effect = effects.init_simple_effect(text, time, scale, position)
    text_effect = functions.apply_functions(text_effect, [{"function": "F",
                                                           "start": fade_frac_times[0],
                                                           "end": fade_frac_times[1],
                                                           "easing": 15,
                                                           "arguments": [0, 1]},
                                                          {"function": "F",
                                                           "start": fade_frac_times[2],
                                                           "end": fade_frac_times[3],
                                                           "easing": 16,
                                                           "arguments": [1, 0]}])

    # text_effect = functions.apply_function_randomly(text_effect, {"function": "M",
    #                                                               "start": fade_frac_times[0],
    #                                                               "end": fade_frac_times[3],
    #                                                               "easing": 0,
    #                                                               "arguments": [0, 20]})
    #
    # text_effect = functions.apply_function(text_effect, {"function": "M",
    #                                                      "start": fade_frac_times[0],
    #                                                      "end": fade_frac_times[3],
    #                                                      "easing": 15,
    #                                                      "arguments": [0, -200]})

    return text_effect


def generate_storyboard(char_dict):
    text_effect = base_lyrics_routine("To His Glory Alone",
                                      0.15,
                                      {"start": 12694, "end": 25326},
                                      [320, 400],
                                      [0, 1 / 8, 7 / 8, 1],
                                      char_dict)

    lyrics = [
        *base_lyrics_routine("The Artisan designs",
                             0.15,
                             {"start": 25326, "end": 31641},
                             [320, 400],
                             [1 / 8, 2 / 8, 6 / 8, 7 / 8],
                             char_dict)
    ]

    bg_go_away = convert.convert_osb_element_to_object(
        """Sprite,Background,Centre,"mosaic_bg.jpg",320,240\n F,0,0,0,0""")

    glow = {"type": "Sprite",
            "filepath": "sb/glow.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 63, "end": 12694},
            "position": [320, 240],
            "functions": [{"function": "C",
                           "start": 0,
                           "end": 2,
                           "easing": 0,
                           "arguments": [252 / 255, 220 / 255, 160 / 255, 252 / 255, 220 / 255, 160 / 255]},
                          {"function": "S",
                           "start": 0,
                           "end": 2,
                           "easing": 0,
                           "arguments": [50, 50]},
                          {"function": "F",
                           "start": 0,
                           "end": 1 / 2,
                           "easing": 0,
                           "arguments": [0, 1]},
                          {"function": "R",
                           "start": 0,
                           "end": 2,
                           "easing": 0,
                           "arguments": [3.14 / 2, 3.14 / 2]}]}

    dot = {"type": "Sprite",
            "filepath": "sb/dot.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 63, "end": 12694},
            "position": [320, 240],
            "functions": [{"function": "C",
                           "start": 0,
                           "end": 1,
                           "easing": 0,
                           "arguments": [0, 0, 0, 0, 0, 0]},
                          {"function": "S",
                           "start": 0,
                           "end": 1,
                           "easing": 0,
                           "arguments": [1, 1]}
                          ]}

    theocracy = {"type": "Sprite",
           "filepath": "sb/theocracy.png",
           "layer": "Foreground",
           "tether": "Centre",
           "time": {"start": 63, "end": 12694},
           "position": [320, 240],
           "functions": [{"function": "S",
                          "start": 0,
                          "end": 1,
                          "easing": 0,
                          "arguments": [0.5, 0.5]},
                         {"function": "F",
                          "start": 1/8,
                          "end": 1 / 2,
                          "easing": 0,
                          "arguments": [0, 1]},
                         {"function": "F",
                          "start": 3/4,
                          "end": 1,
                          "easing": 0,
                          "arguments": [1, 0]}
                         ]}

    cross = {"type": "Sprite",
                 "filepath": "sb/cross.png",
                 "layer": "Foreground",
                 "tether": "Centre",
                 "time": {"start": 12694, "end": 25326},
                 "position": [320, 220],
                 "functions": [{"function": "S",
                                "start": 0,
                                "end": 1,
                                "easing": 0,
                                "arguments": [0.5, 0.5]},
                               {"function": "F",
                                "start": 0,
                                "end": 1 / 4,
                                "easing": 0,
                                "arguments": [0, 1]},
                               {"function": "F",
                                "start": 3/4,
                                "end": 1,
                                "easing": 0,
                                "arguments": [1, 0]}
                               ]}

    return [*text_effect, *lyrics, dot, glow, bg_go_away, theocracy, cross]
