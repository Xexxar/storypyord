import src.common.resolver as resolver
import src.common.maths as maths
import threading

# TOMORROW:
# CHANGE THE CODE SO THAT SCALING ISNT ALLOWED ON 3D
# CHANGE THE CODE SO THAT APPLY PERSPECTIVE TAKES SPRITE AND CONVERTS TO 2D
# SCALING THAT IS DYNAMIC IS VECTOR BASED


def apply_perspective():
    if not active_functions:
        {function: "S"}


def get_active_functions(functions, time_range):
    # starts before end or ends after start
    return [f for f in functions if f["start"] < time_range[1] or f["end"] > time_range[0]]


def apply_moving_camera_effect(sprite, camera, time_range):
    # TODO hell, 2 hard 2 do rn

    return {}


def apply_stationary_camera_effect(sprite, camera, time_range):
    # TODO Need to break down near edges if there is a non linear motion occuring. For now don't care 2 hard

    active_functions = get_active_functions(sprite["functions"], time_range)
    c_active_functions = get_active_functions(camera["functions"], time_range)

    # create the camera settings.

    # TODO redo this for context with moving effect
    camera_pos = [f for f in c_active_functions if f["function"] == "M"]

    if len(camera_pos) == 0:
        camera_pos = camera.get("position", [0, 0])
    elif len(camera_pos) > 1:
        raise Exception("Multiple camera poses found at stationary camera effect")
    else:
        camera_pos = camera_pos[0].get("arguments")[0:2]

    camera_scale = [f for f in c_active_functions if f["function"] == "S"]

    if len(camera_scale) == 0:
        camera_scale = camera.get("scale", [1])
    elif len(camera_scale) > 1:
        raise Exception("Multiple camera scales found at stationary camera effect")
    else:
        camera_scale = camera_scale[0].get("arguments")[0]

    camera_z = [f for f in c_active_functions if f["function"] == "Z"]

    if len(camera_z) == 0:
        camera_z = camera.get("z", [1])
    elif len(camera_z) > 1:
        raise Exception("Multiple camera zeds found at stationary camera effect")
    else:
        camera_z = camera_z[0].get("arguments")[0]

    # for the current functions, apply this perspective, then return, in moving case, make new functions here
    return apply_perspective(active_functions, camera_pos, camera_scale, camera_z)


def camera_active_check(c_active_functions):
    # need to calculate whether or not hte camera is active

    # TODO
    return 0


def flatten_sprites(sprites, camera):
    """Keep depth data so we can use it to reorder after along with framerate"""
    c_functions = camera["functions"]
    camera_times = maths.determine_time_windows(c_functions)

    out = []

    # TODO thread this

    for sprite in sprites:
        functions = [f for f in sprite["functions"] if f["function"] in {"M"}]

        if not camera_times:
            camera_times = [[min([f["start"] for f in functions]), max([f["start"] for f in functions])]]

        out_sprite = sprite.copy()

        out_sprite["functions"] = [f for f in sprite["functions"] if f["function"] not in {"M"}]
        sprite["functions"] = functions

        for time_range in camera_times:
            # determine if this time is moving, if it is, we're breaking everything into linear movements at the frame rate
            c_active_functions = get_active_functions(c_functions, time_range)

            if not camera_active_check(c_active_functions):
                # Not moving! yay easy
                out_sprite["functions"] = [*out_sprite["functions"],
                                           *apply_stationary_camera_effect(sprite, camera, time_range)]
            else:
                out_sprite["functions"] = [*out_sprite["functions"],
                                           *apply_moving_camera_effect(sprite, camera, time_range)]

        out.append(out_sprite)


def flatten_storyboard(storyboard: dict) -> list:
    """Converts a 3D storyboard dictionary into a list of sprites to convert to .osb

    Args:
        storyboard:"""

    # Goal: get the damn thing to render some text on the screen using this new method.

    # NOTE default z depth is 480

    storyboard = {"camera": {"start": 0,
                             "end": 10000,
                             "position": [0, 0],
                             "scale": 1.0,
                             "framerate": (60000 / 172) / 4,
                             "functions": [{"function": "M",
                                            "easing": 0,
                                            "start": 0,
                                            "end": 1,
                                            "args": [0, 0]},
                                           {"function": "Z",
                                            "easing": 0,
                                            "start": 0,
                                            "end": 1.0,
                                            "args": [1.0]}]},
                  "objects": [{}],
                  "sprites": [{"position": [256, 192, 0],
                               "scale": 1.0,
                               "filepath": "",
                               "tether": "",
                               "type": "",
                               "layer": "",
                               "start": 0,
                               "end": 10000,
                               "functions": []}]}

    # Ok, we know our plan for how we will structure the data. First, we need to run the storyboard through the resolver

    storyboard = resolver.resolve_storyboard(storyboard)

    # Okay, we have a storyboard now with all times de-fractioned. We can now begin to do flattening
    # in order to do this, we need to loop through each object and calculate real screen position.
    # if the effect is a non linear motion coupled with a non linear camera movement, then the motion must be interpolated
    # likewise,
    # when we cross a depth containing an object, we generate a new sprite layered above that object, assuming same layer

    out_objects = []
