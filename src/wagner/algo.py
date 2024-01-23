
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

        for column in range(1, len(possible) + 1):
            matrix[column].append(column)

        for row in range(1, len(matrix)):
            for column in range(1, len(word) + 1):

                tri = [matrix[row][column - 1], matrix[row - 1]
                       [column], matrix[row - 1][column - 1]]

                if word[column - 1] == possible[row - 1]:
                    matrix[row].append(min(tri))
                else:
                    matrix[row].append(min(tri) + 1)

        print(matrix[len(possible)][len(word)])
