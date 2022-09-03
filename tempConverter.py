def tempConversion(temp, userString):
    while True:
        if userString == 'c':
            x = (temp * 1.8) + 32
            break
        elif userString == 'f':
            x = (temp - 32) * (5 / 9)
            break
        else:
            print("enter c or f")
    return x