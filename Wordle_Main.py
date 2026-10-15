from Worlde_Game import *
from Wordle_Tournament import *

if __name__ == "__main__":

    game = Game() 
    tournament = Tournament(6,game)

    tournament.play()