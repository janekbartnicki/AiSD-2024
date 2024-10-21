def NWD(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def NWW(a, b):
    return (a * b) / NWD(a, b)


a = int(print('a: '))
b = int(print('b: '))
print(f'NWD: {NWD(a, b)}')
print(f'NWW: {NWW(a, b)}')