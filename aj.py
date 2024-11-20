def scambio (A, i, j):
    A[i], A[j] = A[j], A[i]
lista = [1, 2, 3, 4, 5]
scambio(lista, 0, 4)
print (lista)