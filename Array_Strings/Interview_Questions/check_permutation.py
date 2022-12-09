#method1
def method1(s1,s2):
    if len(s1)!=len(s2):
        return False
    lookup1={}
    for i in range(len(s1)):
        if s1[i] not in lookup1:
            lookup1[s1[i]]=0
        else:
            lookup1[s1[i]]+=1
    lookup2={}
    for i in range(len(s2)):
        if s1[i] not in lookup1:
            lookup1[s1[i]]=0
        else:
            lookup1[s1[i]]+=1
    if len(lookup1)!=len(lookup2):
        return False

    for i in s1:
        if i in s2 and lookup1[i]==lookup2[i]:
            continue
        else:
            return False
    return True
    