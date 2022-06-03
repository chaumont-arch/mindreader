import random
import debug
from scipy.stats import binom_test

class AI:
    def __init__(self,p_floor):
        self.p_floor = p_floor

    def interleave(self,base_matches,new_matches):
        return_matches = []
        first_index = min(len(base_matches),len(new_matches))
        for i in range(first_index):
            return_matches.append([base_matches[i][0]+new_matches[i][0],base_matches[i][1]+new_matches[i][1]])

        if len(base_matches) > len(new_matches):
            for i in range(first_index,len(base_matches)):
                return_matches.append([*base_matches[i]])
        else:
            for i in range(first_index,len(new_matches)):
                return_matches.append([*new_matches[i]])

        return return_matches

    def instance_to_p_value(self,results): 
        if results == [0,0]:
            return 1
        hits = min(results[0],results[1])
        trials = results[0] + results[1]
        return binom_test(x=hits,n=trials,p=1/2,alternative='less')

    def interpret_results(self,results): #Converts a match list to a probability
        best_probability = 2
        best_index = -1
        if debug.show_ai_thoughts:
            print("Counts at {}".format(results))

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
        

    def interpret_history_with_memory(self,move_history,memory):
        #get each history's match count
        #merge into one
        #generate probabilities
        #interpret
        total_matches = []
        for history in memory:
            matches = history.scan_move_history(move_history)
            total_matches = self.interleave(total_matches,matches)
        results = self.interpret_results(total_matches)

        best_results = results[0]
        best_probability = results[1]

        if debug.show_terse_thoughts:
            print("AI Prediction:\t0: {}\t1: {}\tp={}\n".format(*best_results,best_probability))

        if (best_probability > self.p_floor) or (best_results[0] == best_results[1]):
            if debug.show_ai_thoughts:
                print("No prediction strong enough to use\n")
            return random.randint(0,1)
        else:
            if debug.show_ai_thoughts:
                print("Prediction of {}\n".format(int(best_results[0]<best_results[1])))
            if best_results[0] > best_results[1]:
                return 0
            else:
                return 1

        