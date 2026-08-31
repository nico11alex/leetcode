class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStrings = [] 

        for i in range(0, len(s)):
            subString = s[i:]
            subStrings.append(Solution.length(subString))
        
        if len(s) != 0:
            maximo = max(subStrings, key=len)
            return len(maximo)
        return 0



    def length(s)-> str:
        subString = ''
        for i in s:
            if i in subString:
                return subString
            else:
                subString += i
        return subString