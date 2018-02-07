"""
Modify the following word_distribution function so that
it returns a dictionary with the count of each word in 
the input string.

Don't forget to put the words in lowercase.

If there's a punctuation sign at the end of a word, you should remove it.
You should remove only one punctuation sign if there are multiple signs.

Tests:

word_distribution("Hello. How are you? Please say hello if you don’t love me!") 
should return {‘hello’: 2, ‘how’:1, ‘are’:1, ‘you’:2, ’please’:1, “don’t”: 1, 'say':1, 'if':1, 'love':1,'me':1}

word_distribution("That's when I saw Jane (John's sister)!")
should return {"that's":1, "when":1,"i":1,"saw":1,"jane":1, "john's":1, "sister)":1}
"""

def word_distribution(string):
    """ (str) -> dict of {str: int}

    Returns a dictionary with the count of each word in  the input string.

    >>> word_distribution("Hello. How are you? Please say hello if you don’t love me!")
    {‘hello’: 2, ‘how’:1, ‘are’:1, ‘you’:2, ’please’:1, “don’t”: 1, 'say':1, 'if':1, 'love':1,'me':1}
    >>> word_distribution("That's when I saw Jane (John's sister)!")
    {"that's":1, "when":1,"i":1,"saw":1,"jane":1, "john's":1, "sister)
    """

    # Create a words list to extract all the words from the string
    words = []
    text = string.split()
    for word in text:
        word = word.strip()
        word = word.lower()
        if not word[0].isalpha():
            word = word[1:]
        elif not word[-1].isalpha():
            word = word[:-1]
        words.append(word)

    # Create a dictionary to store the words and count
    result = {}
    for word in words:
        if not word in result:
            result[word] = 1
        else:
            result[word] += 1
    return result

