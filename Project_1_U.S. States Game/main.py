import pandas as pd
import turtle as t
import time

#Screen Setup
screen=t.Screen()
screen.setup(730,500)
screen.tracer(0)
screen.bgpic(rf"100-Days_Python_Projects\Project_1_U.S. States Game\blank_states_img.gif")

#Turtle Setup
tur=t.Turtle()
tur.color("black")
tur.hideturtle()
tur.pu()

#Read csv data
data= pd.read_csv(rf"100-Days_Python_Projects\Project_1_U.S. States Game\50_states.csv")

game_is_on=True
guesses_state=[]
while game_is_on:
    time.sleep(0.1)

    
    input_text=screen.textinput(title="US Guess prompt",prompt="Enter the state name:")

    # Handle cancel or exit
    if input_text is None or input_text.title() == "Exit":
        game_is_on=False
        break

    input_text=input_text.title()
    if input_text in data.state.values:
        guesses_state.append(input_text)
        tur.goto(data[data.state== input_text].x.values[0],data[data.state== input_text].y.values[0])
        tur.write(data[data.state== input_text].state.values[0],align="center",font=("arial",8,"normal"))
        screen.update()


# Optionally show missed states on screen in red    
xs=[]
ys=[]
not_guessed=[states for states in data.state.values if states not in guesses_state]
for states in not_guessed:
    xt=data[data.state==states].x.item()
    xs.append(xt) 
    yt=data[data.state==states].y.item() 
    ys.append(yt)
        
new_dict={'state':not_guessed,
          'x':xs,
          'y':ys}

new_df=pd.DataFrame(new_dict)
new_df.to_csv(rf"100-Days_Python_Projects\Project_1_U.S. States Game\Learning_task.csv")

# Optionally show missed states on screen in red
tur.color("red")
for ng in not_guessed:
    tur.goto(new_df[new_df.state== ng].x.values[0],new_df[new_df.state== ng].y.values[0])
    tur.write(new_df[new_df.state== ng].state.values[0],align="center",font=("arial",8,"normal"))
screen.update()   


screen.mainloop() 
