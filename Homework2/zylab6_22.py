# Syed Ali
# 1799248

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())


# equation
def solve(first, second, third, fourth, fifth, sixth):
    # iterate x from -10 to 10
    for x in range(-10, 11):
        # iterate x from -10 to 10
        for y in range(-10, 11):
            # check that both string satisfy or not
            if ((x * first) + (y * second) == third) and ((x * fourth) + (y * fifth) == sixth):
                return str(x) + " " + str(y)

    return "No solution"


print(solve(a, b, c, d, e, f))
