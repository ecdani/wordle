
"""
Trying to get best five initial words for wordle counterreloj
@author: Dani
"""
import itertools

# Probability of letters in each position in Spanish
alpha = {'A': (11.1, 21.7, 6.6, 16.9, 20),
         'B': (5, 1.6, 3.3, 2, 0.1),
         'C': (10.9, 1.6, 5.9, 3.7, 0.1),
         'D': (3.8, 1, 4.4, 5.7, 0.2),
         'E': (3.2, 13.3, 6.9, 13.5, 15.8),
         'F': (4.7, 0.5, 1, 0.2, 0),
         'G': (3.5, 0.7, 3.7, 2.8, 0),
         'H': (3.7, 0.7, 0.3, 1.3, 0),
         'I': (1.1, 11.8, 7.2, 9.1, 1.7),
         'J': (1.3, 0.1, 2.3, 1.9, 0.1),
         'K': (0.1, 0, 0.1, 0, 0),
         'L': (5, 4.2, 8.6, 4.9, 2.1),
         'M': (5.3, 1.2, 3.9, 2.6, 0.1),
         'N': (1.9, 2.6, 7.2, 3.5, 9),
         'Ñ': (0.1, 0.3, 1.5, 0.6, 0),
         'O': (3.4, 13.2, 4, 8, 24.2),
         'P': (8, 1.2, 1.9, 1.5, 0.1),
         'Q': (0.6, 0.1, 0.4, 0, 0),
         'R': (6.2, 7.2, 10.7, 5.9, 5.5),
         'S': (5.7, 1.8, 6.3, 3.2, 20.3),
         'T': (7.3, 0.7, 5.5, 7.6, 0.1),
         'U': (1.6, 12.7, 4.7, 2.1, 0.1),
         'V': (5.2, 0.9, 1.5, 1.6, 0),
         'W': (0, 0, 0, 0.1, 0),
         'X': (0.1, 0.6, 0.4, 0.1, 0.1),
         'Y': (0.5, 0.3, 0.8, 0.2, 0.1),
         'Z': (0.6, 0.1, 1.4, 1.1, 0.7)
         }


def main():
    txt_file = open("list.txt", "r", encoding='utf8')
    file_content = txt_file.read()
    content_list = file_content.splitlines()
    txt_file.close()
    current_best_set = ()
    current_best_set_score = 0

    # Too many permutations :S we need to wait until the end of the universe or a bit more.
    for p in itertools.permutations(content_list, 5):
        new_score = score(p)
        if new_score > current_best_set_score:
            current_best_set = p
            current_best_set_score = new_score
            print(current_best_set_score, current_best_set)


def score(set=['BOGAN', 'BOGAR', 'BOGAS', 'BOGUE', 'BOHIO']):
    used_letters = []
    score = 0
    for word in set:
        counter = 0
        for position in (0, 1, 2, 3, 4):
            if word[position] not in used_letters:
                counter += alpha[word[position]][position]
                used_letters.append(word[position])
        score += counter
    return score

main()
