import random

courses = []
currDay = 0 #index of current day
currHours = 1 #how many hours the course lasts
currMins = 0 #how many additional minutes the course lasts
currCol = 0 #color index

def setup():
    size(1000, 600)
    stroke(0)
    fill(255)
    textSize(25)
    frameRate(30)

# class courseBlock(object):
#     #init x y , class time, course name, r g b colors
#     def __init__(self, xCoor, yCoor, duration, title, r=random.randint(0,255), g=random.randint(0,255), b=random.randint(0,255)):
#         self.fill(r, g, b)
#         self.rect(xCoor, yCoor, 100, h)
#         self.text(title)

def draw():
    background(255)
    #global vars
    global currDay, currHours, currMins, currCol
    a = 250

    for num in range(len(courses)):
        fill(150, 150, 150,a)
        stroke(0,0)
        rect(courses[num][0],courses[num][1],95,courses[num][2])
    stroke(0)

    #make the grid
    Times = ["7AM","8AM","9AM","10AM","11AM","12PM","1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM", "12AM"]
    yCoor = 30 #y coordinate for grid boxes
    for hour in Times:
        xCoor = 70 #x coordinate for grid boxes
        for day in range(7):
            fill(255.0, 255.0, 255.0 ,0.0)
            rect(xCoor, yCoor, 100, 30) #x,y,w,h
            xCoor += 100
        yCoor+=30
    #adding times on the left side:
    yCoor = 60
    for time in Times:
        fill(0)
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
    fill(0)
    text("ACTIONS",825,25)
    fill(255,0)
    rect(775, 30, 200, 540)
    
    for newRect in range(2):
        fill(200,150,150)#box
        rect(800, 50+(newRect*30), 25, 25)
        fill(0)#minus sign
        rect(805, 60+(newRect*30), 15, 5)
        fill(150,200,150)#box
        rect(920, 50+(newRect*30), 25, 25)
        fill(0)#plus sign
        rect(925, 60+(newRect*30), 15, 5)
        rect(930, 55+(newRect*30), 5, 15)
    text("Hours: "+str(currHours),825,70)
    text("Mins: "+str(currMins),825,100)
    
    text("Click and drag\nthe mouse on \nthe screen to fill\nin time slots\n\nThe Hours and\nMins change the\nheight of the\ncursor", 785, 200)

    if mousePressed:
        if mouseX<690 and mouseX>70:
            if mouseY<550 and mouseY>30:
                rect(mouseX, mouseY, 100, 20)
                courses.append([mouseX,mouseY,currHours*30+int(currMins/2)])
        elif mouseX > 920 and mouseX<945:
            if mouseY>50 and mouseY<75:
                if currHours ==8:
                    currHours=1
                else:
                    currHours+=1
            elif mouseY>80 and mouseY<105:
                if currMins ==59:
                    currMins=0
                else:
                    currMins+=1
        elif mouseX>800 and mouseX<825:
            if mouseY>50 and mouseY<75:
                if currHours ==1:
                    currHours=8
                else:
                    currHours-=1
            elif mouseY>80 and mouseY<105:
                if currMins ==0:
                    currMins=59
                else:
                    currMins-=1
