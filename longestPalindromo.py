class Solution:
    def longestPalindrome(self, s: str) -> str:
        palabras = {}
        palindromos = {}
        posicion = {}
        for i in s:
            if i in posicion:
                continue
            posicionesletra = Solution.posiciones(s,i)
            if len(posicionesletra) >= 2:
                posicion.update({i:posicionesletra})
                
        for clave , valor in posicion.items():
            palabras2 = Solution.subString(s,valor,clave)
            if palabras2 != 0:
                palabras.update(palabras2)
            
        
        if len(s) <= 1 or len(palabras) == 0:
            return s[0]
        
        clave = max(palabras)
        return palabras[clave]
       

    def posiciones(s,letraBuscada):
        posicion = []
        for i,letra in enumerate(s):
            if letra == letraBuscada:
                posicion.append(i)
        return posicion
    
    def subString(s,posicion,letra):
        subString = {}
        for i in range(0,len(posicion)):
            if i != len(posicion):
                for j in range(i+1,len(posicion)):
                    palabra = s[posicion[i]:posicion[j]]
                    palabra += letra
                    palabra = Solution.palindromo(palabra)
                    if palabra == 0:
                        continue
                    subString.update({len(palabra):palabra})
        
        if len(subString) >=1:
            return subString
        return 0
    
    def palindromo(palabra):
        palabraAlReves = palabra[::-1]
        if palabra == palabraAlReves:
            return palabra
        return 0
    

