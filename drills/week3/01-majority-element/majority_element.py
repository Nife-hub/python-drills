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

print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
print(majority_element([1, 1, 1, 2, 3]))
print(majority_element([1, 2, 3, 4]))
print(majority_element([1, 2, 1, 2]))
print(majority_element([5]))
print(majority_element([0, 0, 1, 0]))
print(majority_element([-1, -1, -1, 2, 3]))
print(majority_element([]))
