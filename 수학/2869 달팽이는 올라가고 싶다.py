
a, b, v = map(int, input().split())

# a*n - b*(n-1) >= v
# n >= (v-b)/(a-b)
# n >= (v-b)//(a-b) + 1

n = (v-b)/(a-b)
print(int(n) if n == int(n) else int(n) + 1)

    
