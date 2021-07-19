def calculate_angle(*angles):
    angleCount = len(angles)
    angle1 = int(angles[0])

    if angleCount == 2:
        angle2 = int(angles[1])
        angle3 = 180 - angle1 - angle2
        return angle3
    else:
        angle3 = 90 - angle1
        return angle3
