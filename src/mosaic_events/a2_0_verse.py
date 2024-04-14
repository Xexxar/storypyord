import src.effects.lyrics as lyrics
import src.common.effects as effects
import src.common.functions as functions
import src.common.osb_converter as convert
import src.mosaic_events.a1_0_intro as a1_0
import src.common.restrictions as restrictions
import math


def apply_movement_to_lyrics_1(objects, start, end):
    objects = functions.apply_function_with_restriction(objects,
                                                        {"function": "M",
                                                         "start": start,
                                                         "end": end,
                                                         "easing": 0,
                                                         "arguments": [0, 30]},
                                                        restrictions.absolute_distance_from_center_x, 3)

    objects = functions.apply_function_with_restriction(objects,
                                                        {"function": "M",
                                                         "start": start,
                                                         "end": end,
                                                         "easing": 0,
                                                         "arguments": [30, 0]},
                                                        restrictions.distance_from_center_x, 3)

    objects = functions.apply_function_with_restriction(objects,
                                                        {"function": "R",
                                                         "start": start,
                                                         "end": end,
                                                         "easing": 18,
                                                         "arguments": [0.5]},
                                                        restrictions.distance_from_center_x, 3)

    objects = functions.apply_function(objects,
                                       {"function": "M",
                                        "start": start,
                                        "end": end,
                                        "easing": 18,
                                        "arguments": [0, -250]})

    objects = functions.apply_function_randomly(objects,
                                                {"function": "M",
                                                 "start": start,
                                                 "end": end,
                                                 "easing": 0,
                                                 "arguments": [0, 10]})

    return objects


def apply_movement_to_lyrics_2(objects, start, end):
    objects = functions.apply_function_with_restriction(objects,
                                                        {"function": "M",
                                                         "start": start,
                                                         "end": end,
                                                         "easing": 0,
                                                         "arguments": [1, 0]},
                                                        restrictions.distance_from_center_x, 3)

    objects = functions.apply_function_randomly(objects,
                                                {"function": "R",
                                                 "start": start,
                                                 "end": end,
                                                 "easing": 18,
                                                 "arguments": [0.5]})

    objects = functions.apply_function(objects,
                                       {"function": "M",
                                        "start": start,
                                        "end": end,
                                        "easing": 18,
                                        "arguments": [0, -20]})

    objects = functions.apply_function_randomly(objects,
                                                {"function": "M",
                                                 "start": start,
                                                 "end": end,
                                                 "easing": 0,
                                                 "arguments": [0, 2]})

    return objects


def generate_storyboard(char_dict):
    lyrics = [
        *apply_movement_to_lyrics_1(
            a1_0.base_lyrics_routine("Picture perfect on the wall",
                                     0.15,
                                     {"start": 84962, "end": 90416},
                                     [320, 410],
                                     [1 / 12, 2 / 8, 6 / 8, 7 / 8],
                                     char_dict), 1 / 12, 7 / 8),
        *apply_movement_to_lyrics_1(
            a1_0.base_lyrics_routine("I'm a step behind.",
                                     0.15,
                                     {"start": 90416, "end": 93143},
                                     [320, 410],
                                     [-9 / 32, -1 / 8, 7 / 8, 1],
                                     char_dict), -9 / 32, 1),
        *apply_movement_to_lyrics_2(
            a1_0.base_lyrics_routine("Lost",
                                     0.2,
                                     {"start": 93143, "end": 93655},
                                     [320, 320],
                                     [-1 / 6 + 1 / 12, 0 + 1 / 12, 4 / 6 + 1 / 12,
                                      5 / 6 + 1 / 12],
                                     char_dict),
            -1 / 12, 5 / 6 + 1 / 12),
        *apply_movement_to_lyrics_2(
            a1_0.base_lyrics_routine("in",
                                     0.2,
                                     {"start": 93655, "end": 94166},
                                     [320, 320],
                                     [-1 / 6 + 1 / 12, 0 + 1 / 12, 4 / 6 + 1 / 12,
                                      5 / 6 + 1 / 12],
                                     char_dict),
            -1 / 12, 5 / 6 + 1 / 12),
        *apply_movement_to_lyrics_1(
            a1_0.base_lyrics_routine("time",
                                     0.2,
                                     {"start": 94166, "end": 95871},
                                     [320, 320],
                                     [-1 / 16 + 1 / 32, 0 + 1 / 32, 1 / 2, 1],
                                     char_dict),
            -1 / 32, 1),
    ]

    globe_scale = 0.88

    ring = {"type": "Sprite",
            "filepath": "sb/ring.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 74053, "end": 79507},
            "position": [320, 240],
            "functions": [{"function": "S",
                           "start": 0,
                           "end": 6,
                           "easing": 0,
                           "arguments": [globe_scale * 0.31, globe_scale * 0.31]},
                          {"function": "R",
                           "start": 0,
                           "end": 6,
                           "easing": 0,
                           "arguments": [0, -math.pi]}
                          ]}

    spiral = {"type": "Sprite",
              "filepath": "sb/spiral.png",
              "layer": "Foreground",
              "tether": "Centre",
              "time": {"start": 74053, "end": 79507},
              "position": [320, 240],
              "functions": [{"function": "S",
                             "start": 0,
                             "end": 6,
                             "easing": 0,
                             "arguments": [globe_scale * 0.59, globe_scale * 0.59]},
                            {"function": "R",
                             "start": 0,
                             "end": 6,
                             "easing": 0,
                             "arguments": [0, math.pi]}
                            ]}

    glow = {"type": "Sprite",
            "filepath": "sb/glow.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 74053, "end": 79507},
            "position": [320, 240],
            "functions": [{"function": "C",
                           "start": 0,
                           "end": 6,
                           "easing": 0,
                           "arguments": [252 / 255, 220 / 255, 160 / 255, 252 / 255, 220 / 255, 160 / 255]},
                          {"function": "S",
                           "start": 0,
                           "end": 6,
                           "easing": 0,
                           "arguments": [65, 65]},
                          {"function": "R",
                           "start": 0,
                           "end": 6,
                           "easing": 0,
                           "arguments": [math.pi / 2, math.pi / 2]}]}

    burst = {"type": "Sprite",
             "filepath": "sb/glow.png",
             "layer": "Foreground",
             "tether": "Centre",
             "time": {"start": 74053, "end": 74734},
             "position": [320, 240],
             "functions": [{"function": "F",
                            "start": 0,
                            "end": 1,
                            "easing": 16,
                            "arguments": [1, 0]},
                           {"function": "P",
                            "start": 0,
                            "end": 1,
                            "easing": 0,
                            "arguments": ["A"]},
                           {"function": "S",
                            "start": 0,
                            "end": 1,
                            "easing": 0,
                            "arguments": [75, 75]},
                           {"function": "R",
                            "start": 0,
                            "end": 1,
                            "easing": 0,
                            "arguments": [math.pi / 2, math.pi / 2]}]}

    return [glow, ring, spiral, burst, *lyrics]
