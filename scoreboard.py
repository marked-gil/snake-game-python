from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self, score=0):
        super().__init__()
        self.score = score
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.setposition(0, 270)
        self.penup()
        self.color("white")
        self.display_score()
    
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()
        
    def add_score(self):
        self.score += 1
        self.display_score()
