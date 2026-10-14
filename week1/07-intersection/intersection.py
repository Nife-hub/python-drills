def intersection(a, b) -> list:
    result = []
    for first in a:
        for sec in b:
            if first == sec and first not in result:
                result.append(first)
    return result

print(intersection([1, 2, 2, 3], [2, 2, 3]))