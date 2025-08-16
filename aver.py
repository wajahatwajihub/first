def aver(nums):
    result = 0
    for num in nums:
        result += num

    return result/len(nums)

print(aver([3,4,5,6,3,34,56]))