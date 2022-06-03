import random
import debug

class AI:
    def __init__(self,p_floor):
        self.p_floor = p_floor

    def interpret_history_with_memory(self,move_history,memory):
        best_probability = 2
        best_results = None

        for history in memory:
            if debug.show_ai_thoughts:
                print("\nEvaluating {}: ".format(history))
                if debug.show_full_history:
                    print("History: {}".format(history.history))
                    
            valuation = history.evaluate_move_history(move_history)
            if best_probability > valuation[1]:
                best_probability = valuation[1]
                best_results = valuation[0]

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
