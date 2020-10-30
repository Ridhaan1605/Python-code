import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
print("hello world")
a=int(input())
b=int(input())
c=int(input())
print("sum:", a+b+c)
if a>b and a>c:
    print("A is greatest", a)
elif a<b and b>c:
    print(" B is the greatest", b)
else: 
    print("C is the greatest", c)
    
