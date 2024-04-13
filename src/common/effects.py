"""Functions that are typically used during initatilization of object creation for an effect."""

from src.common.maths import calc_objects_center

def start_centered_at(objects, target_position):
    current_center = calc_objects_center(objects)

    difference = [target_position[0] - current_center[0],
                  target_position[1] - current_center[1]]

    for object in objects:
        object["position"] = [object["position"][0] + difference[0],
                              object["position"][1] + difference[1]]

    return objects


def start_with_scale(objects, scale):
    """Simple scale that starts effect with size"""
    current_center = calc_objects_center(objects)

    for object in objects:
        diff_from_center = [object["position"][0] - current_center[0],
                            object["position"][1] - current_center[1]]
        object["position"] = [current_center[0] + diff_from_center[0] * scale,
                              current_center[1] + diff_from_center[1] * scale]
        object["functions"].append({"function": "S",
                                    "easing": 0,
                                    "start": 0,
                                    "end": 1,
                                    "arguments": [scale, scale]})

    return objects


def start_at_time(objects, time):
    for object in objects:
        object["time"] = time

    return objects


def align_objects_h(objects, alignment):
    alignments = {"left", "right", "center"}

    if alignment not in alignments:
        raise Exception("Alignment selected is not a valid alignment: " + str(alignment) + ". Please use one of " + str(
            alignments) + ".")

    current_center = calc_objects_center(objects)

    objects_sorted = {}
    out = []

    for object in objects:
        objects_sorted[object["position"][1]] = [*objects_sorted[object["position"][1]],
                                                 object] if objects_sorted.get(object["position"][1]) else [object]

    if alignment == "center":
        for row in objects_sorted.values():
            objects_center = calc_objects_center(row)

            difference = [current_center[0] - objects_center[0],
                          current_center[1] - objects_center[1]]

            for object in row:
                object["position"] = [object["position"][0] + difference[0],
                                      object["position"][1]]

                out.append(object)

    return out


def init_simple_effect(objects, time, scale, target_position):
    return start_centered_at(start_with_scale(start_at_time(objects,
                                                            time),
                                              scale),
                             target_position)
