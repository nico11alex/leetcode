class Solution:
    def convert(self, s: str, numRows: int) -> str:
        orden={}

        if len(s) <= 1 or numRows == 1:
            return s
        
        contador =0 
        bajando = True
        for i in s:
            if contador == 1:
                bajando = True

            if bajando:
                bajando = Solution.ordenar(contador, numRows)
                contador += 1
                orden[contador] = Solution.asignar(orden,i,contador)
            else:
                contador = contador-1
                orden[contador] = Solution.asignar(orden,i,contador)            
        
        palabra = ""
        for i in orden.values():
            palabra += i
        return palabra
    
    def ordenar(contador, numRows):
        if contador == numRows-1:
            return False
        return True
    
    def asignar(orden, nuevoValor,contador):
        if contador not in orden:
            return nuevoValor
        valor = orden[contador]
        return valor + nuevoValor


                  