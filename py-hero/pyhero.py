"""PyHero Module"""

class Chart:
        def __init__(self,name,max):
            self.name = str(name)
            self.note_matrix = None
            self.selected_row=None
            self.score=0
            self.max_score=max
        def import_chart(self,chart_file):
            with open(chart_file,'r') as chartf:
                lines=chartf.readlines()
            self.note_matrix = [line.strip() for line in lines]
            self.selected_row=1
        def print_chart(self):
            print("Score: ",self.score)
            print(self.note_matrix[0][self.selected_row:])
            print(self.note_matrix[1][self.selected_row:])
            print(self.note_matrix[2][self.selected_row:])
            print(self.note_matrix[3][self.selected_row:])
            print(self.note_matrix[4][self.selected_row:])
        def step(self):
            self.selected_row +=1
        def submit(self,response,autostep=False):
            #response should be a list where no buttons pressed is 0 and button pressed is 1
            if self.end_check() is True:
                return False
            for i,key in enumerate(response):
                if int(key) == 1 and self.note_matrix[i][self.selected_row] == 'x':
                    self.score += 1
            if autostep == True:
                self.selected_row +=1
            return True
        def end_check(self):
            if self.note_matrix[0][self.selected_row-1] == "@":
                return True
            return False


