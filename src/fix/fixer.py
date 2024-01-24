import os
import sys

functionPath = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(functionPath)

from wagner.algo import wagner_fischer

class spell_checker():

    def __init__(self):
        pass

    def manual_input(self):
        word = input("Word: ")
        return word

    def fix(self):
        word = self.manual_input()
        
        instance = wagner_fischer()

        filePath = os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "list.txt"))

        with open(filePath, "r") as f:
            data = [line.strip() for line in f]

        if word not in data:
            best_choice = [float("inf"), None]
            
            for possible in data:
                
                run = instance.wagner(word, possible)
                
                if run < best_choice[0]:
                    best_choice = [run, possible]
                    
            print(f"Possible Word: {best_choice[1]}")
            print(f"Distance: {best_choice[0]}")
        else:
            print("Given Word Is Correctly Spelled")
