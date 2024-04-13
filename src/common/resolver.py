"""Hell. The worst algorithm in existance."""

def int_time_to_time(object_time, int_time):
    duration = object_time["end"] - object_time["start"]

    return object_time["start"] + duration * int_time

def resolve_storyboard(storyboard):
    # TODO actually write this thing

    for object in storyboard:
        if (object.get("resolved") != True):
            time = object["time"]
            for function in object["functions"]:
                function["start"] = int_time_to_time(time, function["start"])
                function["end"] = int_time_to_time(time, function["end"])

    return storyboard

