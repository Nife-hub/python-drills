import string
def longest_word(sentence):
    words = sentence.split()
    punc = str.maketrans('', '', string.punctuation)
    clean_words = [word.translate(punc) for word in words]
    if clean_words == []:
        return ""
    longest = clean_words[0]
    
    for word in clean_words:
        if word == "":
            return ""
        if len(word) > len(longest):
            longest = word
    return longest


# bonus
def longest_words(sentence):
    words = sentence.split()
    punc = str.maketrans('', '', string.punctuation)
    clean_words = [word.translate(punc) for word in words]
    if clean_words == []:
        return []
    longest = clean_words[0]
    longest = clean_words[0]

    for word in clean_words:
        if word == "":
            return ""
        if len(word) > len(longest):
            longest = word 

    result = []
    for word in clean_words:
        if len(longest) == len(word):
            result.append(word)
    return result

print(longest_word(""))        # → ["cat", "bat", "rat"]
print(longest_word("the quick brown fox"))
print(longest_word('hi there'))
print(longest_word('hello, world'))
print(longest_words(""))        # → ["cat", "bat", "rat"]
print(longest_words("the quick brown fox"))
print(longest_words('hi there'))
print(longest_words('hello world'))
