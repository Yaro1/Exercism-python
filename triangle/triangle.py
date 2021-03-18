def triangle(f):
    return lambda s: 2 * max(s) < sum(s) and f(s)


@triangle
def equilateral(sides):
    return len(set(sides)) == 1


@triangle
def isosceles(sides):
    return len(set(sides)) < 3


@triangle
def scalene(sides):
    return len(set(sides)) == 3
