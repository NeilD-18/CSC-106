# Don't forget to add an appropriate header comment which contains
# information about the author and a description of this program's
# purpose.


def read_word_dict (filename):
    """Read a translation dictionary from a file and return it as a dictionary."""
    file = open(filename, 'r')
    worddict = {}
    for line in file:
        line = line.strip()
        [english, german] = line.split(":")
        worddict[english] = german   
        print(english, german)
    file.close()
    return worddict


def pretty_print_dict(dictionary): 
    
    for (key,value) in dictionary.items(): 
        print(key, "." * (16-len(key)),value)
        
       
def translate(string,dictionary):
    x = string.split()
    for word in x:
        print(dictionary[word]) 



# Change the file name to try out your own dictionary.

translation_dict =  read_word_dict ("eng-spl.txt")
translate("the dog barks", translation_dict) 


