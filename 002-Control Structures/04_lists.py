words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

nums = [5, 4, 3, 2, 1]
print(nums[1])

empty_list = []
print(empty_list)

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
print(num[5])

# The item at a certain index in a list can be reassigned.
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

nums = [1, 2, 3]
print(4 not in nums)
print(3 not in nums)
