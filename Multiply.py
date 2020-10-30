import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# a=input().split()
# a=[int(i) for i in a]
# prod=1
# for i in range(len(a)):
#     prod=prod*a[i]
# print(prod) 
b=input().split()
a=input().split()
b=[int(i) for i in b]
a=[int(i) for i in a]
prod=1
for i in range(len(a)):
    prod=prod*a[i]
for i in range(len(b)):
    prod=prod*b[i]
print(prod)
