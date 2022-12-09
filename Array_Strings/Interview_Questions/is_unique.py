#method1: by sorting the given string
def method1(s):
    s=s.sort()                          #O(Nlog(N))
    unique=True
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            unique=False
            break
    return unique
#method2 : using diffrent data structure i.e. hashtable
def method2(s):
    lookup={}                           #O(N)  but it will tak extra space
    for i in range(0,len(s)):
        lookup[s[i]]=True
    if len(lookup)==len(s):
        return True
    return False
#method3 : simply brite force compare one element to each element
def method3(s):
    for i in range(0,len(s)):           #O(N^2)  it is brute force method
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                return False
    return True
