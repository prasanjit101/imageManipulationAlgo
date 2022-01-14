'''
gray = min(red,green,blue)
'''

def Decomposition_MIN_BW(i,j):
    pixels = i.load() 
    width, height = i.size
    #cpixel[0] contains red value   cpixel[1] contains green value
    #cpixel[2] contains blue value  cpixel[3] contains alpha value
    for w in range(width):
        for h in range(height):
            cpixel = pixels[w, h]
            gray = int(min(cpixel))
            j.putpixel((w,h),(gray,gray,gray))
    return j


