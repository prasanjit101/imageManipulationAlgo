'''
Luminance algorithm
luma = (red*0.3+green*0.59+blue*0.11)
'''

def Decomposition_MAX_BW(i,j):
    pixels = i.load() 
    width, height = i.size
    #cpixel[0] contains red value   cpixel[1] contains green value
    #cpixel[2] contains blue value  cpixel[3] contains alpha value
    for image_width_iterator in range(width):
        for image_height_iterator in range(height):
            cpixel = pixels[image_width_iterator, image_height_iterator]
            luma = int((cpixel[0]*0.3)+(cpixel[1]*0.59)+(cpixel[2]*0.11))
            j.putpixel((image_width_iterator,image_height_iterator),(luma,luma,luma))
    return j