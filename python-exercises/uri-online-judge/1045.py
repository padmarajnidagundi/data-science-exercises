valores = input().split()
valores = list(map(float,valores))

A,B,C = sorted(valores)[::-1]

## We cant use 'elif' because the triangles may have more than only one classification

if (A >= (B + C)):
    print("NAO FORMA TRIANGULO")
else:
    if (A**2 == ((B**2) + (C**2))):
        print("TRIANGULO RETANGULO")
    if (A**2 > ((B**2) + (C**2))):
        print("TRIANGULO OBTUSANGULO")
    if (A**2 < ((B**2) + (C**2))):
        print("TRIANGULO ACUTANGULO")
    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
    if (A == B and B != C) or (A == C and C != B) or (B == C and C != A):
        print("TRIANGULO ISOSCELES")