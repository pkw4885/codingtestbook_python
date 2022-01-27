input_data = input()
row = int(input_data[1]) #여기 꼭 int로 묶어야 하는 이유는?
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [[-2,-1], [-1,-2], [2,-1], [1,-2], [2,1], [1,2], [-2,1], [-1,2]]
count = 0

for step in steps:
    nrow = row + step[0]
    ncolumn = column + step[1]
    if nrow < 1 or nrow > 8 or ncolumn < 1 or ncolumn >8:
        count += 1

print(8-count)
