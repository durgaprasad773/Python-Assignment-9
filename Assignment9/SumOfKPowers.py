n=int(input())
k=int(input())
sum_of = 0
for i in range(1,n+1):
    sum_of = sum_of + (i**k)
print(sum_of)