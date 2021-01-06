import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Method to find the coordinates on the image (these are already stored by state in the 50_states.csv)
# def get_mouse_click_coor(x, y):
# 	print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []


while len(guessed_states) < 50:
	#Use the data from the 50_states.csv file to create a prompt to the user
	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
		prompt="What's another state's name?").title()

	if answer_state == "Exit":
		missing_states = [state for state in all_states if state not in guessed_states:]
		# missed_states = []
		# for state in all_states:
		# 	if state not in guessed_states:
		# 		missed_states.append(state)
		new_data = pandas.DataFrame(missed_states)
		new_data.to_csv("states_to_learn.csv")

		break
	
	if answer_state in all_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer_state)




