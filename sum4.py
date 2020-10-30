import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a = input().split()
b=input().split()
c=input().split()

sum=0
for i in range(len(a)):
    a[i]=int(a[i])
    sum=sum+a[i]
  
for i in range(len(b)):
    b[i]=int(b[i])                            
    sum=sum+b[i]
  
for i in range(len(c)):
    c[i]=int(c[i])
    sum=sum+c[i]
print("sum =",sum)


