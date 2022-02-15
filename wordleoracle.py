import numpy as np
import random 

class WordleOracle (): # inherits from abstract class Shape
        def __init__ (self):
            self.secret_word = ""
            self.playing = False
            self.turn = 0
            self.dict = get_possible_words()
            self.results_list = []
            
        def play (self):
            self.secret_word = random.choice(self.dict)
            self.turn = 0
            self.playing = True
            
        def get_word(self):
            return self.secret_word
        
        def set_word(self,word):
            self.secret_word = word
            
        def test_guess(self,guess): # TODO / BUG, shouldn't return yellow if slot is already filled by green
            self.turn +=1
            secret_word = self.secret_word
            if not isinstance(guess, str):
                raise ValueError(guess,"not a string")
            if not len(guess)==5:
                raise ValueError(guess,"not 5 letter word")
            results = np.zeros((5))
            guess = guess.lower()
            for i in range(5): #  not optimised for speed
                if guess[i] == secret_word[i]:
                    results[i]=2
                elif guess[i] in secret_word: # TODO / BUG, shouldn't return yellow if slot is already filled by green
                    results[i] = 1
        #         else: 
        #           results[i] = 0
            self.results_list.append(results)
            return results

        

def load_words():
    with open('english-words-master/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

# demo print
# print('fate' in english_words)
# print(len(english_words))
# print(len(wordle_words))

def get_possible_words():
    return wordle_words.copy()

english_words = load_words()
wordle_words = [word for word in english_words if len(word)==5]



# my_sum = 0
# for (letter,freq) in letter_freqs:
#     my_sum+=freq
# print(my_sum)
# #normalise
# x = []
# for i in range(len(letter_freqs)):
#     (letter,freq) = letter_freqs[i]
#     x.append((letter,freq/my_sum))
# # to dict
# letter_freq_dict = {}
# for (letter,freq) in x:
#     letter_freq_dict[letter.lower()]=freq
    
# with open('letter_freq.json', 'w') as outfile:
# json.dump(letter_freq_dict, outfile)
