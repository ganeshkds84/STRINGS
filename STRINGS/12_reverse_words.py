class Solution():
    def reverse_words(self,string):
        s=string.split(" ")
        print(s)
        l=s[::-1]
        
        return " ".join(l)
    
string='Hello world'
answer=Solution()
print(answer.reverse_words(string))
        