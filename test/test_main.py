import main as m


def test_current_red():
    assert m.current_red("yellow", None)  # True
    assert m.current_red(None, "yellow")  # True
    assert m.current_red(None, None)  # True
    assert m.current_red("yellow", "yellow")  # True
    assert not m.current_red("yellow", "blink")  # False
    assert not m.current_red("blink", "yellow")  # False
    assert not m.current_red("yellow", "left green")  # False
    assert not m.current_red("left green", "yellow")  # False
    assert not m.current_red("yellow", "green")  # False
    assert not m.current_red("green", "yellow")  # False
    assert not m.current_red("blink", "left green")  # False
    assert not m.current_red("left green", "blink")  # False
    assert not m.current_red("blink", None)  # False
    assert not m.current_red(None, "blink")  # False
    assert not m.current_red("blink", "green")  # False
    assert not m.current_red("green", "blink")  # False
    assert not m.current_red(None, "left green")  # False
    assert not m.current_red("left green", None)  # False
    assert not m.current_red("green", "left green")  # False
    assert not m.current_red("left green", "green")  # False
    assert not m.current_red(None, "green")  # False
    assert not m.current_red("green", None)  # False
    assert not m.current_red("blink", "blink")  # False
    assert not m.current_red("green", "green")  # False
    assert not m.current_red("left green", "left green")  # False


def test_current_yellow():
    assert m.current_yellow("blink", "red")  # True
    assert m.current_yellow("red", None)  # True
    assert m.current_yellow(None, "red")  # True
    assert m.current_yellow("red", "green")  # True
    assert m.current_yellow("red", "left green")  # True
    assert m.current_yellow("blink", None)  # True
    assert m.current_yellow(None, "left green")  # True
    assert m.current_yellow(None, None)  # True
    assert m.current_yellow(None, "green")  # True
    assert not m.current_yellow("red", "blink")  # False
    assert not m.current_yellow("left green", "red")  # False
    assert not m.current_yellow("green", "red")  # False
    assert not m.current_yellow("blink", "left green")  # False
    assert not m.current_yellow("left green", "blink")  # False
    assert not m.current_yellow(None, "blink")  # False
    assert not m.current_yellow("blink", "green")  # False
    assert not m.current_yellow("green", "blink")  # False
    assert not m.current_yellow("left green", None)  # False
    assert not m.current_yellow("green", "left green")  # False
    assert not m.current_yellow("left green", "green")  # False
    assert not m.current_yellow("green", None)  # False
    assert not m.current_yellow("red", "red")  # False
    assert not m.current_yellow("blink", "blink")  # False
    assert not m.current_yellow("green", "green")  # False
    assert not m.current_yellow("left green", "left green")  # False


def test_current_green_or_left():
    assert m.current_green_or_left(None, None)  # True
    assert m.current_green_or_left("blink", None)  # True
    assert m.current_green_or_left("blink", "blink")  # True
    assert m.current_green_or_left(None, "blink")  # True
    assert m.current_green_or_left("yellow", "blink")  # True
    assert m.current_green_or_left("yellow", None)  # True
    assert not m.current_green_or_left("red", "blink")  # False
    assert not m.current_green_or_left("red", "left green")  # False
    assert not m.current_green_or_left("red", None)  # False
    assert not m.current_green_or_left("red", "green")  # False
    assert not m.current_green_or_left("red", "yellow")  # False
    assert not m.current_green_or_left("red", "red")  # False
    assert not m.current_green_or_left("blink", "red")  # False
    assert not m.current_green_or_left("left green", "red")  # False
    assert not m.current_green_or_left(None, "red")  # False
    assert not m.current_green_or_left("green", "red")  # False
    assert not m.current_green_or_left("yellow", "red")  # False
    assert not m.current_green_or_left("blink", "left green")  # False
    assert not m.current_green_or_left("blink", "green")  # False
    assert not m.current_green_or_left("blink", "yellow")  # False
    assert not m.current_green_or_left("left green", "blink")  # False
    assert not m.current_green_or_left("green", "blink")  # False
    assert not m.current_green_or_left(None, "left green")  # False
    assert not m.current_green_or_left("left green", None)  # False
    assert not m.current_green_or_left("green", "left green")  # False
    assert not m.current_green_or_left("left green", "green")  # False
    assert not m.current_green_or_left("yellow", "left green")  # False
    assert not m.current_green_or_left("left green", "yellow")  # False
    assert not m.current_green_or_left(None, "green")  # False
    assert not m.current_green_or_left("green", None)  # False
    assert not m.current_green_or_left(None, "yellow")  # False
    assert not m.current_green_or_left("yellow", "green")  # False
    assert not m.current_green_or_left("green", "yellow")  # False
    assert not m.current_green_or_left("green", "green")  # False
    assert not m.current_green_or_left("left green", "left green")  # False
    assert not m.current_green_or_left("yellow", "yellow")  # False


def test_current_blink():
    assert m.current_blink(None, None)  # True
    assert m.current_blink("left green", "left green")  # True
    assert m.current_blink("left green", None)  # True
    assert m.current_blink("left green", "green")  # True
    assert m.current_blink("green", None)  # True
    assert m.current_blink("green", "yellow")  # True
    assert m.current_blink("green", "green")  # True
    assert m.current_blink(None, "left green")  # True
    assert m.current_blink(None, "green")  # True
    assert m.current_blink(None, "yellow")  # True
    assert not m.current_blink("left green", "red")  # False
    assert not m.current_blink("left green", "yellow")  # False
    assert not m.current_blink("green", "red")  # False
    assert not m.current_blink("green", "left green")  # False
    assert not m.current_blink("yellow", None)  # False
    assert not m.current_blink("red", "left green")  # False
    assert not m.current_blink("red", None)  # False
    assert not m.current_blink("red", "green")  # False
    assert not m.current_blink("red", "yellow")  # False
    assert not m.current_blink("red", "red")  # False
    assert not m.current_blink(None, "red")  # False
    assert not m.current_blink("yellow", "red")  # False
    assert not m.current_blink("yellow", "left green")  # False
    assert not m.current_blink("yellow", "green")  # False
    assert not m.current_blink("yellow", "yellow")  # False
