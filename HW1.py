def replace(test_string, replace_string):
    """ (str, str) -> str

    Return a new string where the first occurrence of replace_string has been
    replaced by "bodega", based on test_string as an input.
    
    >>> replace("Hi how are you?", "you")
    "Hi how are bodega?"
    """

    i = test_string.find(replace_string)
    replength = len(replace_string)
    
    str1 = test_string[:i]
    str2 = 'bodega'
    str3 = test_string[(i+replength):]
    transformed_string =  str1 + str2 + str3
    
    return transformed_string
