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
                             '"' + str(object.get("filepath")).replace("/", "\\") + '"',
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
                                                    str(loop_function.get("start")),
                                                    str(loop_function.get("end"))]) + ","
                            if loop_function.get("arguments"):
                                out += ",".join([str(x) for x in loop_function.get("arguments")])

                            out += "\n"
                    else:
                        out += " " + ",".join([str(function.get("function")),
                                               str(function.get("easing")),
                                               str(function.get("start")),
                                               str(function.get("end"))]) + ","
                        if function.get("arguments"):
                            out += ",".join([str(x) for x in function.get("arguments")])

                        out += "\n"

    return out.replace(",None,", ",,")
