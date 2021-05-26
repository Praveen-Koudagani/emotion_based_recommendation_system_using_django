
def valid(N,A):
    result=-404

    # write here
    for i in range(0,N-4):
        a=A[i]
        b=A[i+1]
        c=A[i+2]
        d=A[i+3]
        if (a+b)==(c+d) and result==-404:
            result=1
        elif (a+b)==(c+d):
            result+=1
    return result

#print(valid(5,[1,2,3,0]))

def ans(n,s):
    turn=0
    my=0
    fr=0
    for i in s:
        if turn==0 or my>=fr:
            if i=="W":
             turn=1
             my+=1
            else:
                fr+=1
        else :
            if i=="W":
              fr+=1
            else:
                my+=1
    print(my,fr)
ans(18,"LWWWWLLWLWLWLWWLWL")