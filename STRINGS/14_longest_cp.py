class Solution():
    def longest_common_prefix(self,list_strs):
        sorted_strs=sorted(list_strs)
        first=sorted_strs[0]
        last=sorted_strs[-1]
        i=0
        print(len(sorted_strs))
        while i<len(sorted_strs[0]) and first[i]==last[i]:
            i+=1
            
        return first[:i]
    
answer=Solution()
strs=list(input("Enter different strings:").split(","))
print(answer.longest_common_prefix(strs))