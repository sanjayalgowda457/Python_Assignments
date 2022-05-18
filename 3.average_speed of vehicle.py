t=[0,6,2,1,0.1,1.0,0.25,0.45,0.55,0.7,0.9]
t.sort()
print(t)
dt=t[-1]-t[0]#time interval=start time - end time
print("The time interval is:",dt)
d=[6,7.5,2.5,10.75,1.3,3.9,6.8,9.95]
d.sort()
print(d)
total_distance=sum(d)
print("The Total distance is",total_distance)
average_speed=((total_distance)/dt)
print("The average speed of the vehicle is",average_speed)