totale_minuti = 538

ore = totale_minuti // 60 #inserisco la doppia / per indicare che è un intero altrimenti sarebbe: ore= int(totale_minuti/60)
minuti = totale_minuti % 60 #per semplificare il tutto posso usare: ore, minuti = divmod(totale_minuti, 60)
                            #divmod restituisce sia risultato che modulo della doivisione
print(f"{ore}h:{minuti}min")