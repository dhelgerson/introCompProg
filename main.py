from random import randint
import json
import turtle as t

t.setworldcoordinates(-1,-1,5,5)
t.shape('circle')
t.hideturtle()
t.penup()

def createMatrix(rows,columns):
    return [[randint(0,1) for y in range(columns)] for x in range(rows)]

matrix = createMatrix(5,5)

for row in enumerate(matrix):
    for item in enumerate(row[1]):
        if item[1]:
            t.goto(row[0],item[0])
            t.stamp()
        print(row[0],item[0],item[1])
        
input()