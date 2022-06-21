
import config
import itertools

def brute_force_search():
    """
    Too many permutations :S we need to wait until the end of the universe or a bit more.
    """
    current_best_set = ()
    current_best_set_score = 0
    for p in itertools.permutations(config.content_list, 5):
        new_score = score(p)
        if new_score > current_best_set_score:
            current_best_set = p
            current_best_set_score = new_score
            print(current_best_set_score, current_best_set)

def greedy_search():
    """
    """
    current_best = []
    current_best_score = 0
    current_set = []
    while len(current_set) < 5:
        for word in config.content_list:
            current_score = individual_word_score(word, current_set)
            if current_score > current_best_score:
                current_best = word
                current_best_score = current_score
        current_set.append(current_best)
        current_best = []
        current_best_score = 0
    return current_set

def individual_word_score(current_word,set = None):
    used_letters = []
    if set:
        for word in set:
            for character in word:
                if character not in used_letters:
                    used_letters.append(character)
    
    score = 0
    for position, character in enumerate(current_word):
        if current_word[position] not in used_letters:
            score += config.alpha[current_word[position]][position]
            used_letters.append(current_word[position])
    return score

def score(set=['BOGAN', 'BOGAR', 'BOGAS', 'BOGUE', 'BOHIO']):
    used_letters = []
    score = 0
    for word in set:
        counter = 0
        for position in (0, 1, 2, 3, 4):
            if word[position] not in used_letters:
                counter += config.alpha[word[position]][position]
                used_letters.append(word[position])
        score += counter
    return score