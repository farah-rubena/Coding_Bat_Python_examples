#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


def sum2_func(nums):

    if len(nums) <=2:
        return nums[0] + nums[1]
    return nums[0] + nums[1]

x = sum2_func([1,2,3])
y = sum2_func([1,1])
z = sum2_func([1,1,1,1])

print(x, y, z)
