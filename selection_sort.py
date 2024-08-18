# find an element->15 in the given  array

ar = [4,22,8,67,15,33]

for i in range(len(ar)-1):
    min = i
    for j in range(i+1, len(ar)):
        if ar[min] > ar[j]:
            min = j
    ar[min], ar[i] = ar[i], ar[min]

print(ar)