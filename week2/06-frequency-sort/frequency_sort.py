def frequency_sort(items):
    # GET THE FREQUENCY
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    # SORT ACCORDING TO FREQUENCY
    freq_sort = sorted(freq.keys(), key =lambda x:(-freq[x], x))
    # 1. sort through the keys of the dict (the values)
    # 2. key= means the formula the sorted function should follow for each iterable
    # 3. lambda x is an anonymous function x represents each of the keys of the dict
    # 4. negate the value of the keys (stating the frequency) so high frequency becomes a very small negative number, forcing it to the front of an ascending sort
    # 5. x means sort by frequency descending. If two frequencies match, sort them alphabetically ascending.
    result = [word for word in freq_sort for _ in range(freq[word])]
    return result

print(frequency_sort([4, 5, 6, 5, 4, 4]))
print(frequency_sort([2, 1, 1, 2, 2, 1, 3]))
print(frequency_sort([5]))
print(frequency_sort([]))
print(frequency_sort(['orange', 'apple', 'apple', 'banana', 'apple', 'orange', 'orange']))





                                                #-value, key
