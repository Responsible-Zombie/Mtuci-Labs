a = int(input())
b = int(input())
c = int(input())

def vad(a, b, c):
    D = (b**2) + (4 * a * c)

    if D > 0:
        x1 = (-b + (D ** (1/2))) / (2*a)
        x2 = (-b - (D ** (1/2))) / (2*a)
        return str(x1), str(x2)
    elif D == 0:
        x = -b / (2 * a)
        return str(x)
    
    realPart = -b / (2*a)
    imaginaryPart = (-D)**(1/2) / (2*a)
    return str(realPart), str(imaginaryPart)

a = vad(a,b,c)
print(", ".join(a))