def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    num_words = len(file_contents.split())
    return file_contents, num_words



def count_characters(text):
    lower_text = text.lower()
    char_dict = {}
    for c in lower_text:
        if c in char_dict:
            char_dict[c] = char_dict[c] +1
        else:
            char_dict[c] = 1
    
    return char_dict



def sorted_list(dictionary):
    list = []
    for char, count in dictionary.items():
        small_dict = {"char": char, "count": count}
        list.append(small_dict)
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["count"]