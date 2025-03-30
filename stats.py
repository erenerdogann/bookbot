def get_book_text(path_to_file):
    with open(path_to_file) as f:
        data = f.read()
        return data


def num_words(data):
    return data.split()


def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        sorted_list.append(char_info)

    def sort_on(dict):
        return dict["count"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

