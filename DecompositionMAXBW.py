''' 
gray = max(red,green,blue)
'''
#cpixel[0] contains red value   cpixel[1] contains green value
#cpixel[2] contains blue value  cpixel[3] contains alpha value
def Decomposition_MAX_BW(i,j):
    pixels = i.load() 
    width, height = i.size
    for w in range(width):
        for h in range(height):
            cpixel = pixels[w, h]
            gray = int(max(cpixel))
            j.putpixel((w,h),(gray,gray,gray))
    return j