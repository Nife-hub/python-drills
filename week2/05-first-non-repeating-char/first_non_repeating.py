def first_non_repeating(s, case_sensitive=True):
    if not case_sensitive:
        s = s.lower().strip()
    freq = {}
    for ch in s.strip():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for key, value in freq.items():
        if value == 1:
            return key

print(first_non_repeating('DaAbBc', False))
print(first_non_repeating('DaAbBc', True))


