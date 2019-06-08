n, m = map(int, input().split())

card_list = [1] * n

minr = 10**9
maxl = 0

for i in range(m):
    l, r  = map(int, input().split())
    maxl = max(maxl, l)
    minr = min(minr, r)
print(max(minr - maxl + 1, 0))
