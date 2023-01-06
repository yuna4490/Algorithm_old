import sys
input = sys.stdin.readline

t = int(input())

switches = {
    '0' : '1110111',
    '1' : '0010001',
    '2' : '0111110',
    '3' : '0111011',
    '4' : '1011001',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110001',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000'
}

for k in range(t):
    cnt = 0
    a, b = input().split()
    a = (5 - len(a)) * ' ' + a
    b = (5 - len(b)) * ' ' + b

    for i in range(5):
        for j in range(7):
            if switches[a[i]][j] != switches[b[i]][j]:
                cnt += 1
    
    print(cnt)