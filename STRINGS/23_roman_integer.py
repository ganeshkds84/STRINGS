class Solution():
    def roman_integer(self,s):
        if not s:
            return "Invalid input"
        roman_values={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        for ch in s:
            if ch not in roman_values:
                return "Inavalid input"
        result=roman_values[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if roman_values[s[i]]<roman_values[s[i+1]]:
                result-=roman_values[s[i]]
            else:
                result+=roman_values[s[i]]
    
        return result
    
s=input("Enter roman value:")
answer=Solution()
print(answer.roman_integer(s))