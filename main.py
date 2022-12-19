import turtle
import string
import pandas
t=turtle.Turtle()
t.penup()
t.color("black")
t.hideturtle()
screen=turtle.Screen()
image="./us-states-game-start/blank_states_img.gif"
screen.title("U.S.A based game")
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("./us-states-game-start/50_states.csv")
#data_dict=data.to_dict()
#print(data_dict)
#states=[]
game_is_on=[]
while len(game_is_on)<50:
    answer_input = screen.textinput(title=f"{len(game_is_on)}/50 correct", prompt="guesss the state")
    for row in data["state"]:
        if(row.lower()==answer_input.lower()):
            game_is_on.append(row)
            match=data[data.state==row]
            x_cordinate=int(match.x)
            y_cordinate=int(match.y)
            t.goto(x_cordinate,y_cordinate)
            t.write(row)












screen.exitonclick()
