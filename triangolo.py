def triangolo (a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triangolo Equilatero"
        elif a==b or b==c or a==c:
            return "Triangolo isoscele"
        else:
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
                return "Triangolo rettangolo scaleno"
            else:
                return "Triangolo scaleno"
    else:
        return "I numeri non possono formare un triangolo"
print (triangolo(1, 2, 3))