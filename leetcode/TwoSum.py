
def two_sum(nums, target):
    result = []
    dictionary = {}

    for i in range(len(nums)):
        x = target - nums[i]
        if x in dictionary:
            result.append(i)
            result.append(dictionary[x])
            return result
        else:
            dictionary[nums[i]] = i


n = [2, 7, 11, 15]
t = 9
print(two_sum(n, t))

