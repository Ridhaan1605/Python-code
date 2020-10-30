import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
if a==1:
    print("1 is neither prime nor composite")
    exit()
p=1
for i in range(2,(a//2)+1):
    if a%i==0:
        p=0
        break
if p==1:
    print("It's a prime number")
else:
    print("It's not prime")
    