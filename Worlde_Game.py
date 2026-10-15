import random
import requests
import os

class Game:
    def __init__(self):
        self.green = "\033[42;30m"
        self.yellow = "\033[43;30m"
        self.close_color = "\033[0m"

    def random_word(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "common_5_letter_words.txt")

        with open(file_path, 'r', encoding='utf-8-sig') as file:
            words_list = file.read().splitlines()

        return random.choice(words_list)

    def check_word(self, word, r_word):

        final_word = [""] * 5

        for i in range(5):
            if word[i] == r_word[i]:
                final_word[i] = self.green + word[i] + self.close_color
            elif word[i] in r_word:
                final_word[i] = self.yellow + word[i] + self.close_color
            else:
                final_word[i] = word[i]

        return "".join(final_word)

    def validate_word_api(self, url: str, word: str) -> dict:
    
        key="&md=d"
        new_url=url+word+key
    
        response = requests.get(new_url, timeout=10)
        
        if(response.status_code == 200 and len(word) == 5):
            return True

        return False

    def round(self, rnd_w):
        guess = input("Your guess: ").strip().lower()

        
        if len(guess) != 5:
            print("You need a 5 letter word")
            return False

        if self.validate_word_api("https://api.datamuse.com/words?sp=", guess):
            print(self.check_word(guess, rnd_w))
            
            if guess == rnd_w.lower():
                print("Good job, you won!")
                
            return True
        
        else:
            print("None existing word")

        return False