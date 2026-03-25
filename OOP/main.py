from turtle import Turtle, Screen
from prettytable import PrettyTable

# Object creation

# Penny = Turtle()
# print(Penny)
# Penny.shape("turtle")
# Penny.color("green")
# Penny.forward(100)                       # Object Methods
#
# # Object attributes
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()                    # Object construction

table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])

# print(table.align)

table.align = "l"                       # Align the table content with left margin

print(table)




