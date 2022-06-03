import history as h
import ai
import time
import sys

class Game:
    def __init__(self,id):
        self.id = id
        self.active_history = h.History(time.time(),self.id)
        self.memory = [self.active_history]
        self.ai = ai.AI(1/3)
        self.display_score = 0
        self.move_count = 0

    def load_memory(self,history):
        if history.id == self.id:
            self.memory.append(history)

    def get_input(self):
        feedin = input("Input value: ")
        if feedin in ["q","quit","exit","bye"]:
            sys.exit('Goodbye')
        try:
            feedin = int(feedin)
        except:
            pass
        while not isinstance(feedin,int):
            feedin = input("Invalid input received. Input value:")
            try:
                feedin = int(feedin)
            except:
                pass
        return feedin % 2

    def update_memory(self,move_pair): #Not needed?
        self.active_history.add_move(*move_pair)
        self.memory[0].add_move(*move_pair)

    def print_move(self,move_pair):
        print("Round {} results:".format(self.move_count))
        print("--------")
        print("Human: {}\tAI: {}".format(*move_pair))
        print("Current Score {}\n".format(self.display_score))

    def round(self):
        ai_move = self.ai.interpret_history_with_memory(self.active_history.history,self.memory)
        human_move = self.get_input()

        self.move_count += 1
        self.display_score += int(ai_move != human_move)*2-1
        self.active_history.add_move(human_move,ai_move)

        self.print_move([human_move,ai_move])
    
    def print_memory_info(self):
        if len(self.memory) > 1:
            print("{} memory file(s) loaded".format(len(self.memory)-1))