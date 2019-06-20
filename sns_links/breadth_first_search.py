# breadth first search
from collections import deque
import pickle

# input name to user_id
def name_to_user_id(name):
    nicknames = pickle.load(open("nicknames_dic.pickle", "rb"))
    if name in nicknames:
        user_id = nicknames[name]
        return user_id
    else:
        print("the nickname does not exist")

        
# detect steps from user to jacob based on user_id
def detect_steps_to_jacob(user_id):
    search_deque = deque()    # make new que
    searched = []    # checked persons list
    graph_table = pickle.load(open("sns_links_graph_table.pickle", "rb"))
    
    if user_id in graph_table:
        search_deque += graph_table[user_id]    # add all adjacent nodes to search queue
    else:
        print("the user does not exsit")
        return False
        
    while search_deque:
        user = search_deque.popleft()
        if user not in searched:
            searched.append(user)
            if user == 23:
                print("steps from you to jacob:", len(searched))
                print("routes:", searched)
                return True
            else:
                search_deque += graph_table[user]
    return False

while True:
    name = input("input your nickname>")
    user_id = name_to_user_id(name)
    detect_steps_to_jacob(user_id)
