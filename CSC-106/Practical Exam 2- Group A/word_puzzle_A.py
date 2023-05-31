#Neil Daterao

#Program that prints mystery words from a list of words in a text file 

def get_wordlist ():
    """This function reads a list of words from a file called
    wordlist.txt and returns those words as a Python list of
    strings. It converts all letters to lower case letters.
    """
    datafile = open("wordlist.txt", 'r')
    wordlist = []
    for line in datafile:
        line = line.strip()
        wordlist.append(line.lower())
    return wordlist

def is_vowel(letter):
    """Checks whether the given letter is a vowel."""
    return letter.lower() in "aeiouy"

def count_vowels(word):
    """Counts how many vowels the given word contains."""
    vowel_num = 0
    for char in word:
        if is_vowel(char):
            vowel_num += 1
    return vowel_num

def mystery_words():

    #Variables for the list of words, and character we don't want in the word 
    wordlist = get_wordlist()
    char = "s" 

    #Iterate through the words in the list 
    for word in wordlist:

        #Only look at words with a length of 7 characters, and then count the vowels. 
        if len(word) == 7:
            vowel_num = count_vowels(word)

            #If the number of vowels in the word is 1 and the character we don't want isn't in the word, we can then print the word 
            if (vowel_num == 1) and (char not in word):
                print(word)

           
                


# Replace this comment with your function definition

### DO NOT DELETE THIS LINE: beg testing

mystery_words()
