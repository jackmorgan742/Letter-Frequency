import string

def letter_count(filename):
    """
    Returns a dict of all letters within filename
    with the number of their occurences as the corresponding values
    Fails if file is empty
    """
    if not any(line.strip() for line in open(filename)):
      raise Exception("The file is empty!")
    else:
        filename = open(filename, "r").read().lower() #opens file to read and sets all letters to lowercase
        filename = filename.split() #puts all words into a list seperated by space
        d = dict()
        for word in filename:
            for letter in word:
                    if letter in string.ascii_lowercase: #prevents speacil characters from making it into the dictionary
                        if letter in d: #fills in empty dictionary, creating a value of 1 or increasing value by 1
                            d[letter] += 1
                        else:
                            d[letter] = 1
    return d

def letter_frequency(dict_letters):
    """
    returns dict of all letters within dict_letters
    and their frequency (ratio between number of occurences and the total number of letters)
    as the corresponding values
    """
    d = dict()
    counts = letter_count(dict_letters) #stores dict using letter_count function within counts
    sum_letters = sum(counts.values()) #Retrieves sum of all values in counts
    for ratio in counts:
        frequency = counts.get(ratio) / sum_letters #calculates ratio (frequency) for each value
        d[ratio] = frequency #adds calculated ratio to a new empty dict
    return d

if __name__ == '__main__':
    #assert test for letter_count(filename) function
    expected_count = {'a': 1, 
                    'e': 3,
                    'x': 1,
                    't': 2,
                    'r': 2,
                    'o': 2,
                    'd': 1,
                    'i': 1,
                    'n': 2,
                    'y': 1,
                    'm': 2,
                    'v': 1}
    actual_count = letter_count('test.txt')
    assert(expected_count == actual_count)

    #assert test for letter_frequency(dict_letters) function
    expected_freq = 0.15789473684210525                         
    dict_freq = letter_frequency('test.txt')
    actual_freq = dict_freq.get('e')
    assert round(expected_freq, 3) == round(actual_freq, 3)
    print(letter_frequency('test.txt'))
