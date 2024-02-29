def check_pin(pinCode):
    a, b, c = pinCode.split('-')

    a = int(a)
    if a < 2:
        return 'Некорректен'
    for i in range(2, int(a * 0.5) + 1):
        if a % i == 0:
            return 'Некорректен'

    b = int(b)
    if str(b) != str(b)[::-1]:
        return 'Некорректен'

    c = int(c)
    if c <= 0 or (c & (c - 1)) != 0:
        return 'Некорректен'

    return 'Корректен'