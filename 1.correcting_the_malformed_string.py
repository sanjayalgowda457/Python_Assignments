# Correct the malformed time string , for e.g "5:70:65" to "6:11:05"
#enter in hour:minutes:seconds format
time="5:70:65"
x=int(time[0])
y=int(time[2:4])
z=int(time[5:7])
sec=(x*60*60) + (y*60) + z
print("The total no of seconds is:",sec)
sec = sec % (24 * 3600)
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print("seconds value in hours:",hour)
print("seconds value in minutes:",min)
print("second value inseconds is:",sec)
print("The final value of the malformed Timestring is:","%02d:%02d:%02d"%(hour, min, sec))

