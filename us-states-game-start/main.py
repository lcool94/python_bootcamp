import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_dict = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 states',
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_dict if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in states_dict:
        guessed_states.append(answer_state)
        print(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == answer_state]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(answer_state)


# def get_mouse_click_coor(x, y): print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# # turtle.exitonclick()

# flag = 0
# thoi_han = 20
# tong = 1000000000
# while True:
#     tong = tong + (tong*8)/100
#     flag +=1
#     print(f'lãi năm thứ {flag}:{tong}')
#     if flag == thoi_han:
#         break
