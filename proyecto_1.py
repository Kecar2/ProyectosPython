import turtle
import random

s = turtle.Screen()
s.title("Primer proyecto")

s.bgcolor("#faffb3")

#Crear jugadores
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

#Definir caracteristicas de jugador1
jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green", "green")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

#Definir caracteristicas de jugador2
jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("red", "red")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

#Punto de salida y final
jugador1.penup()
jugador1.goto(200, 200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-200, 225)
jugador1.showturtle()

#Punto de salida y final
jugador2.penup()
jugador2.goto(200, -200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-200, -170)
jugador2.showturtle()

dado = [1,2,3,4,5]

for i in range(20):
    if jugador1.pos() >= (200, 200):
        print("La tortuga Verde ha ganado")
        break
    elif jugador2.pos() >= (200, -200):
        print("La tortuga Roja ha ganado")
        break
    else:
        turno1 = input("Turno1 Enter para avanzar...")
        turno1 = random.choice(dado)
        print("Tu numero es: ",turno1,"\nAvanzas: ",turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Turno2 Enter para avanzar...")
        turno2 = random.choice(dado)
        print("Tu numero es: ",turno2,"\nAvanzas: ",turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)


turtle.done()