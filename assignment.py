#! python3

import math


def tempConversion(degrees, unit="C"):
    if unit == "C":
        converted = 9*(float(degrees)/5)+32
    elif unit == "F":
        converted = (5*(float(degrees)-32))/9
    return round(converted, 1)


def factorPair(number, factor):
    factor2 = number/factor
    answer = [int(factor), int(factor2)]
    answer.sort()
    return answer


def cosineLaw(side1, side2, angle, oppositeSide=True):
    import math
    x = toRadians(angle)
    if oppositeSide == True:
        tanswer = math.sqrt(side1**2 + side2**2 - 2*side1*side2*math.cos(x))
        return tanswer
    elif oppositeSide == False:
        if side1 > side2:
            s = side2
        else:
            s = side1
        a = 1
        b = -2*s*math.cos(x)
        c = side2**2 - side1**2
        qlist = quadratic(a, b, c)
        fanswer = solution(qlist)
        return fanswer


def toRadians(angle):
    import math
    radianAngle = angle*(math.pi/180)
    x = float(radianAngle)
    return x


def quadratic(a, b, c):
    import math
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    answers = [x1, x2]
    answers.sort()
    return answers


def solution(a):
    z = a[1]
    return z
