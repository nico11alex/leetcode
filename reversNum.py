"""
Revers num the min 32 bits
"""

class Solution:
    def reverse(self, x: int) -> int:
        numString = f"{x}"
        negativo = False

        if len(numString) ==1:
            return x
    
        if "-" in numString:
            negativo = True
            numString = numString.replace("-","")
        
        newValue=int(numString[::-1])
        if negativo:
            newValue -= newValue*2
      

        if newValue.bit_length()>=32:
            return 0
        else:
            return newValue
        
    