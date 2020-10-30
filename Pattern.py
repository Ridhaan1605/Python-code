import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
row=int(input())
column=int(input())
char=input()
# for i in range(row,-1,-1):
#     for j in range(i):
#         print(char,end=" ")
#     print()
for i in range(row):
    for j in range(i+1):
        print(char,end=" ")
    print()
    
