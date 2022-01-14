'''
Gamma correction Algorithm
gammaCorrection = 1 / gamma
colour = GetPixelColour(x, y)
newRed   = 255 * (Red(colour)   / 255) ^ gammaCorrection
newGreen = 255 * (Green(colour) / 255) ^ gammaCorrection
newBlue  = 255 * (Blue(colour)  / 255) ^ gammaCorrection
PutPixelColour(x, y) = RGB(newRed, newGreen, newBlue)
'''

def GammaCorrection(i,j):
  pixels = i.load() 
  width, height = i.size
  gamma=input("Enter the value of gamma range:0.25 to 2.0: ")
  for x in range(width):
      for y in range(height):
        cpixel = pixels[x, y]
        gammaCorrection = 1 / gamma
        #cpixel[0] contains red value   cpixel[1] contains green value
        #cpixel[2] contains blue value  cpixel[3] contains alpha value
        newRed   = int(255 * ((cpixel[0]/ 255.0)**gammaCorrection))
        newGreen = int(255 * ((cpixel[1]/ 255.0)**gammaCorrection))
        newBlue  = int(255 * ((cpixel[2]/ 255.0)**gammaCorrection))
        j.putpixel((x,y),(newRed, newGreen, newBlue))
  return j
