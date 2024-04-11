#File: HW6.py
#Author: Max Allen
#UT EID: mca2773
#Course: CS303E
# I am going to use my knowledge on python's data structures 
# and file reading to analyze word distribution of poems.


stop_words = {"a", "am", "an", "and", "are", "as", "at", "be", "but", "by",
              "for", "i", "if", "in", "into", "is", "it", "its", "my", "nor",
              "not", "of", "on", "or", "so", "than", "that", "the", "then",
              "this", "to", "too", "will", "with"}

def count_words(filename):
    """
    Counts how many times each word appears in a file.

    Parameters
    ----------
    filename: str
        Name of the file that we are going to read and analyze. 

    Returns
    -------
    dictionary: dict
        Words as keys and counts as values
    """
    file_variable = open(filename, "r")
    poem = file_variable.read()
    dictionary = ({})
    wordslist = poem.split()
    for i in range(len(wordslist)):
        wordslist[i] = wordslist[i].strip("!\\\"#$%&'()*+,-./:;<=>?@[]^_`{|}~")
        wordslist[i] = wordslist[i].replace("-", "")
        wordslist[i] = wordslist[i].replace("'", "")
        wordslist[i] = wordslist[i].replace("_", "")
        wordslist[i] = wordslist[i].lower()
    for word in wordslist:
        dictionary[word] = 0
    for word in wordslist:
        if word in dictionary:
            dictionary[word] += 1  
    for item in stop_words:
        if item in dictionary:
            dictionary.pop(item)
    file_variable.close()
    return dictionary

def find_max(word_counts):
    """
    Finds which value in a dictionary is greatest

    Parameters
    ----------
    word_counts: dict
        Any dict with numerical values, but made for the count_words function

    Returns
    -------
    poople: tuple
        A tuple containing the most frequent word and its frequency
    """
    max = 0
    word = ""
    for key in word_counts:
        if word_counts[key] > max:
            max = word_counts[key]
            word = key
    poople = (word, max)
    return poople

def find_same_words(words1, words2):
    """
    Finds shared words between two lists

    Parameters
    ----------
    words1:
        First list/set of words to compare
    words2:
        Second list/set of words to compare
    
    Returns
    -------
    sameset:
        A set of all of the words in common
    """
    words1 = set(words1)
    words2 = set(words2)
    sameset = words1.intersection(words2)
    return sameset

def find_different_words(words1, words2):
    """
    Finds non-shared words between two lists

    Parameters
    ----------
    words1:
        First list/set of words to compare
    words2:
        Second list/set of words to compare
    
    Returns
    -------
    sameset:
        A set of all of the words in not in common    
    """
    words1 = set(words1)
    words2 = set(words2)
    diffset = words1.difference(words2)
    return diffset
def main():
    print(f'Count of "{find_max(count_words("raven.txt"))[0]}" is: {find_max(count_words("raven.txt"))[1]}')
    print(f'Count of "nevermore" is: {count_words("raven.txt")["nevermore"]}')
    print(f'Count of "raven" is: {count_words("raven.txt")["raven"]}')
    print()
    print(find_same_words(count_words("raven.txt"), count_words("road.txt")))
    print()
    print(find_different_words(count_words("road.txt"), count_words("raven.txt")))

if __name__ == '__main__':
    main()

