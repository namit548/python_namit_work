
x = [10, 12, 13, 14, 15, 134, 14141, 1313, 1313131, 90]

for i in range(0,len(x)-1):
    for j in range(i+1, len(x)):
         
         if x[i] > x[j]:
            c = x[i]
            x[i] = x[j]
            x[j] = c

print(x)

