import src.effects.lyrics as lyrics
import src.common.effects as effects
import src.common.functions as functions
import src.common.osb_converter as convert
import src.mosaic_events.a1_0_intro as a1_0
import src.common.restrictions as restrictions
import math


def generate_storyboard(char_dict):
    glow = {"type": "Sprite",
            "filepath": "sb/glow.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 204962, "end": 210416},
            "position": [320, 240],
            "functions": [{"function": "C",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [252 / 255, 220 / 255, 160 / 255, 252 / 255, 220 / 255, 160 / 255]},
                          {"function": "S",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [65, 65]},
                          {"function": "R",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [3.14 / 2, 3.14 / 2]}]}

    globe_scale = 0.88

    globe = {"type": "Sprite",
             "filepath": "sb/globe.png",
             "layer": "Foreground",
             "tether": "Centre",
             "time": {"start": 204962, "end": 210416},
             "position": [320, 240],
             "functions": [{"function": "S",
                            "start": 0,
                            "end": 3,
                            "easing": 0,
                            "arguments": [globe_scale * 0.25, globe_scale * 0.25]},
                           {"function": "S",
                            "start": 3,
                            "end": 3 + 3/4,
                            "easing": 17,
                            "arguments": [globe_scale * 0.25, globe_scale * 0.3]},
                           {"function": "S",
                            "start": 3 + 3/4,
                            "end": 4,
                            "easing": 0,
                            "arguments": [globe_scale * 0.3, globe_scale * 0.3]},
                           ]}

    ring = {"type": "Sprite",
            "filepath": "sb/ring.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 204962, "end": 210416},
            "position": [320, 240],
            "functions": [{"function": "S",
                           "start": 0,
                           "end": 3,
                           "easing": 0,
                           "arguments": [globe_scale * 0.34, globe_scale * 0.34]},
                          {"function": "S",
                           "start": 3,
                           "end": 3 + 3/4,
                           "easing": 17,
                           "arguments": [globe_scale * 0.34, globe_scale * 0.31]},
                          {"function": "R",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [0, -4 * math.pi]}
                          ]}

    spiral = {"type": "Sprite",
              "filepath": "sb/spiral.png",
              "layer": "Foreground",
              "tether": "Centre",
              "time": {"start": 204962, "end": 210416},
              "position": [320, 240],
              "functions": [{"function": "S",
                             "start": 0,
                             "end": 3,
                             "easing": 0,
                             "arguments": [globe_scale * 0.8, globe_scale * 0.8]},
                            {"function": "S",
                             "start": 3,
                             "end": 3 + 3/4,
                             "easing": 17,
                             "arguments": [globe_scale * 0.8, globe_scale * 0.59]},
                            {"function": "R",
                             "start": 0,
                             "end": 4,
                             "easing": 0,
                             "arguments": [0, 4 * math.pi]}
                            ]}

    burst = {"type": "Sprite",
             "filepath": "sb/white.jpg",
             "layer": "Foreground",
             "tether": "Centre",
             "time": {"start": 204962, "end": 210416},
             "position": [320, 240],
             "functions": [{"function": "F",
                            "start": 0,
                            "end": 1,
                            "easing": 19,
                            "arguments": [1.0, 0]},
                           {"function": "P",
                            "start": 0,
                            "end": 1,
                            "easing": 0,
                            "arguments": ["A"]}]}

    return [glow, globe, ring, spiral, burst]
