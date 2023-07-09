def in_1st_row(row, n):
    if(n>0 and n<=row):
        return True
    return False

def in_col(row, n, col):
    for i in range(1, col-1):
        if((row*i)+1 == n):
            return True
        elif(row*i == n):
            return True
    if(row*col == n):
        return True

    return False

row, col = map(int, input().split())
n = int(input())

if in_1st_row(row, n) or in_col(row, n, col):
    print(True)
else:
    print(False)