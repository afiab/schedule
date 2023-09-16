def setup():
    size(1000, 600)
    stroke(0)
    background(192, 64, 0)

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
    yCoor = 50
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
