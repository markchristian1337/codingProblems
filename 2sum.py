def twoSum(nums, target):
    dict = {}
    for index,number in enumerate(nums):
        complement = target - number
        if number in dict:
            return [dict[number],index]
        else:
            dict[complement] = index

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))