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
    x = convertAngle(angle)
    if oppositeSide == True:
        answer = math.sqrt(side1**2 + side2**2 - 2*side1*side2*math.cos(x))
    elif oppositeSide == False:
        sides = (side1, side2)
        y = math.sin(min(sides), max(sides))
    return y


def convertAngle(angle):
    import math
    radianAngle = angle*(math.pi/180)
    x = float(radianAngle)
    return x


def solution(a, b):
    a = answers[0]
    b = answers[1]
    x = max[a, b]
    return x


def quadratic(a, b, c):
    import math
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    answers = float([x1, x2])
    answers.sort()
    return answers
