def count_words(text):
    words = text.split()  
    num_words = {}

    for word in words:
        if word in num_words:  
            num_words[word] += 1  
        else:
            num_words[word] = 1  

    return num_words
text = input("Pls enter string of string$ ")
word_counts = count_words(text)
print(word_counts)
