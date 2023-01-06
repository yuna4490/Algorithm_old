import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
s = list(map(str,input().split()))
b = list(map(str,input().split()))

key = (''.join(s))
button = (''.join(b))

if key in button:
    print("secret")

else:
    print("normal")