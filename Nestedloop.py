import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# for i in range(10):
#     for j in range(10):
#         print(a,end=' ')
#     print()
row= int(input())
column=int(input())
charr= input()
for i in range(row):
    for j in range(column):
        print(charr,end='')
    print()