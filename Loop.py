import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
b=int(input())
for i in range(b+1):
    print(a+i)
    
