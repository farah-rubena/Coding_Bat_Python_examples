#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.


def make_ends_func(nums):

    new_nums = []

    new_nums.append(nums[0])
    new_nums.append(nums[-1])

    return new_nums

x = make_ends_func([1,2,3])
y = make_ends_func([1,2,3,4])
z = make_ends_func([7,4,6,2])
print(x,y,z)