import src.effects.lyrics as lyrics
import src.common.effects as effects
import src.common.functions as functions
import src.common.osb_converter as convert

scale = 0.88

def generate_storyboard(char_dict):
    globe = {"type": "Sprite",
             "filepath": "sb/globe.png",
             "layer": "Foreground",
             "tether": "Centre",
             "time": {"start": 74053, "end": 84962},
             "position": [320, 240],
             "functions": [{"function": "S",
                            "start": 0,
                            "end": 4,
                            "easing": 0,
                            "arguments": [scale * 0.3, scale * 0.3]}
                           ]}

    ring = {"type": "Sprite",
            "filepath": "sb/ring.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 74053, "end": 84962},
            "position": [320, 240],
            "functions": [{"function": "S",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [scale * 0.31, scale * 0.31]},
                          {"function": "R",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [0, -3.141592]}
                          ]}

    spiral = {"type": "Sprite",
            "filepath": "sb/spiral.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 74053, "end": 84962},
            "position": [320, 240],
            "functions": [{"function": "S",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [scale * 0.59, scale * 0.59]},
                          {"function": "R",
                           "start": 0,
                           "end": 4,
                           "easing": 0,
                           "arguments": [0, 3.141592]}
                          ]}

    glow = {"type": "Sprite",
            "filepath": "sb/glow.png",
            "layer": "Foreground",
            "tether": "Centre",
            "time": {"start": 74053, "end": 84962},
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
                           "arguments": [3.14 / 2, 3.14 / 2]}]}


    return [glow, ring, globe, spiral, burst]
