# find an element->15 in the given  array
import time

start = time.time()
ar = [4, 8, 15, 22, 33, 67, 78]
m = len(ar)//2
# num = int(input('enter a value from the given array: '))
num = 15

if ar[m] > num:
    for i in range(m):
        if ar[i] == num:
            print(i)
else:
    for i in range(m, len(ar)):
        if ar[i] == num:
            print(i)
time.sleep(2)
end = time.time()
print((end - start))