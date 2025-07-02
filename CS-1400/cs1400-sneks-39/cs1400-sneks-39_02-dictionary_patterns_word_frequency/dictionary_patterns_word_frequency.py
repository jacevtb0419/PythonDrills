from cisc108 import assert_equal
def count_words(words):
    word_count = {}
    words = words.split(",")
    
    for word in words:
        
        word = word.strip()
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    return word_count

assert_equal(count_words("Lunch Dinner, Lunch"), {"Lunch": 2, "Dinner": 1})
assert_equal(count_words("Twelve, Twelve, Twelve"), {"Twelve": 3} )