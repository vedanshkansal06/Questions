def isNameValid(name):
    """
    Write down a method boolean isNameValid(String  name).
        A name is valid if following conditions are satisfied:
            • It does not contain any vowel more than once.
            • If the name contains two 'S', then there is not any 'T' in between them (both in capital cases).
    """
    vowels = 'AEIOUaeiou'
    vowel_count = 0
    for i in name:
        for j in vowels:
            if i == j:
                vowel_count += 1
                if vowel_count > 1:
                    return False
    if name.count('S') == 2:
        if 'T' in name:
            first_index=name.index('S')
            second_index=name.index('T')
            name_sliced = name[second_index:len(name)]
            if 'S' in name_sliced and first_index < second_index:
                return False
    return True
String_name = input("Enter a name: ")
print(isNameValid(String_name))

