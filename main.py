print("SEJA UMA MATRIZ DO SEGUINTE MODELO:")
print(" _________________ ")
print(" | a11  a12  a13 | ")
print(" | a21  a22  a23 | ")
print(" | a31  a32  a33 | ")
print(" _________________ ")
print("DEFINA OS VALORES DA MATRIZ 'A'")


a11 = int(input("Digite o valor para a11: "))
a12 = int(input("Digite o valor para a12: "))
a13 = int(input("Digite o valor para a13: "))
a21 = int(input("Digite o valor para a21: "))
a22 = int(input("Digite o valor para a22: "))
a23 = int(input("Digite o valor para a23: "))
a31 = int(input("Digite o valor para a31: "))
a32 = int(input("Digite o valor para a32: "))
a33 = int(input("Digite o valor para a33: "))


A = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]


print("A MATRIZ 'A' É:")
print(A[0])
print(A[1])
print(A[2])


print("DEFINA OS VALORES PARA A MATRIZ 'B'")


b11 = int(input("Digite o valor para b11: "))
b12 = int(input("Digite o valor para b12: "))
b13 = int(input("Digite o valor para b13: "))
b21 = int(input("Digite o valor para b21: "))
b22 = int(input("Digite o valor para b22: "))
b23 = int(input("Digite o valor para b23: "))
b31 = int(input("Digite o valor para b31: "))
b32 = int(input("Digite o valor para b32: "))
b33 = int(input("Digite o valor para b33: "))

B = [[b11, b12, b13], [b21, b22, b23], [b31, b32, b33]]


print("A MATRIZ 'B' É:")
print(B[0])
print(B[1])
print(B[2])

print("MULTRIPLICANDO A.B=C")
print("OS ELEMENTOS DA MATRIZ C É:")
print("EXEMPLO: c11 = (a11*b11 + a12*b21 + a13*b31)")

c11 = (a11*b11+a12*b21+a13*b31)
c12 = (a11*b12+a12*b22+a13*b32)
c13 = (a11*b13+a12*b23+a13*b33)
c21 = (a21*b11+a22*b21+a23*b31)
c22 = (a21*b12+a22*b22+a23*b32)
c23 = (a21*b13+a22*b23+a23*b33)
c31 = (a31*b11+a32*b21+a33*b31)
c32 = (a31*b12+a32*b22+a33*b32)
c33 = (a31*b13+a32*b23+a33*b33)
C = [[c11, c12, c13], [c21, c22, c23], [c31, c32, c33]]

print("A MATRIZ 'C' É:")
print(f"{C[0]}")
print(f"{C[1]}")
print(f"{C[2]}")
print(" _____________________________________")
