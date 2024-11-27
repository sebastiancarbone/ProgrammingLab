#Scrivere una funzione che prende in input due liste e ritorna `True` se le due liste hanno almeno un elemento in comune
def confronto (lista1, lista2):
    for elemento in lista1: #ciclo for per ogni elemento nella lista1
        if elemento in lista2: #se l'elemento è presente nella lista2
            return True #ritorna True
    return False #se non ci sono elementi in comune, ritorna False
list = [1, 2, 3, 4, 5]
list2 = [1, 10, 6, 7, 8]
print (confronto (list, list2)) #output: True