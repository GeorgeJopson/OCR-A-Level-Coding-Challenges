fibonacci=[0,1]
places=int(input("How many places: "))
for n in range(len(fibonacci),places):
    fibonacci.append(fibonacci[n-2]+fibonacci[n-1])
print(fibonacci)
