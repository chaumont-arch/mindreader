from scipy.stats import binom_test
import debug
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

    def instance_to_p_value(self,results): #Converts a [0s,1s] - move to AI - jk
        if results == [0,0]:
            return 1
        hits = min(results[0],results[1])
        trials = results[0] + results[1]
        return binom_test(x=hits,n=trials,p=1/2,alternative='less')

    def interpret_results(self,results): #Converts a match list to a probability
        best_probability = 2
        best_index = -1

        if debug.show_ai_thoughts:
            print("Values at: ",end="")

        for index in range(len(results)):
            active_probability = self.instance_to_p_value(results[index])
            if active_probability < best_probability:
                best_probability = active_probability
                best_index = index
            if debug.show_ai_thoughts:
                print("{} ".format(active_probability),end="")

        if debug.show_ai_thoughts:
            print(" ")
            
        return [results[best_index],best_probability]

    def evaluate_move_history(self,move_history):
        matches = self.scan_move_history(move_history)

        if debug.show_ai_thoughts:
            print("Counts at {}".format(matches))

        return self.interpret_results(matches)
        