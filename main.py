"""This is the entry file for a Python Storyboarding tool called storypyord"""

import mosaic_event_maestro as maestro
import src.common.osb_converter as osb_converter
import src.common.resolver as resolver
import pprint

def main() -> None:
    # path = "/home/xexxar/.osustable/drive_c/osu/Songs/1275778 Theocracy - Mirror of Souls/Theocracy - Mirror of Souls (I Must Decrease).osb"
    path = "/home/xexxar/osu-winello-install/osu!/Songs/Theocracy_-_Mosaic/Theocracy - Mosaic (I Must Decrease).osb"

    print("Generating json-esq storyboard...")
    storyboard = maestro.generate_storyboard()
    print("Done!")
    print("Begin resolving and optimizing storyboard...")
    storyboard_post_resolve = resolver.resolve_storyboard(storyboard)
    print("Done!")
    print("Converting to .osb...")
    converted = osb_converter.convert_storyboard_to_osb(storyboard_post_resolve)
    print("Done!")

    # Official out
    file = open(path, "w")
    file.write(converted)
    file.close()

    # handy out
    file = open("test_out.osb", "w")
    file.write(converted)
    file.close()

    # handy out 2
    file = open("test_out_json.osb", "w")
    file.write(pprint.pformat(storyboard_post_resolve))
    file.close()

if __name__ == "__main__":
    main()
