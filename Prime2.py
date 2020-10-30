import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
for i in range(300,n):
    a = i
    p=1
    for w in range(2,(a//2+1)):
        if a%w==0:
            p=0
            break
    if p==1:
        print(a)


 