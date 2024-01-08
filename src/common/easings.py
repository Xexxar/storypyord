import math
from functools import partial


def reverse(function, value):
    return 1.0 - function(1.0 - value)


def to_in_out(function, value):
    if value < 0.5:
        return 0.5 * function(2.0 * value)

    return 0.5 * (2.0 - function(2.0 - (2.0 * value)))


def linear(x):
    return x


def quad(x):
    return x * x


def cubic(x):
    return x * x * x


def quart(x):
    return x * x * x * x


def quint(x):
    return x * x * x * x * x


def sine(x):
    return 1.0 - math.cos(math.pi * x / 2.0)


def expo(x):
    return 2.0 ** (10.0 * (x - 1.0))


def circ(x):
    return 1.0 - (1.0 - x * x) ** 0.5


def elastic_out(percent, x):
    return 1.0 + (2.0 ** (-10.0 * x) * math.sin((x * percent - 0.075) * ((2.0 * math.pi) / 0.3)))


def back_in(x):
    return x * x * (((1.0 + 1.70158) * x) - 1.70158)


def back_in_out(x):
    return x * x * (((1.525 * 1.70158 + 1.0) * x) - (1.525 * 1.70158))


def bounce_out(x):
    if x < 1.0 / 2.75:
        return 7.5625 * x * x
    elif x < 2.0 / 2.75:
        return (7.5625 * (x - (1.5 / 2.75)) * (x - (1.5 / 2.75))) + 0.75
    elif x < 2.5 / 2.75:
        return (7.5625 * (x - (2.25 / 2.75)) * (x - (2.25 / 2.75))) + 0.9375
    else:
        return (7.5625 * (x - (2.625 / 2.75)) * (x - (2.625 / 2.75))) + 0.984375


easing_names = {"Linear": 0,
                "InQuad": 3,
                "OutQuad": 4,
                "InOutQuad": 5,
                "InCubic": 6,
                "OutCubic": 7,
                "InOutCubic": 8,
                "InQuart": 9,
                "OutQuart": 10,
                "InOutQuart": 11,
                "InQuint": 12,
                "OutQuint": 13,
                "InOutQuint": 14,
                "InSine": 15,
                "OutSine": 16,
                "InOutSine": 17,
                "InExpo": 18,
                "OutExpo": 19,
                "InOutExpo": 20,
                "InCirc": 21,
                "OutCirc": 22,
                "InOutCirc": 23,
                "InElastic": 24,
                "OutElastic": 25,
                "OutElasticHalf": 26,
                "OutElasticQuarter": 27,
                "InOutElastic": 28,
                "InBack": 29,
                "OutBack": 30,
                "InOutBack": 31,
                "InBounce": 32,
                "OutBounce": 33,
                "InOutBounce": 34}

easings = {0: partial(linear),
           1: partial(linear),  # TODO figure out function for this (i think its circ)
           2: partial(linear),
           3: partial(quad),
           4: partial(reverse, quad),
           5: partial(to_in_out, quad),
           6: partial(cubic),
           7: partial(reverse, cubic),
           8: partial(to_in_out, cubic),
           9: partial(quart),
           10: partial(reverse, quart),
           11: partial(to_in_out, quart),
           12: partial(quint),
           13: partial(reverse, quint),
           14: partial(to_in_out, quint),
           15: partial(sine),
           16: partial(reverse, sine),
           17: partial(to_in_out, sine),
           18: partial(expo),
           19: partial(reverse, expo),
           20: partial(to_in_out, expo),
           21: partial(circ),
           22: partial(reverse, circ),
           23: partial(to_in_out, circ),
           24: partial(reverse, elastic_out),
           25: partial(elastic_out, 1.0),
           26: partial(elastic_out, 0.5),
           27: partial(elastic_out, 0.25),
           28: partial(to_in_out, partial(reverse, partial(elastic_out, 1.0))),
           29: partial(back_in),
           30: partial(reverse, back_in),
           31: partial(to_in_out, back_in_out),
           32: partial(reverse, bounce_out),
           33: partial(bounce_out),
           34: partial(to_in_out, partial(reverse, bounce_out))}


def calc_easing(easing, value):
    try:
        if not isinstance(easing, int):
            easing = int(easing)
        return easings[easing](value)
    except:
        print("Errored on easing, with value " + str(value) + " and easing " + str(easing))
