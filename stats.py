def get_num_words(text):
    split_text=text.split()
    length=len(split_text)
    return length

def count_characters(text):
    dict_characters={}
    text_lower = text.lower()
    for character in text_lower:
        if character not in dict_characters:
            dict_characters[character] = 1
        else:
            dict_characters[character] += 1
    return dict_characters

def sort_on(items):
    return items["num"]

def dictionary_to_list(dictionary):
    list_of_key_and_value=[]
    for key in dictionary:
        list_of_key_and_value.append({"char":key, "num":dictionary[key]})
    list_of_key_and_value.sort(reverse=True, key=sort_on)
    return list_of_key_and_value