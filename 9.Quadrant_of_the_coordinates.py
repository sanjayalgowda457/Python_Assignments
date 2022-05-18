#To find the Quadrant of the given coordinates
x=int(input("Enter the x coordinate:"))
y=int(input("Enter the y coordinate:"))
if (x > 0 and y > 0):
    print("The Entered Coordinates",x,y,"lies in First quadrant")

elif (x < 0 and y > 0):
    print("The Entered Coordinates",x,y,"lies in Second quadrant")

elif (x < 0 and y < 0):
    print("The Entered Coordinates",x,y,"lies in Third quadrant")

elif (x > 0 and y < 0):
    print("The Entered Coordinates",x,y,"lies in Fourth quadrant")

elif (x == 0 and y > 0):
    print("The Entered Coordinates",x,y,"lies in positive y axis")

elif (x == 0 and y < 0):
    print("The Entered Coordinates",x,y,"lies in negative y axis")

elif (y == 0 and x < 0):
    print("The Entered Coordinates",x,y,"lies in negative x axis")

elif (y == 0 and x > 0):
    print("The Entered Coordinates",x,y,"lies in positive x axis")

else:
    print("The Entered Coordinates",x,y,"lies at origin")