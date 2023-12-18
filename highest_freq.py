from letters import letter_count #imports functions from letters.py
from letters import letter_frequency

def highest_freq(file):
    """
    Returns hihest frequency and its corresponding letter
    as a tuple
    """
    ltr = letter_count(file) #assigns ltr with a dict of letters and their occurences
    freq = letter_frequency(file) #assigns freq with a dict of the letters and their frequencies
    max_freq = max(freq.values()) #obtains max frequency value
    max_ltr = max(ltr, key=ltr.get) #obtains the key that the max value is associated with 
    return max_ltr, max_freq #returns tuple of the max frequency and its corresponding letter

#assert statement for highest_freq(file) function
ltr, freq = highest_freq('test.txt') 
print(ltr, freq)
