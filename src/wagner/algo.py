
class wagner_fischer():
    
    def __init__(self):
        pass
    
    def manual_input(self):
        word = input("Misspelled Word: ")
        possible = input("Possible Word: ")
        return word, possible
    
    def wagner(self):
        word, possible = self.manual_input()
        
        matrix = []
        matrix = [[] for _ in range(len(possible) + 1)]
        
        
        for row in range(0, len(word) + 1):
            matrix[0].append(row)
            
        for column in range(1, len(word) + 1):
            matrix[column].append(column)
        
        
        
        
        
        for row in matrix:
            print(row) 
        
        
        
        
        
        
        