def average(array):
    # your code goes here
    a = set(array)
    s = 0
    for x in a:
        s += x
    av = float( s / len(a) )
    return av