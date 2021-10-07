import random
import colorgram
import turtle as t

timmy = t.Turtle()

'''Extract color from image'''''
# colors = colorgram.extract('hirst.jpg', 25)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     # store in tuple
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

'''RGB colors extracted'''
list_of_colors = [
    (199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
    (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
    (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
    (172, 153, 159), (212, 183, 177), (176, 198, 203)
]
t.colormode(255)
color = random.choice(list_of_colors)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
# between 270 and 360 degrees from center
timmy.setheading(225)
# to adjust the position
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(list_of_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()
