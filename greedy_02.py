#  큰 수의 법칙

# M번 더해서 가장 큰 수를 만들어라
# 주어진 숫자는 N개
# 한 숫자가 연속으로 나올 수 있는 경우는 K

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#큰수가 더해지는 수
count = int(m/(k+1)) * k + m%(k+1)

result = count * first
result += (m-count) * second

print(result)


# print(int(3.4))
# print(int(3.8))