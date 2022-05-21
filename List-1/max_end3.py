#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


def max_end3_func(nums):

    largest = max(nums)

    new_nums = []

    for _ in nums:
        new_nums.append(largest)

    return new_nums

x = max_end3_func([1,2,3])
y = max_end3_func([11,5,9])
z = max_end3_func([3,3,3])

print(x, y, z)
