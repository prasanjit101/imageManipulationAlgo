# Rotate image by 90 degrees


def RotateBy90(i,j):
    pixels = i.load()
    width, height = i.size
    #cpixel[0] contains red value   cpixel[1] contains green value
    #cpixel[2] contains blue value  cpixel[3] contains alpha value
    for w in range(width):
        for h in range(height):
            cpixel = pixels[w,h]
            j.putpixel((abs(height-1-h),abs(w)),(cpixel))
    return j