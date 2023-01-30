# your code goes here!# your code goes here!

# title_cased_nm = " ".join(list(map(lambda word: word[0].capitalize() + word[1:], name.split(' '))))
import ipdb

class Anagram:

    def __init__(self, word):
        # ipdb.set_trace()
        self.word = word

    # ["listen", "poison", "hello"]
    def match(self, word_list: list) -> list:
        matched_words = []
        for word in word_list:
            matched_words.append(word) if sorted(word) == sorted(self.word) else None
       
        return matched_words

    pass