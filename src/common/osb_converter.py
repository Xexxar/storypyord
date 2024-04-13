def convert_storyboard_to_osb(storyboard: list):
    """Converts from json format storyboard to .osb format"""
    groups = {"Video": "//Background and Video events\n",
              "Background": "//Storyboard Layer 0 (Background)\n",
              "Fail": "//Storyboard Layer 1 (Fail)\n",
              "Pass": "//Storyboard Layer 2 (Pass)\n",
              "Foreground": "//Storyboard Layer 3 (Foreground)\n",
              "Overlay": "//Storyboard Layer 4 (Overlay)\n",
              "Sound": "//Storyboard Sound Samples\n"}

    out = "[Events]\n"

    for k, v in groups.items():
        # Layer level
        out += v

        for object in [x for x in storyboard if x["layer"] == k]:
            # Iterate on objects within layer

            out += ",".join([str(object.get("type")),
                             str(object.get("layer")),
                             str(object.get("tether")),
                             str(object.get("filepath")).replace("/", "\\"),
                             str(object.get("position")[0]),
                             str(object.get("position")[1])]) + "\n"

            if object.get("functions"):
                for function in object.get("functions"):
                    # Iterate on functions within object
                    if function.get("type") == "L":  # TODO Update to handle "T" type trigger functions
                        out += " " \
                               + ",".join(
                            [str(function.get("function")), str(function.get("start")), str(function.get("count"))]) \
                               + "\n"

                        for loop_function in function.get("arguments"):
                            out += "  " + ",".join([str(loop_function.get("function")),
                                                    str(loop_function.get("easing")),
                                                    str(int(loop_function.get("start"))),
                                                    str(int(loop_function.get("end")))]) + ","
                            if loop_function.get("arguments"):
                                out += ",".join([str(x) for x in loop_function.get("arguments")])

                            out += "\n"
                    else:
                        out += " " + ",".join([str(function.get("function")),
                                               str(function.get("easing")),
                                               str(int(function.get("start"))),
                                               str(int(function.get("end")))]) + ","
                        if function.get("arguments"):
                            out += ",".join([str(x) for x in function.get("arguments")])

                        out += "\n"

    return out.replace(",None,", ",,")


def convert_osb_element_to_object(element):
    element = element.split("\n")
    element = [[y.strip() for y in x.split(",")] for x in element]

# Sprite,Foreground,Centre,"sb\font\8.png",268.25,420.0
# S,0,10000,30000,0.15,0.15

    object = {"type": element[0][0],
              "layer": element[0][1],
              "tether": element[0][2],
              "filepath": element[0][3],
              "resolved": True,
              "position": [element[0][4], element[0][5]],
              "functions": []}

    for function in element[1:]:
        object['functions'] = [*object['functions'], {"function": function[0],
                                                      "easing": function[1],
                                                      "start": function[2],
                                                      "end": function[3],
                                                      "arguments": function[4:]}]

    return object
