import random
def setup():
    size(1000, 600)
    stroke(0)
    background(192, 64, 0)

class courseBlock(object):
    #init x y , class time, course name, r g b colors
    def __init__(self, xCoor, yCoor, duration, title, r=random.randint(0,255), g=random.randint(0,255), b=random.randint(0,255)):
        self.fill(r, g, b)
        self.rect(xCoor, yCoor, 100, h)
        self.text(title)

def draw():
    #make the grid
    Times = ["7AM","8AM","9AM","10AM","11AM","12PM","1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM", "12AM"]
    yCoor = 30 #y coordinate for grid boxes
    for hour in Times:
        xCoor = 50 #x coordinate for grid boxes
        for day in range(7):
            rect(xCoor, yCoor, 100, 30) #x,y,w,h
            xCoor += 100
        yCoor+=30
    #adding times on the left side:
    yCoor = 60
    for time in Times:
        text(time, 20, yCoor)
        yCoor += 30
    #adding weekdays on the top
    Days = ["SUN","MON","TUE","WED","THUR","FRI","SAT"]
    xCoor = 90
    for day in Days:
        text(day, xCoor, 20)
        xCoor+=100
    #grid done
