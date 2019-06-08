a, b = map(int, input().split())

ans = 0
if a > 12:
    ans = b
elif 6 <= a <= 12:
    ans = b // 2
print(ans)