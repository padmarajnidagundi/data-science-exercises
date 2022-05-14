import math


A = 10.0
B = 20.1
C = 5.1

delta = B**2 - 4*A*C
divisao = 2*A

if delta < 0 or divisao == 0:
    print("Impossivel calcular")
else:
    root = math.sqrt(delta)
    R1 = (-B+root)/divisao
    R2 = (-B-root)/divisao
    
    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))