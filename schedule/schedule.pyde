import random
def setup():
    size(1000, 600)
    stroke(0)
    background(192, 64, 0)
    fill(255)
    textSize(25)

class courseBlock(object):
    #init x y , class time, course name, r g b colors
    def __init__(self, xCoor, yCoor, duration, title, r=random.randint(0,255), g=random.randint(0,255), b=random.randint(0,255)):
        self.fill(r, g, b)
        self.rect(xCoor, yCoor, 100, h)
        self.text(title)

def draw():
    #global vars
    global currDay, currHours, currMins, currRed, currGreen, currBlue
    currDay = 0 #index of current day
    currHours = 0 #how many hours the course lasts
    currMins = 0 #how many additional minutes the course lasts
    currRed = 0 #current r value
    currGreen = 0 #current g value
    currBlue = 0 #current b value

    #make the grid
    Times = ["7AM","8AM","9AM","10AM","11AM","12PM","1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM", "12AM"]
    yCoor = 30 #y coordinate for grid boxes
    for hour in Times:
        xCoor = 70 #x coordinate for grid boxes
        for day in range(7):
            fill(255.0, 255.0, 255.0 ,3.0)
            rect(xCoor, yCoor, 100, 30) #x,y,w,h
            xCoor += 100
        yCoor+=30
    #adding times on the left side:
    yCoor = 60
    for time in Times:
        fill(255)
        text(time, 5, yCoor)
        yCoor += 30
    #adding weekdays on the top
    Days = ["SUN","MON","TUE","WED","THUR","FRI","SAT"]
    xCoor = 90
    for day in Days:
        text(day, xCoor, 25)
        xCoor+=102
    #grid done
    
    #lists for options
    Days = ["SUN","MON","TUE","WED","THUR","FRI","SAT"]
    fill(255)
    text("ACTIONS",825,25)
    fill(255.0, 255.0, 255.0 ,3.0)
    rect(775, 30, 200, 540)
    
    for newRect in range(6):
        fill(200,150,150)#box
        rect(800, 50+(newRect*30), 25, 25)
        fill(0)#minus sign
        rect(805, 60+(newRect*30), 15, 5)
        fill(150,200,150)#box
        rect(920, 50+(newRect*30), 25, 25)
        fill(0)#plus sign
        rect(925, 60+(newRect*30), 15, 5)
        rect(930, 55+(newRect*30), 5, 15)
    text("Day: "+Days[currDay],825,70)
    text("Hours: "+str(currHours),825,100)
    text("Mins: "+str(currMins),825,130)
    text("Red: "+str(currRed),825,160)
    text("Green: "+str(currGreen),825,190)
    text("Blue: "+str(currBlue),825,220)
    
def mousePressed():
    global currDay
    if mouseX>800 and mouseX<825:
        if mouseY>50 and mouseY<75:
            if currDay==0:
                currDay = 7
            else: 
                currDay-=1
            text("Day: "+Days[currDay],850,70)
    else:
        fill(randint(255))
        rect(400, 400, 500, 500)
