def line(s, t):
    k, b = map(float, s[:-1].split("x+"))
    x, y = map(float, t.split(";"))

    if y == k * x + b:
        print("true")
    else:
        print("false")