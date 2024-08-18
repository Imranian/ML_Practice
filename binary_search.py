# find an element->15 in the given  array
import time

start = time.time()
arr = [4, 8, 15, 22, 33, 67, 78]
target_num = 15
left = 0
right = len(arr) - 1

while left <= right:

    mid = (right + left) // 2

    # If target_num is greater, ignore left half
    if arr[mid] < target_num:
        left = mid + 1

    # If target_num is smaller, ignore right half
    elif arr[mid] > target_num:
        right = mid - 1

    # means target_num is present at mid
    else:
        print(mid) 
        break


else:
    print(-1)
time.sleep(2)
end = time.time()
print(end - start)


#for loop
# m = len(ar)//2
# # num = int(input('enter a value from the given array: '))
# num = 15

# if ar[m] > num:
#     for i in range(m):
#         if ar[i] == num:
#             print(i)
# else:
#     for i in range(m, len(ar)):
#         if ar[i] == num:
#             print(i)
# time.sleep(2)
# end = time.time()
# print((end - start))