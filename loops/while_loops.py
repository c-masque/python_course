#set a sentinel value in order to tell the while loop to stop

nums = list(range(1, 101))
'''
print(nums)

for num in nums:
    print(num)
'''
############################
'''
while len(nums) > 0: #sentinel value is the len(nums)
    print(nums.pop()) #pop removes item and prints new value
'''
############################

