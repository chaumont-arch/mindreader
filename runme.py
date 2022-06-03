import game
import os
import pickle
import debug

def prep_save_folder():
    try:
        os.mkdir("savefiles")
    except:
        pass

def load_all_files():
    power_files = []
    for file in os.listdir("savefiles"):
        if file.endswith(".power"):
            object = open("savefiles/"+file,"rb")
            power_files.append(pickle.load(object))
            object.close()
    return power_files

def get_profile(valid_ids):
    if debug.auto_id:
        return "0"
        
    id = input("Input ID: ")
    flag = (id in valid_ids) or (len(valid_ids) == 0)
    while not flag:
        mood = input("ID not found. Create new? (Y/N) ")
        if mood == "Y":
            flag = True
        else:
            id = input("ID")
            flag = (id in valid_ids)
    return id

def main():
    prep_save_folder()
    memories = load_all_files()

    valid_ids = []
    for memory in memories:
        valid_ids.append(memory.id)
    player_id = get_profile(valid_ids)

    active_game = game.Game(player_id)
    for memory in memories:
        active_game.load_memory(memory)
    active_game.print_memory_info()

    while True:
        active_game.round()

if __name__ == '__main__':
    main()
