#Sepia Algorithm


def Sepia(i,j):
    pixels = i.load() 
    width, height = i.size
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y] 
            outputRed = int((cpixel[0] * 0.393) + (cpixel[1] *0.769) + (cpixel[2] * 0.189))
            outputGreen = int((cpixel[0] * 0.349) + (cpixel[1] *0.686) + (cpixel[2] * 0.168))
            outputBlue = int((cpixel[0] * 0.272) + (cpixel[1] *0.534) + (cpixel[2] * 0.131))
            #cpixel[0] contains red value   cpixel[1] contains green value
            #cpixel[2] contains blue value  cpixel[3] contains alpha value
            if(outputRed>255):
                outputRed=255
            if(outputGreen>255):
                outputGreen=255
            if(outputBlue>255):
                outputBlue=255
            j.putpixel((x,y),(outputRed,outputGreen,outputBlue))
    return j
