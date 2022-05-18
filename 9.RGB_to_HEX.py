#RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF
#A 256 color code is not possible as only the 0-255 range is available for a color.
#Given three colors, such as R, G, and B, convert these RGB color to a hex color code.
# If the conversion is not possible, print -1.(255,0,255) into 0xFF00FF

r=int(input("enter the Red code:"))
g=int(input("enter the green code:"))
b=int(input("enter the blue code:"))
if r>255 or g>255 or b>255:
    print("cant solve")
else:
    rgb = r, g, b
    print("%02x%02x%02x" % (rgb))