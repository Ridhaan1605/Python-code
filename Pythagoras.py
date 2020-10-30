import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def pythagoras(a):
    if a[0]**2 +a[1]**2 ==a[2]**2:
        print("This is a right angled triangle ")
    else:
        print("It is not a right angled triangle")
a=input().split()
a=[int(i) for i in a]
pythagoras(a)
