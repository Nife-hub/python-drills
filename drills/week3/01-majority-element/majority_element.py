def majority_element(numbers) -> int | None:
    half = len(numbers)/2
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key in freq:
        if freq[key] > half:
            return key

    return None

def majority_element2(nums):
    cand = None
    count = 0
    for num in nums:
        if count == 0:
            cand = num
            count = 1
        elif num == cand:
            count += 1
        else:
            count -= 1

    freq = 0
    for num in nums:
        if num == cand:
            freq += 1
    if freq > len(nums)//2:
        return cand
    return None



print(majority_element2([3, 3, 2, 3, 1]))
print(majority_element2([5, 1, 5, 2, 5, 5, 3]))
print(majority_element2([2, 2, 1, 2]))
print(majority_element2([1, 2, 3, 2]))
print(majority_element2([7, 7, 7, 1, 1]))
# print(majority_element([3, 2, 3]))
# print(majority_element([2, 2, 1, 1, 1, 2, 2]))
# print(majority_element([1, 1, 1, 2, 3]))
# print(majority_element([1, 2, 3, 4]))
# print(majority_element([1, 2, 1, 2]))
# print(majority_element([5]))
# print(majority_element([0, 0, 1, 0]))
# print(majority_element([-1, -1, -1, 2, 3]))
# print(majority_element([]))





