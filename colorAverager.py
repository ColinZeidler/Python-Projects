import ImageGrab

image = ImageGrab.grab()    #get the image
w, h = image.size
hoffset = h/2 - 450         #set the height offset
woffset = w/2 - 450         #set the width offset

# zero the numbers
red  = 0 
green= 0
blue = 0
total = 0


for ny in range (hoffset, hoffset + 1000, 200):
    for nx in range(woffset, woffset + 1000, 200):  #grabs multiple set with spaces between them

        for y in range(ny, ny+100, 5):
            for x in range(nx, nx+100, 5):
            
                color = image.getpixel((x, y))
                image.putpixel((x, y), (255,0,0))
                redt, greent, bluet = color #get the pixel colors
                #add the value to the averages
                red += redt
                green += greent
                blue += bluet
                total += 1  #number of pixels grabbed, used in averages
#calculate the averages
red = red/total
green = green/total
blue = blue/total
print (red, green, blue)    #print the averages