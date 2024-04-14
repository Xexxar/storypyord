import src.effects.lyrics as lyrics
import src.common.effects as effects
import src.common.functions as functions
import src.common.osb_converter as convert
import src.common.restrictions as restrictions


def apply_lyrics_functions(objects, start, end):
    objects = functions.apply_function(objects, {"function": "M",
                                                 "start": start,
                                                 "end": end,
                                                 "easing": 17,
                                                 "arguments": [0, -80]})

    objects = functions.apply_function_randomly(objects, {"function": "M",
                                                          "start": start,
                                                          "end": end,
                                                          "easing": 0,
                                                          "arguments": [0, -2]})

    objects = functions.apply_function_with_restriction(objects, {"function": "M",
                                                                  "start": start,
                                                                  "end": end,
                                                                  "easing": 0,
                                                                  "arguments": [0, 20]},
                                                        restrictions.absolute_distance_from_center_x, 3)

    objects = functions.apply_function_with_restriction(objects, {"function": "M",
                                                                  "start": start,
                                                                  "end": end,
                                                                  "easing": 0,
                                                                  "arguments": [15, 0]},
                                                        restrictions.distance_from_center_x, 0)

    objects = functions.apply_function_with_restriction(objects, {"function": "R",
                                                                  "start": start,
                                                                  "end": end,
                                                                  "easing": 0,
                                                                  "arguments": [0.25]},
                                                        restrictions.distance_from_center_x, 3)

    objects = functions.apply_function_randomly(objects, {"function": "R",
                                                          "start": start,
                                                          "end": end,
                                                          "easing": 0,
                                                          "arguments": [0.05]})

    return objects


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

    return text_effect


def generate_storyboard(char_dict):
    text_effect = base_lyrics_routine("For His Glory Alone",
                                      0.15,
                                      {"start": 12694, "end": 25326},
                                      [320, 400],
                                      [1 / 2, 5 / 8, 7 / 8, 1],
                                      char_dict)

    credits = [*base_lyrics_routine("a beatmap collaboration featuring\nFoss",
                                    0.2,
                                    {"start": 12694, "end": 25326},
                                    [320, 240],
                                    [0, 1 / 8, 3 / 8, 1 / 2],
                                    char_dict),
               *base_lyrics_routine("with hitsounds by\nnebuwua",
                                    0.15,
                                    {"start": 12694, "end": 25326},
                                    [320, 400],
                                    [0, 1 / 8, 3 / 8, 1 / 2],
                                    char_dict), ]

    lyrics = [*apply_lyrics_functions(base_lyrics_routine("The Artisan designs",
                                                          0.15,
                                                          {"start": 25326, "end": 31641},
                                                          [320, 280],
                                                          [1 / 8, 2 / 8, 1 + 6 / 8, 1 + 7 / 8],
                                                          char_dict),
                                      1 / 8, 3 / 2)]

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
                           "arguments": [65, 65]},
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
                 "position": [320, 200],
                 "functions": [{"function": "S",
                                "start": 0,
                                "end": 1,
                                "easing": 0,
                                "arguments": [0.5, 0.5]},
                               {"function": "F",
                                "start": 1 / 8,
                                "end": 1 / 2,
                                "easing": 0,
                                "arguments": [0, 1]},
                               {"function": "F",
                                "start": 7 / 8,
                                "end": 1,
                                "easing": 0,
                                "arguments": [1, 0]}
                               ]}

    mosaic_text = {"type": "Sprite",
                   "filepath": "sb/mosaic_text.png",
                   "layer": "Foreground",
                   "tether": "Centre",
                   "time": {"start": 63, "end": 12694},
                   "position": [320, 340],
                   "functions": [{"function": "S",
                                  "start": 0,
                                  "end": 1,
                                  "easing": 0,
                                  "arguments": [0.5, 0.5]},
                                 {"function": "F",
                                  "start": 1 / 2,
                                  "end": 5 / 8,
                                  "easing": 0,
                                  "arguments": [0, 1]},
                                 {"function": "F",
                                  "start": 7 / 8,
                                  "end": 1,
                                  "easing": 0,
                                  "arguments": [1, 0]}
                                 ]}

    cross_glow = {"type": "Sprite",
            "filepath": "sb/glow.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 12694, "end": 25326},
            "position": [320, 220],
            "functions": [{"function": "S",
                           "start": 0,
                           "end": 2,
                           "easing": 0,
                           "arguments": [15, 15]},
                          {"function": "F",
                           "start": 1 / 2,
                           "end": 5 / 8,
                           "easing": 17,
                           "arguments": [0, 1]},
                          {"function": "F",
                           "start": 5 / 8,
                           "end": 6 / 8,
                           "easing": 17,
                           "arguments": [1, 0.5]},
                          {"function": "F",
                           "start": 6 / 8,
                           "end": 7 / 8,
                           "easing": 17,
                           "arguments": [0.5, 1]},
                          {"function": "F",
                           "start": 7 / 8,
                           "end": 1,
                           "easing": 17,
                           "arguments": [1, 0]}]}

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
                            "start": 1 / 2,
                            "end": 5 / 8,
                            "easing": 0,
                            "arguments": [0, 1]},
                           {"function": "F",
                            "start": 7 / 8,
                            "end": 1,
                            "easing": 0,
                            "arguments": [1, 0]}
                           ]}

    return [bg_go_away, glow, cross_glow, cross, *text_effect, *lyrics, dot, theocracy, *credits, mosaic_text]
