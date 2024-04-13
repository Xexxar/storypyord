import random

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
        temp_function["arguments"] = [x * random.random() for x in temp_function["arguments"]]

        object["functions"].append(temp_function)

    return objects