def remove_duplicates(nums) -> list:
    if not nums:
        return []
    new = []
    for num in nums:
        if num in new:
            continue
        new.append(num)
    return new

print(remove_duplicates([1, 2, 2, 3, 4, 4]))
print(remove_duplicates([3, 1, 3, 2, 1]))
print(remove_duplicates([]))