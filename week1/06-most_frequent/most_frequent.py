def most_frequent(items):
    if not items:
        return None
    seen = {}
    for item in items:
        if item in seen:
            seen[item] += 1
        else:
            seen[item] = 1

    highest = 0
    for num in seen.values():
        if num > highest:
            highest = num

    for key, value in seen.items():
        if value == highest:
            return key

print(most_frequent([1, 2, 2, 3]))



def most_frequent2(items):
    if len(items) == 0:
        return None
    count = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    highest = 0
    result = None
    for num in count:
        if count[num] > highest:
            highest = count[num]
            result = num
    return result


