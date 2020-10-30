import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=input().split()
print(a)
for i in range(len(a)):
    a[i]=int(a[i])
print(a)
