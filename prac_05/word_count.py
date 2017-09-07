key_words = {}
input_text = input("Text: ")
words = input_text.split()
for word in words:
    find_word = key_words.get(word, 0)
    if find_word is None:
        key_words[word] = 1
    else:
        key_words[word] = find_word + 1
words = list(key_words.keys())
longest_word = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, longest_word, key_words[word]))


