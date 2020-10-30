import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=input()
b=a[::-1]
if a==b:
    print("Yes it is palindrome")
else:
    print("it is not palindrome")
b=a[0:4]
print(b)
b=a[::2]
print(b)