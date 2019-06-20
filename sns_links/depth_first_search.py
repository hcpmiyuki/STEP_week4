import pickle

# input name to user_id
def name_to_user_id(name):
    nicknames = pickle.load(open("nicknames_dic.pickle", "rb"))
    if name in nicknames:
        user_id = nicknames[name]
        return user_id
    else:
        print("the nickname does not exist")


searched = []    # checked persons list
graph_table = pickle.load(open("sns_links_graph_table.pickle", "rb"))

# detect steps from user to jacob based on user_id
def detect_steps_to_jacob(user_id):
    if user_id in graph_table:
        searched.append(user_id)
    else:
        print("the user does not exsit")
        return False
        
    if user_id == 23:
        del searched[0]
        print("steps from you to jacob:", len(searched))
        print("routes:", searched)
        return True
    
    for user in graph_table[user_id]:
        if user not in searched:
            detect_steps_to_jacob(user)
            
    return False


while True:
    name = input("input your nickname>")
    user_id = name_to_user_id(name)
    detect_steps_to_jacob(user_id)
    # initialize
    searched = []    # checked persons list
    graph_table = pickle.load(open("sns_links_graph_table.pickle", "rb"))
