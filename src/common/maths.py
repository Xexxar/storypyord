def calc_objects_center(objects):
    max_min_box = {"maxX": objects[0]["position"][0],
                   "minX": objects[0]["position"][0],
                   "maxY": objects[0]["position"][1],
                   "minY": objects[0]["position"][1]}

    for object in objects[1:]:
        x = object["position"][0]
        y = object["position"][1]
        if x > max_min_box["maxX"]:
            max_min_box["maxX"] = x
        if x < max_min_box["minX"]:
            max_min_box["minX"] = x
        if y > max_min_box["maxY"]:
            max_min_box["maxY"] = y
        if y < max_min_box["minY"]:
            max_min_box["minY"] = y

    return [(max_min_box["maxX"] + max_min_box["minX"]) / 2, (max_min_box["maxY"] + max_min_box["minY"]) / 2]