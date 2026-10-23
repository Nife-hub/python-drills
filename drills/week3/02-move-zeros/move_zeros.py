def move_zeros(numbers):
    for index in range(len(numbers)):
        if numbers[index] == 0:
            numbers.pop(index)
            numbers.append(numbers[index])
    return numbers

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 0, 2, 0, 3]))