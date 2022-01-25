# 숫자 카드 게임

# 문제 자체가 그냥 정답이라 이게 해설인가 싶을 정도로 의아했다
# "각 행에서 낮은 걸 뽑아야 한다. 그 중 가장 높을 카드를 골라라"를 푸시오
# 의 정답이 "각 행에서 낮은 걸 뽑은 뒤, 그 중 가장 높을 카드를 고르면 된다" ?!?!?!?
# 좀 이상..;;
# "1,2,3 을 차례대로 더하려면 어떻게 해야하는가?" "1,2,3을 차례대로 더하면 된다" 같다;;
# 일단 진행

n, m = map(int, input().split())

result_min = []

for i in range(n):
    data = list(map(int, input().split()))
    miny = min(data)
    result_min.append(miny)

print(max(result_min))