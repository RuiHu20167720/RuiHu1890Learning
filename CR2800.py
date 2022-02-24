from math import pi


def areacircle(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non_negative real number")
    if r < 0:
        raise ValueError("Radius can not be negative")
    return pi * r ** 2
