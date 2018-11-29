# Given a string, cycle the first letter of each word back one word,
# and cycle the last letter of each word forward one word. 

def cycle_letters(s):
    """
    input: string of words
    output: new string of words with rotated letters
    >>> cycle_letters('who welld horly')
    'why hello world'

    >>> cycle_letters('bes le uoogit')
    'let us boogie'

    """

    # I assume the string is not an empty string
    # for one word strings- it will just return the same word

    words = s.split()
    n = len(words)
    new_words = []
    for i,word in enumerate(words):
        first_letter = get_first_letter(words,i,n)
        last_letter = get_last_letter(words,i,n)
        new_words.append(build_word(first_letter, word, last_letter))

    new_words_str = words_to_string(new_words)
    return new_words_str

def get_first_letter(words,i,n):
    """returns first letter of new word"""
    # calculate which word we take the first letter from
    # return that letter from that word
    first_letter_index = (i + 1) % n
    first_letter = words[first_letter_index][0]
    return first_letter

def get_last_letter(words,i,n):
    """returns last letter of new word"""
    # calculate which word we take the last letter from
    # return that letter from that word
    last_letter_index = (i - 1 + n) % n
    last_letter = words[last_letter_index][-1]
    return last_letter

def build_word(first_letter, word, last_letter):
    """return new word according to new first and last letters """
    new_word = first_letter + word[1:-1] + last_letter
    return new_word

def words_to_string(words):
    """return a string made of list of words """
    return " ".join(words)


# cycle_letters("who welld horly")
# cycle_letters("uoogit")

