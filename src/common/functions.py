import src.common.resolver as resolver

def apply_function(objects, function):
    for object in objects:
        object["functions"].append(function)