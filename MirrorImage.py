# Mirroring Image


def MirrorImage(i,j):
    #pixel data is stored in pixels in form of two dimensional array
    pixels = i.load()
    width, height = i.size
    print("1 Mirror along X and Y axis, 2 Mirror along Y axis, 3 Mirror along X axis")
    option=input('Enter your choice: ')
    if option == 1:
        widthmodifier=width-1
        heightmodifier=height-1
    elif option == 2:
        widthmodifier=0
        heightmodifier=height-1
    else:
        widthmodifier=width-1
        heightmodifier=0

    for image_width_iterator in range(width):
        for image_height_iterator in range(height):
            cpixel = pixels[image_width_iterator,image_height_iterator]
            j.putpixel((abs(widthmodifier-image_width_iterator),abs(heightmodifier-image_height_iterator)),(cpixel))
    return j
