def palindromo(s):
    if s==s[::-1]: #attenzione allo slicing
       return True
    return False 
stringa = "palla"
print (palindromo(stringa))

#correzione
# s="ciao"
# print(s[::-1])
# def palindromo(stringa)
#     return True