import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.hideturtle()
        self.color('white')

    def write_score(self):
        self.write(arg=f'Level: {self.level}', font=FONT, move=False, align='left')

    def update_score(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', font=FONT, move=False, align='center')




