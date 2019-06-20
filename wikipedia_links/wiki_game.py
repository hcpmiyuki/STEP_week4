# breadth first search

import pickle
import random
from collections import deque

# Determine start_word randomly
def start_word():
    pages = pickle.load(open("pages_dic.pickle", "rb"))
    num = random.randint(0,len(pages))
    return list(pages.keys())[num]


def word_to_id(word):
    pages = pickle.load(open("pages_dic.pickle", "rb"))
    
    # word to word_id
    if word in pages:
        word_id = pages[word]
        return word_id
    else:
        print("the word is not in wikipedia")
        return False


def detect_steps_from_start_to_end(s_word_id, e_word_id):
    search_deque = deque()    # make new que
    search_deque += [s_word_id]
    searched = []    # checked persons list
    data = {s_word_id: []}
    graph_table = pickle.load(open("wiki_links_graph_table.pickle", "rb"))
    
    if e_word_id not in graph_table:
        print("the end_word is not linked")
        return False

    if s_word_id in graph_table:
        search_deque += graph_table[s_word_id]    # add all adjacent nodes to search queue
    else:
        print("the start_word is not linked")
        return False
        
    while search_deque:
        word_id = search_deque.popleft()
        if word_id not in searched:
            searched.append(word_id)
            if word_id == e_word_id:
                return len(data[word_id])
            else:
                if word_id in graph_table:
                    search_deque += graph_table[word_id]
                    for id in graph_table[word_id]:
                        if id not in data:
                            data[id] = data[word_id] + [word_id]
    return False
    


def is_success(steps, acceptable_range):
    if steps >= acceptable_range["min"] and steps <= acceptable_range["max"]:
        return True
    else:
        return False
    
def success_message(steps, end_word):
    print("ok! this steps are ", steps)
    print("next start word:", end_word)
    print("next acceptable range: " + str(steps) + " to " + str(steps*10))
    

def failure_message(steps):
    if steps != False:
        print("game over! this steps are ", steps)

    
def wiki_game(acceptable_range, start_word):
    end_word = input("end word: ")
    s_word_id = word_to_id(start_word)
    e_word_id = word_to_id(end_word) 
    steps = detect_steps_from_start_to_end(s_word_id, e_word_id)
    print(steps)
    if is_success(steps, acceptable_range):
        success_message(steps, end_word)
        acceptable_range["min"] = steps
        acceptable_range["max"] = steps * 10
        return wiki_game(acceptable_range, end_word)
    
    else:
        failure_message(steps)
        return False
    
    
if __name__ == "__main__":
    print("fisrst acceptable range: 0 to 100000")
    print("start word: " + start_word())
    acceptable_range = {"min": 0, "max": 100000}
    wiki_game(acceptable_range, start_word())
