def count_words(text, words):
    count = 0
    for word in words:
        if not (text.lower()).find(word.lower()) == -1:
            count+=1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

#def count_words(text, words):
#    text = text.lower()
#    count = count = sum(word in text for word in words)
#    
#    return count