class Solution:
    def similitud(prefijo,palabra2):
        if prefijo == palabra2:
            return palabra2
        palabra = ""
        for i in range(len(prefijo)):
            if i == len(palabra2):
                if prefijo[i] in palabra2 and len(prefijo)==len(palabra2):
                    palabra += prefijo[i]
                    break
                else:
                    break
            if prefijo[i]==palabra2[i]:
                palabra += prefijo[i]
            else:
                break
        return palabra
    def longestCommonPrefix(self, strs: List[str]) -> str:
        valor=strs[0]
        del strs[0]
        for i in strs:
            valor=Solution.similitud(valor,i)
        return valor



