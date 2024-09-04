n=int(input())
for i in range(n):
    if i == 0:
        print("* " * n)
    else:
        row="+ " * (n-i)
        print(row)