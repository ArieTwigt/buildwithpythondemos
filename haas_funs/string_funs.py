def hebrewize(name):
    klinkers = ['a', 'e', 'o', 'u', 'i']
    
    letter_list = []
    
    for letter in name:
        if letter not in klinkers:
            letter_list.append(letter)
            
    name_modified = ''.join(letter_list)
    
    return name_modified


def hebrewize_2(name):
    klinkers = ['a', 'e', 'o', 'u', 'i']
    
    name_modified = "".join([letter for letter in name if letter not in klinkers])
    return name_modified