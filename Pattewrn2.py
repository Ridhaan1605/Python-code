import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
rows=int(input())
column=int(input())
char=input()
# for i in range(rows,-1,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for v in range((rows-i)*2+1):
#         print(char,end=" ")
#     print()
for i in range(rows,-1,-1):
    for j in range(i):
        print(" ",end=" ")
    for v in range((rows-i)*1+1):
        print(char,end=" ")
    print()