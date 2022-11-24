from turtle import Screen, Turtle

# timmy = Turtle()
# timmy2 = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "yellow")
#
# my_screen = Screen()
# print(my_screen.canvwidth)
#
# timmy.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Chamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
