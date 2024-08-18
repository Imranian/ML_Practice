# find an element->15 in the given  array

ar = [4,22,8,67,15,33]
for i,j in enumerate(ar):
    if j == 15:
        print(i)
        break
# or 

for i in range(len(ar)):
    if ar[i] == 15:
        print(i)
        break
else:
    print('not found')