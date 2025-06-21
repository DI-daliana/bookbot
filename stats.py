def get_string(contents):
    words = contents.split()

    num_words = len(words)
    return num_words

def count_characters(contents):
    characters_rep={}
    
    for letter in contents:
        if letter.lower() not in characters_rep:
            characters_rep[letter.lower()]= 1
        else:
            characters_rep[letter.lower()] +=1 
    return characters_rep

def sort_on(items):
    return items["num"]

def sorted_dic(char_count):
    new_dict=[]
    for key, value in char_count.items():
        if key.isalpha():
            new_dict.append({"char":key, "num":value})
    new_dict.sort(reverse=True, key= sort_on)

    return new_dict
