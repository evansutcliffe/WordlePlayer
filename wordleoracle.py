import numpy as np
import random 

class WordleOracle ():
        def __init__ (self):
            self.secret_word = ""
            self.playing = False
            self.turn = 0
            self.dictionary = get_possible_words()
            self.results_list = []
            
        def play (self):
            self.secret_word = random.choice(self.dict)
            self.turn = 0
            self.playing = True
            
        def get_word(self):
            return self.secret_word
        
        def set_word(self,word):
            self.secret_word = word
            
        def test_guess(self,guess,testing=False,print_vals=False):
            
            if not isinstance(guess, str): ## check inputs
                raise ValueError(guess,"not a string")
            guess = guess.lower()
            if guess not in self.dictionary and not testing:# (disabled for testing)
                raise ValueError(guess,"not a valid 5 letter word")
            results = np.zeros((5),dtype=int)
            secret_word = self.secret_word

            for i in range(5): #  not optimised for speed
                if guess[i] == secret_word[i]:
                    results[i]=2
            for i in range(5):
                is_green = results[i]==2
                is_yellow =  guess[i] in secret_word and not is_green # potentially is yellow
                letter_green_count = 0
                for j in range(5):
                    if guess[j] == guess[i] and results[j]==2:
                        letter_green_count+=1
                letter_yellow_count = 0
                for j in range(i):
                    if guess[j] == guess[i] and results[j]==1:
                        letter_yellow_count+=1
                more_yellow_required = secret_word.count(guess[i]) -  (letter_green_count + letter_yellow_count) >=1
                
                if is_yellow and more_yellow_required:
                    results[i]=1
                if print_vals:
                    print(guess[i], "for guess", guess, "in", secret_word," is ",colourmap[results[i]])
            self.results_list.append(results)
            self.turn +=1
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
