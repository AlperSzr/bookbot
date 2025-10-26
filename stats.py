def get_num_words(text):
    split_text=text.split()
    length=len(split_text)
    return length

def count_characters(text):
    dict_characters={
    }
    lowered_text=text.lower()
    for character in lowered_text:
        if character not in dict_characters:
	    dict_characters[character] = 1
	else:
	    dict_characters[character] += 1
    return dict_characters


count_characters("AA a!")
