
import random

def load_words():
    word_list=["navgurukul","kindness","learning","swap","help","happy","stuggale","rainbow","computer","science","programming","players","water","condition","logic"]
    # WORDLIST_FILENAME = "/home/shivani/Desktop/hangman.py/words.py/word.txt"
    # print ("Loading word list from file...")
    # infile = open(WORDLIST_FILENAME, "r")
    # line = infile.readline()
    # word_list = str.split(line)
    # print ("  ", len(word_list), "words loaded.\n")
    return word_list

def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    
    return secret_word
