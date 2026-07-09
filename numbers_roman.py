class Solution:
    def romanToInt(self, s: str) -> int:
        suma=0
        simbolos=['I','X','C']

        valores={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        contador =0
        while contador<len(s):
            if s[contador] in simbolos and contador<len(s)-1:
                simbolo = s[contador] + s[contador+1]
                if simbolo in valores:
                    suma += valores[simbolo]
                    contador+=2
                else:
                    suma+=valores[s[contador]]
                    contador+=1
                    
            else:
                suma+=valores[s[contador]]
                contador+=1
                

            
        return suma




        