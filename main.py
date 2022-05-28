# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    f =  open(filename)
    text = f.read()
    
    return text


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    list = text.split()
    
    words_dictionary = {}

    for word in list:
        words_dictionary[word] = list.count(word)

    return words_dictionary


print(read_file_content("./story.txt"))
print(count_words())
