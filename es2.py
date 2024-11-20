def quante_volte(parola, lettera):
    conta = 0
    for carattere in parola:
        if carattere == lettera:
            conta += 1 #oppure conta=conta+1
    return conta
print(quante_volte('ciao', 'a'))