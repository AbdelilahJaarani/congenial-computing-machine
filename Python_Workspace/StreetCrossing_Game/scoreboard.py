from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-220,265)
        self.scoring()

    
    def update_score(self):
        self.clear()
        self.goto(-220,265)
        self.write(f"Level: {self.score} ", True, "center",FONT)
        



    def scoring(self):
        self.score = 1
        self.write(f"Level: {self.score} ", True, "center",FONT)

        
        
    def new_lw(self):
        self.score +=1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center",FONT)