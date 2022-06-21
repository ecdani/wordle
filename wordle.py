
"""
Trying to get best five initial words for wordle counterreloj
@author: Dani
"""

import config
from json import load
import strategies


def main():
    load_word_list()
    calculate_character_probabilities()
    print(strategies.greedy_search())


def load_word_list():
    txt_file = open("list.txt", "r", encoding='utf8')
    file_content = txt_file.read()
    config.content_list = file_content.splitlines()
    txt_file.close()


def calculate_character_probabilities():
    total_amount_characters = {}
    for word in config.content_list:
        for position, character in enumerate(word):
            if character not in config.alpha:
                config.alpha[character] = {}
            if position not in config.alpha[character]:
                config.alpha[character][position] = 0
            config.alpha[character][position] += 1
            if position not in total_amount_characters:
                total_amount_characters[position] = 0
            total_amount_characters[position] += 1
    for character in config.alpha:
        for position in config.alpha[character]:
            config.alpha[character][position] = config.alpha[character][position] / \
                total_amount_characters[position]


main()
