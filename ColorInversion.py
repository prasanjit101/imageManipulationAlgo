'''
Inverted color : 255-colorvalue
'''

def ColourInversion(i,j):
  pixels = i.load()
  width, height = i.size
  for x in range(width):
      for y in range(height):
        cpixel = pixels[x,y]
        #cpixel[0] contains red value   cpixel[1] contains green value
        #cpixel[2] contains blue value  cpixel[3] contains alpha value
        invertedRed   = 255 - cpixel[0]
        invertedGreen = 255 - cpixel[1]
        invertedBlue  = 255 - cpixel[2]
        j.putpixel((x, y),(invertedRed, invertedGreen, invertedBlue))
  return j
