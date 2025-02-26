def get_num_words(text):
    words = text.split()

    return len(words)


def get_num_times_character(text):
    char_dict = {}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def get_dictionary_of_characters(dictionary):
    chars_list = []

    for pairs in dictionary:
        char_dict = {pairs: dictionary[pairs]}
        chars_list.append(char_dict)

    def sort_by_count(dict_item):
        return next(iter(dict_item.values()))

    chars_list.sort(reverse=True, key=sort_by_count)

    return chars_list
