"""Functions that are typically used during initatilization of object creation for an effect."""

import src.common.resolver as resolver

def start_centered_at(objects, target_position):
    current_center = [0, 0]

    for object in objects:
        current_center = [current_center[0] + object["position"][0],
                          current_center[1] + object["position"][1]]

    current_center = [current_center[0] / len(objects),
                      current_center[1] / len(objects)]

    difference = [target_position[0] - current_center[0],
                  target_position[1] - current_center[1]]

    for object in objects:
        object["position"] = [object["position"][0] + difference[0],
                              object["position"][1] + difference[1]]

    return objects


def start_with_scale(objects, scale):
    """Simple scale that starts effect with size"""
    current_center = [0, 0]

    for object in objects:
        current_center = [current_center[0] + object["position"][0], current_center[0] + object["position"][0]]

    current_center = [current_center[0] / len(objects), current_center[1] / len(objects)]

    for object in objects:
        diff_from_center = [object["position"][0] - current_center[0],
                            object["position"][1] - current_center[1]]
        object["position"] = [current_center[0] + diff_from_center[0] * scale,
                              current_center[1] + diff_from_center[1] * scale]
        object["functions"].append({"function": "S",
                                    "easing": 0,
                                    "start": 0,
                                    "end": 1,
                                    "arguments": [scale]})

    return objects

def start_at_time(objects, time):
    for object in objects:
        object["time"] = time

    return objects

def init_simple_effect(objects, time, scale, target_position):
    return resolver.resolve_functions(start_centered_at(start_with_scale(start_at_time(objects,
                                                                                       time),
                                                                         scale),
                                                        target_position))
