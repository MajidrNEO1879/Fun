from typing import List


A = [1,2,3,4,5,]
#A = [-1, 2, 1, 0, 13, 3, -11]
A = [0, 1, 2, 3, 5,4]
ops = 0
ops2 = 0
for i in range(1,len(A)):
    temp = A[i]
    j = i -1
    ops2+=1
    while j>=0 and A[j]>temp:
        A[j+1], j = A[j], j-1
        ops+=1
    A[j+1]=temp
print (A, ops, ops2)
 