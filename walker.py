import math
def solve(a, b, c, alpha, beta, gamma):
    result = []
    # x-dir
    if alpha <= 90 or alpha >= 270:
        a_x = abs(a * math.cos(math.radians(alpha)))
    else:
        a_x = -abs(a * math.cos(math.radians(alpha)))

    if beta <= 180:
        b_x = -abs(b * math.sin(math.radians(beta)))
    else:
        b_x = abs(b * math.sin(math.radians(beta)))

    if gamma <= 90 or gamma >= 270:
        c_x = -abs(c * math.cos(math.radians(gamma)))
    else:
        c_x = abs(c * math.cos(math.radians(gamma)))

    # y-dir
    if alpha <= 180:
        a_y = abs(a * math.sin(math.radians(alpha)))
    else:
        a_y = -abs(a * math.sin(math.radians(alpha)))

    if beta <= 90 or beta >= 270:
        b_y = abs(b * math.cos(math.radians(beta)))
    else:
        b_y = -abs(b * math.cos(math.radians(beta)))

    if gamma <= 180:
        c_y = -abs(c * math.sin(math.radians(gamma)))
    else:
        c_y = abs(c * math.sin(math.radians(gamma)))

    sum_x = a_x + b_x + c_x
    sum_y = a_y + b_y + c_y

    tOC = math.degrees(math.atan2(sum_y, sum_x))
    dCO = ((sum_x ** 2) + (sum_y ** 2)) ** 0.5

    degrees = int(tOC)
    minutes = (tOC - int(tOC)) * 60
    seconds = (minutes - int(minutes)) * 60

    result.append(int(round(dCO, 0)))
    result.append(degrees)
    result.append(int(minutes))
    result.append(int(seconds))

    return result

solve(12, 20, 18, 45, 30, 60)
solve(15,15,19,50,29,55)
solve(14,25,17,41,35,59)
