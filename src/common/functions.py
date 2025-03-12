import random
import src.common.easings as easings

def apply_function(objects, function):
    for object in objects:
        object["functions"].append(function.copy())

    return objects

def apply_functions(objects, functions):
    for object in objects:
        for function in functions:
            object["functions"].append(function.copy())

    return objects

def apply_function_randomly(objects, function):
    for object in objects:
        temp_function = function.copy()
        temp_function["arguments"] = [x * (2 * random.random() - 1) for x in temp_function["arguments"]]

        object["functions"].append(temp_function)

    return objects

def apply_function_with_restriction(objects, function, restriction, easing):
    """Applies the function based on the restriction function

    :param objects: objects to apply the function to
    :param function: the function we're applying
    :param restriction: the restriction we're using to decipher the effect per object. Takes only 1 argument, object.
    :return: objects with the new function applied
    """
    restriction_results = []

    for object in objects:
        restriction_results.append(restriction(object))

    # we've calculated restriction_results, now normalize the results to [0, 1]
    restrict_size = max(abs(min(0, *restriction_results)), max(1, *restriction_results))

    restriction_results = [easings.calc_easing(easing, x / restrict_size) if x >= 0 else -easings.calc_easing(easing, abs(x) / restrict_size) for x in restriction_results]

    for index, object in enumerate(objects):
        scale = restriction_results[index]
        temp_function = function.copy()
        temp_function["arguments"] = [x * scale for x in temp_function["arguments"]]

        object["functions"].append(temp_function)

    return objects

def apply_function_with_index_times(objects, function, index_times):

    for index_time in index_times:
        for object in objects[index_time["index"][0]:index_time["index"][1]]:
            temp_function = function.copy()
            temp_function["start"] = index_time["time"]["start"]
            temp_function["end"] = index_time["time"]["end"]

            object["functions"].append(temp_function)

    return objects


def apply_function_v2(objects, function, restriction=None, restriction_easing=None,)