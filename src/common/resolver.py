"""Hell. The worst algorithm in existance."""
import src.common.easings as easings


def int_time_to_time(object_time, int_time):
    duration = object_time["end"] - object_time["start"]

    return int(object_time["start"] + duration * int_time)


def determine_time_windows(functions):
    windows = set({})

    for function in functions:
        if function.get("start") not in windows:
            windows.add(function.get("start"))
        if function.get("end") not in windows:
            windows.add(function.get("end"))

    windows = list(windows)
    windows.sort()

    out = []

    for x in range(len(windows) - 1):
        out.append([windows[x], windows[x + 1]])

    return out

def calculate_effective_percent(time_window, function):
    easing = function.get("easing")
    start = function.get("start")
    end = function.get("end")
    duration = end - start

    beginning_percent = (time_window[0] - start) / duration
    end_percent = (time_window[1] - start) / duration

    return easings.calc_easing(easing, end_percent) - easings.calc_easing(easing, beginning_percent)


def resolve_function_group(object, function_type, functions, default, merge_type):
    if merge_type not in ["multiplication", "addition"]:
        raise Exception("Merge_type chosen not supported. We only support addition and multiplication here.")

    time_windows = determine_time_windows(functions)
    arg_dimension = len(default)

    out_functions = []

    window_default = default

    for time_window in time_windows:
        active_functions = [function for function in functions
                            if (function.get("start") < time_window[1] and function.get("end") >= time_window[1])]

        if not any(active_functions):
            continue

        window_default = [*window_default, *window_default]

        # TODO probably need to do something like this later.
        non_linear_functions = [function for function in active_functions if function.get("easing") != 0]
        linear_functions = [function for function in active_functions if function.get("easing") != 0]

        window_easing = 0

        if any(non_linear_functions):
            if len(non_linear_functions) > 1:
                print(non_linear_functions)
                raise Exception("NOT YET SUPPORTED")

            if non_linear_functions[0].get("end") != time_window[1]:
                print(non_linear_functions)
                print(time_window)
                raise Exception("NOT YET SUPPORTED")

            window_easing = non_linear_functions[0].get("easing")

        non_delta_functions = [function for function in active_functions if function.get("start") == time_window[0]
                               and len(function.get("arguments")) == 2 * arg_dimension]
        active_functions = [function for function in active_functions if not (function.get("start") == time_window[0]
                               and len(function.get("arguments")) == 2 * arg_dimension)]

        if any(non_delta_functions):
            if len(non_delta_functions) > 1:
                raise Exception("Multiple non delta functions used at the same initial start time!")
            args = non_delta_functions[0].get("arguments")

            effective_percent = calculate_effective_percent(time_window, non_delta_functions[0])

            for x in range(arg_dimension):
                window_default[x] = args[x]
                window_default[x + arg_dimension] = effective_percent * args[x + arg_dimension]

        # calculate effective movement based on current position.

        window_actual = window_default

        for function in active_functions:
            args = function.get("arguments")

            if len(args) > arg_dimension:
                if merge_type == "multiplication":
                    # TODO figure out how to solve the bug here where we can div by 0.
                    args = [args[x + arg_dimension] / args[x] for x in range(arg_dimension)]
                elif merge_type == "addition":
                    args = [args[x + arg_dimension] - args[x] for x in range(arg_dimension)]

            effective_percent = calculate_effective_percent(time_window, function)

            if merge_type == "multiplication":
                for x in range(arg_dimension):
                    window_actual[x + arg_dimension] = window_actual[x + arg_dimension] * effective_percent * args[x]
            elif merge_type == "addition":
                for x in range(arg_dimension):
                    window_actual[x + arg_dimension] = window_actual[x + arg_dimension] + effective_percent * args[x]


        if function_type == "C":
            window_actual = [min(255, int(255 * x)) for x in window_actual]

        window_result = {"function": function_type,
                         "easing": window_easing,
                         "start": int_time_to_time(object["time"], time_window[0]),
                         "end": int_time_to_time(object["time"], time_window[1]),
                         "arguments": window_actual.copy()}

        window_default = [window_actual[arg_dimension + x] for x in range(arg_dimension)]

        out_functions.append(window_result)

    return out_functions


def resolve_storyboard(storyboard):
    # TODO actually write this thing

    function_merge_types = {"S": "multiplication",
                            "M": "addition",
                            "F": "multiplication",
                            "R": "addition",
                            "V": "multiplication",
                            "C": "multiplication"}

    for object in storyboard:
        if object.get("resolved"):
            # Skip already resolved functions.
            continue

        function_defaults = {"S": [1],
                             "M": object.get("position"),
                             "F": [1],
                             "R": [0],
                             "V": [1, 1],
                             "C": [1, 1, 1]}

        functions = object.get("functions")
        result_functions = []

        unique_functions = {function.get("function") for function in functions}

        for function_type in unique_functions:
            function_group = [function for function in functions if function.get("function") == function_type]

            if function_type in ["L", "P"]:
                for function in function_group:
                    function["start"] = int_time_to_time(object["time"], function.get("start"))
                    function["end"] = int_time_to_time(object["time"], function.get("end"))

                result_functions = [*result_functions,
                                    *function_group]

                continue

            result_functions = [*result_functions,
                                *resolve_function_group(object,
                                                        function_type,
                                                        function_group,
                                                        function_defaults[function_type],
                                                        function_merge_types[function_type])]

        object["functions"] = result_functions

    return storyboard
