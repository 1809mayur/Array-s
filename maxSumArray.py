# naive approach.
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
# maxSum = 0   #assumed maxSum is 0

# for i in range(n):
#     for j in range(n):
#         if maxSum < sum(arr[i:j+1]):        #comparing sum of all possible sub-array's.
#             maxSum = sum(arr[i:j+1])        #here we get maxSum.
#             elements = arr[i:j+1]           #elements of sub-array.
# print(maxSum)
# print(elements)

#reduce its complexity to linear time.
# by kadane's algorithm.
start = 0
end = 0
current_max = arr[0]
actual_max = arr[0]
for i in range(1,n):
    if arr[i] < current_max + arr[i]:
        current_max = current_max + arr[i]            #use inbuilt max function for calculating max sum array.
    else:
        start = i
    if actual_max < current_max:
        actual_max = current_max
        end = i 
    # current_max = max(arr[i],arr[i] + current_max)
    # actual_max = max(actual_max,current_max)

        
    
print(actual_max)
print(arr[start:end])

        

        
        