import history
import os
import pickle

def load_all_files():
    power_files = []
    for file in os.listdir("savefiles"):
        if file.endswith(".power"):
            object = open("savefiles/"+file,"rb")
            power_files.append(pickle.load(object))
            object.close()
    return power_files

def main():
    memories = load_all_files()
    print("name\t\t\t\tid\tmove count")
    for memory in memories:
        print("{}\t\t{}\t{}".format(memory.name,memory.id,len(memory.history)))

if __name__ == '__main__':
    main()
