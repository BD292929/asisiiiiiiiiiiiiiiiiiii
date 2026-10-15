from Worlde_Game import *

class Tournament():
    def __init__(self, tries, game : Game):
        self.tries = tries
        self.game = game

    def play(self):

        selected_word = self.game.random_word()

        i = 0

        while(i < self.tries):

            print(f"try number {i+1}:")

            if(self.game.round(selected_word) == False):
                i-=1

            i+=1

            print("---------------")

        print(f"the word was: {selected_word}")