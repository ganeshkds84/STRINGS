class solution():
    def is_palindrome(self,string):
        string=string.lower()
        s1=string[::-1]
        if s1==string:
            return "palindrome"
        else:
            return "Not a palindrome"
    
string=input("Enter the string:")
answer=solution()
print(answer.is_palindrome(string))
