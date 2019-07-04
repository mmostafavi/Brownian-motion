import math

# ignoring the two first line of output
# because they are pygame's greeting and ...
ignore1 = input()
ignore2 = input()


def avagrado():
    # "count" for n in formulla and total
    #  for adding r^2's together.
    count = 0
    total = 0

    while True:
        try:
            r = input()
            if r != "":
                r = float(r) * 0.175e-10
                total += r*r
                count += 1
        # except stands for when there isn't
        # any data anymore
        except:
            break

    d = total/(count*2)
    t = 297
    n = 9.135e-4
    p = 0.5e-6
    r = 8.31446

    # k = 6(pi)dnp/t
    k = 6 * math.pi * d * n * p / t

    # Na = r / k
    Na = r / k

    print("Boltzmann = %se-23" % (str(k)[:6]))
    print("Avagadro  = %se+23" % (str(Na)[:6]))


def __main__():
    avagrado()


if __name__ == "__main__":
    __main__()
