def count_characters(text) -> dict:
    result = {
        'letters': 0,
        'numbers': 0,
        'spaces': 0,
        'special': 0
        }
    for char in text:
        if char.isalpha():
            result['letters'] += 1
        elif char.isdigit():
            result['numbers'] += 1
        elif char == " ":
            result['spaces'] += 1
        else:
            result['special'] += 1   
    return result

# print(count_characters("Hello World 123!"))
    