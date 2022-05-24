import turtle,random

window = turtle.Screen()
window.bgcolor('black')
window.setup(900,700)
I = turtle.Turtle()
I.speed(0)

I.hideturtle()

def starfil(n,dlina):
    I.left(random.randint(10,350))
    I.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            I.forward(dlina)
            angle = n//2 * 360 / n
            I.left(angle)
    I.end_fill()

for i in range(50):
    x = random.randint(-425,425)
    y = random.randint(-325,325)
    I.color('yellow')
    I.up()
    I.setpos(x,y)
    I.down()
    size = random.randint(10,20)
    vershina = random.choice([5,7,9,11,13,15])
    starfil(vershina,size)

def move(x,y):
    I.up()
    I.setpos(x,y)
    I.down()
    size = random.randint(10,20)
    vershina = random.choice([5,7,9,11,13,15])
    starfil(vershina,size)

window.onclick(move)
window.listen()
