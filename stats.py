def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    char_count = {}
    #for each character in a string, increment the value of the index (lowercase char) by one.
    for c in text:
        if c.lower() in char_count:
            char_count[c.lower()] += 1
        else:
            char_count[c.lower()] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def get_char_count_sorted(char_count):
    characters = []
    for character in char_count:
        count = char_count[character]
        characters.append({"char": character, "num": count})
    characters.sort(reverse=True, key=sort_on)
    return characters