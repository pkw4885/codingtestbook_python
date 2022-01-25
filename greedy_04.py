# 1이 될 때까지

n, k = map(int, input().split())

temp = True
count = 0
while temp:
    if n % k == 0:
        n = n/k
    else:
        n = n-1
    count += 1

    if n == 1:
        temp = False
        break

print(count)