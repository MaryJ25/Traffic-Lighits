from itertools import groupby
import sys

"""
Red -> Yellow -> Green -> Yellow -> Red (and repeat)
Red -> Yellow -> Green left -> Green -> Yellow -> Red (and repeat)
Keep in mind that both (and only) green lights blink before turning off, there are no gaps between switches.
The camera might take a picture with no lights on.
Project assumes that green lights always blink before switching to a different colour
"None" indicates only start or end of a dataset, it assumes that a dataset with only one picture is possible
"""

LIGHTS = {"1000": "red", "0100": "yellow", "0010": "green", "0001": "left green", "0000": "blink"}


def current_red(before, after):
    """
    Checks if the red light works well.
    :param before: has to be None or "yellow"
    :param after: has to be None or "yellow"
    :return: if any constraints not met will return False else True
     """
    print(f'{before}--red--{after}')
    accepted = [None, "yellow"]
    if before not in accepted or after not in accepted:
        return False
    return True


def current_yellow(before, after):
    """
    Checks if the yellow light works well.
    :param before: has to be None, "red" or blink
    :param after: has to be None, "red", "green" or "left green"
    :return: if any constraints not met will return False else True
    Additional Constraint:
    1. Colours before and after can't be the same
    2. if previous was "red" then after has to be "green" or "left green"
    3. if previous was "blink" then after has to be "red"

    """
    print(f'{before}--yellow--{after}')
    accepted_before = [None, "red", "blink"]
    accepted_after = [None, "red", "green", "left green"]
    if before not in accepted_before or after not in accepted_after:
        return False
    elif before and after and before == after:
        return False
    elif before == "red" and after not in ["green", "left green", None]:
        return False
    elif before == "blink" and after not in ["red", None]:
        return False
    else:
        return True


def current_green_or_left(before, after, current=None):
    """
    Checks if green and left green lights works well.
    :param before: has to be None, "yellow" or "blink"
    :param after: has to be None or "blink"
    :param current: Set as default None, so it won't trigger tests as the colour is only relevant for print
    :return: if any constraints not met will return False else True
    """
    print(f'{before}--{current}--{after}')
    accepted_before = [None, "yellow", "blink"]
    accepted_after = [None, "blink"]
    if before not in accepted_before or after not in accepted_after:
        return False
    else:
        return True


def current_blink(before, after):
    """
    :param before: has to be None, "left green" or "green"
    :param after: has to be None or "left green", "green" or "yellow"
    :return: if any constraints not met will return False else True
    Additional Constraint:
    1. if before was "green" after has to be "green" or "yellow"
    2. if before was "left green" after has to be "left green" or "green"
    """
    print(f'{before}--blink--{after}')
    accepted_before = [None, "left green", "green"]
    accepted_after = [None, "left green", "green", "yellow"]
    if before not in accepted_before or after not in accepted_after:
        return False
    elif before == "green" and after not in ["green", "yellow", None]:
        return False
    elif before == "left green" and after not in ["green", "left green", None]:
        return False
    else:
        return True


def get_data():
    traffic_lights = []
    try:
        with open('data.txt', 'r') as traffic_data:
            for line in traffic_data.readlines():
                line = line.replace(",", "").strip()
                line = line.replace(line, LIGHTS[line])
                traffic_lights.append(line)
    except FileNotFoundError:
        print("Can't find the file specified!")
        sys.exit(1)

    traffic_lights = [light[0] for light in groupby(traffic_lights)]
    return traffic_lights


def main():
    traffic_data = get_data()
    for idx, current_light in enumerate(traffic_data):
        no_error = None
        if idx == 0:
            previous_light = None
        else:
            previous_light = traffic_data[idx - 1]
        if idx == len(traffic_data) - 1:
            next_light = None
        else:
            next_light = traffic_data[idx + 1]

        if current_light == "red":
            no_error = current_red(previous_light, next_light)
        elif current_light == "yellow":
            no_error = current_yellow(previous_light, next_light)
        elif current_light == "green" or current_light == "left green":
            no_error = current_green_or_left(previous_light, next_light, current_light)
        elif current_light == "blink":
            no_error = current_blink(previous_light, next_light)
        else:
            print("Couldn't recognise the light!")

        if no_error:
            print(f"{idx}. Traffic light works well")
        else:
            print(f"{idx}. Something is wrong!")


if __name__ == "__main__":
    main()
