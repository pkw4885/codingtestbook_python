n = int(input())
x, y = 1, -1
plans = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny > -1 or nx > n or ny < -1*n:
        continue #공간 벗어나는 경우 무시. for문을 무시하고 다음으로 넘어가버리기
    x, y = nx, ny


y = -1*y
print(y,x)

