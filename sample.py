from CR2800 import areacircle

# radii=[1,2,9.6,20,0,-1,2+1j,True,False,"two"]
radii = [1, 2, 9.6, 20, 0, "two"]
message = f"area of circles with r = {radius} is {area}."

for radius in radii:
    try:
        area = areacircle(radius)
        print(message.format(radius=radius, area=area))
    except ValueError as e:
        print(message.format(radius=radius, area=area))
    except ValueError as e:
        print("radius was", radius, " ", e)
    except TypeError as e:
        print("radius was", radius, " ", e)
    except OverflowError as e:
        print("radius was", radius, " ", e)
