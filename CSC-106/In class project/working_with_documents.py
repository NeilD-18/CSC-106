
reviews = [["A", "series", "of", "escapades", "demonstrating", "the", "adage", "that", "what", "is", "good", "for", "the", "goose", "is", "also", "good", "for", "the", "gander", ",", "some", "of", "which", "occasionally", "amuses", "but", "none", "of", "which", "amounts", "to", "much", "of", "a", "story", "."],
           ["This", "quiet", ",", "introspective", "and", "entertaining", "independent", "is", "worth", "seeking", "."],
           ["Even", "fans", "of", "Ismail", "Merchant", "'s", "work", ",", "I", "suspect", ",", "would", "have", "a", "hard", "time", "sitting", "through", "this", "one", "."],
           ["A", "positively", "thrilling", "combination", "of", "ethnography", "and", "all", "the", "intrigue", ",", "betrayal", ",", "deceit", "and", "murder", "of", "a", "Shakespearean", "tragedy", "or", "a", "juicy", "soap", "opera", "."],
           ["Aggressive", "self-glorification", "and", "a", "manipulative", "whitewash", "."],
           ["A", "comedy-drama", "of", "nearly", "epic", "proportions", "rooted", "in", "a", "sincere", "performance", "by", "the", "title", "character", "undergoing", "midlife", "crisis", "."],
           ["Narratively", ",", "Trouble", "Every", "Day", "is", "a", "plodding", "mess", "."],
           ["The", "Importance", "of", "Being", "Earnest", ",", "so", "thick", "with", "wit", "it", "plays", "like", "a", "reading", "from", "Bartlett", "'s", "Familiar", "Quotations"],
           ["But", "it", "does", "n't", "leave", "you", "with", "much", "."],
           ["you", "could", "hate", "it", "for", "the", "same", "reason", "."],
           ["There", "'s", "little", "to", "recommend", "Snow", "Dogs", ",", "unless", "one", "considers", "cliched", "dialogue", "and", "perverse", "escapism", "a", "source", "of", "high", "hilarity", "."],
           ["Kung", "Pow", "is", "Oedekerk", "'s", "realization", "of", "his", "childhood", "dream", "to", "be", "in", "a", "martial-arts", "flick", ",", "and", "proves", "that", "sometimes", "the", "dreams", "of", "youth", "should", "remain", "just", "that", "."],
           ["The", "performances", "are", "an", "absolute", "joy", "."],
           ["Fresnadillo", "has", "something", "serious", "to", "say", "about", "the", "ways", "in", "which", "extravagant", "chance", "can", "distort", "our", "perspective", "and", "throw", "us", "off", "the", "path", "of", "good", "sense", "."],
           ["I", "still", "like", "Moonlight", "Mile", ",", "better", "judgment", "be", "damned", "."],
           ["A", "welcome", "relief", "from", "baseball", "movies", "that", "try", "too", "hard", "to", "be", "mythic", ",", "this", "one", "is", "a", "sweet", "and", "modest", "and", "ultimately", "winning", "story", "."]]


def average_doc_length(reviews): 
    
    total_words = 0 
    
    for i in range(0,len(reviews)): 
        for j in range(0,len(reviews[i])): 
            
            total_words += 1

    average_num = total_words / len(reviews)


    
    
    return average_num


def collection_frequency(reviews, word):
    word_count = 0 
    for i in range(0,len(reviews)): 
        for j in range(0,len(reviews[i])): 
            if reviews[i][j] == word:
                word_count += 1
    return word_count



def document_frequency(reviews, word):
    doc_count = 0 

    for i in range(0,len(reviews)): 
        for j in range(0,len(reviews[i])): 
            if reviews[i][j] == word:
                doc_count += 1
                break 

    return doc_count 


print(average_doc_length(reviews))
print(collection_frequency(reviews, "is"))
print(document_frequency(reviews, "of"))
