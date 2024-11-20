def palindromo(s):
    if s==s[::-1]: #attenzione allo slicing
       return True
    return False 
stringa = "palla"
print (palindromo(stringa))

#correzione
# def palindromo(stringa):
#     return stringa == stringa [::-1]
#       
# print(palindromo("ciao"))
