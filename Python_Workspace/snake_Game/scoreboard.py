from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial",12,"normal")

with open ("high_score.txt","r") as data:
     HIGHSCORE= data.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = HIGHSCORE
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update()
        self.hideturtle()
    
    #In dieser Lösung wurde eine neue Methode update_scoreboard() erstellt, 
    #die die vorherige Anzeige des Scoreboards löscht und das aktualisierte Scoreboard mit der neuen Punktzahl neu schreibt
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", False, ALIGMENT, FONT)

    def update_Highscore(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open ("high_score.txt", "w") as data:
                data.write(str(self.highscore))
                  
        self.score = 0
        self.update()

   # def game_over(self):
       # self.goto(0,0)
       # self.write("GAME OVER", False, ALIGMENT, FONT)

    
    def get_food(self):
        self.score += 1
        self.update()
        
       
       
        
    
        
