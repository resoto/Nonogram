import sys


#進数変換（10 → n）
def Base_10_to_n(X, n, l):
    L = []
    X_dumy = X
    while X_dumy>0:
        L.append(X_dumy%n)
        X_dumy = int(X_dumy/n)
    while len(L) < l:
        L.append(0)
    return L


#配列のコピー
def copyArray(L):
    L2 = []
    for i in L:
        L2.append(i)
    return L2


#盤面の表示

def show(S):
    for i in S:
        for j in i:
            if j == True:
                print("#",end='')
            elif j == False:
                print(".",end='')
            else:
                print("?",end='')
        print("")


#パターンの列挙
def candidates(n,L):

    Q = len(L)-1
    for i in L:
        Q = i + Q

    M2 = []
    for i in range(0,(n-Q+1)**(len(L)+1)):
        A = Base_10_to_n(i,n-Q+1,len(L)+1)
        sum = 0
        for j in A:
            sum += int(j)
        if sum == n-Q:
            M2.append(A)


    result = []    
    for K in M2:
        M = [] 
        for i in range(0,int(K[0])):
            M.append(False)
        for i in range(0,len(L)):
            for j in range(0,L[i]):
                M.append(True)
            if not i == len(L)-1:
                M.append(False)
                for j in range(0,int(K[i+1])):
                    M.append(False)
        for i in range(0,int(K[len(K)-1])):
            M.append(False)    
        result.append(M)
    return result


def propagate(L):
    L1 = []
    if not len(L) == 0:
        L1 = copyArray(L[0])
    for i in L:
        for j in range(0,len(L1)):
            if not L1[j] == i[j]:
                L1[j] = None
            else:
                L1[j] = L1[j] and i[j]

    return L1
            

#横
def propagate1(S,L,l):
    for i in range(0,len(S[l])):
        if len(L)==0:
            return S
        if(L[i]):
            S[l][i] = True
        if(L[i] == False):
            S[l][i] = False
    return S

#縦
def propagate2(S,L,l):
    for i in range(0,len(S)):
        if len(L)==0:
            return S
        if(L[i]):
            S[i][l] = True
        if(L[i] == False):
            S[i][l] = False
    return S

#横
def candidates1(L,S,l):

    A = copyArray(S[l])
    result = []
    
    for i in range(0,len(L)):
        for j in range(0,len(A)):
            
            if not (L[i][j] == A[j]) and (A[j] or (A[j]==False)):
                break
                
            if j == len(A)-1:
                result.append(L[i])
                
 
    return result
    
#縦
def candidates2(L,S,l):

    result = []
    
    for i in range(0,len(L)):
        for j in range(0,len(L[i])):
            
            if not (L[i][j] == S[j][l]) and (S[j][l] or (S[j][l]==False)):
                break
                
            if j == len(S[j])-1:
                result.append(L[i])
            
    return result


def check(S):
    for i in S:
        for j in i:
            if j == None:
                return False
    return True



args = sys.argv
R = []
C = []
f = open(args[1],"r",encoding="utf_8_sig")
for line in f:
    P = []
    D = line.strip().split(" ")
    for i in range(0,len(D)):
        if not i == 0:
            P.append(int(D[i]))
    
    if D[0] == "r":
        R.append(P)
    elif D[0] == "c":
        C.append(P)

S = []
for i in range(0,len(R)):
    S.append([])
    for j in range(0,len(C)):
        S[i].append(None)


R_cand = []
C_cand = []

#横の数 len(C)5
#縦の数 len(R)3

for i in range(0,len(R)):
    R_cand.append(candidates(len(C),R[i]))
    propagate1(S,propagate(R_cand[i]),i)
    


for i in range(0,len(C)):
    C_cand.append(candidates(len(R),C[i]))
    propagate2(S,propagate(C_cand[i]),i)
    


count=0
while True:
    count = count+1
    for i in range(0,len(R)):
        R_cand[i] = candidates1(R_cand[i],S,i)
        propagate1(S,propagate(R_cand[i]),i)
        
    
    for i in range(0,len(C)):
        C_cand[i] = candidates2(C_cand[i],S,i)
        propagate2(S,propagate(C_cand[i]),i)



    if check(S):
        break
    if count == 50:
        break

    
show(S)
