import pickle

class History:
    def __init__(self,name,player_id):
        self.name = str(name).replace(".","")+".power" #Used to save
        self.id = player_id #Used to identify player. Set to 0 for now. 
        self.history = [[-1,-1]] #Human, AI

    def add_move(self,first_move,second_move): #Add in saving capability
        self.history.append([first_move,second_move])
        file = open('savefiles/'+self.name,'wb')
        pickle.dump(self, file)
        file.close()

    def scan_move_series(self,move_series): #Scans in a given string of, HELPER
        results = [0,0] 
        for index in range(len(self.history)-len(move_series)):
            if self.history[index:index+len(move_series)] == move_series:
                results[self.history[index+len(move_series)][0]] += 1 
        return results

    def get_zero_count(self):
        results = [0,0]
        for index in range(len(self.history)):
            active_value = self.history[index][0]
            if active_value in [0,1]:
                results[active_value] += 1
        return results

    def scan_move_history(self,history):
        memory = history #stupid
        results = [self.get_zero_count()]
        for i in range(len(memory)):
            if results[-1] == [0,0]:
                return results #Break early when no more matches. Do it first to cover turn 0. 
            move_series = memory[-(i+1):]
            results.append(self.scan_move_series(move_series))
        return results