import turtle
import random

myT,tX,tY,tColor,tSize,tShape = [None]*6
shapeList=[]
playerT=[]
swidth,sheight = 500,500

if __name__ == "__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    shapeList=turtle.getshapes()
    for i in range(0,100):
        random.shuffle(shapeList)
        myT=turtle.Turtle(shapeList[0])
        tX=random.randrange(-swidth / 2, swidth/2)
        tY=random.randrange(-sheight/2, sheight/2)
        r = random.random(); g=random.random();b=random.random()
        tSize=random.randrange(1,3)
        playerT.append([myT,tX,tY,tSize,r,g,b])

    for tList in playerT:
        myT=tList[0]
        myT.color((tList[4],tList[5],tList[6]))
        myT.pencolor((tList[4],tList[5],tList[6]))
        myT.turtlesize(tList[3])
        myT.goto(tList[1],tList[2])
    turtle.done()