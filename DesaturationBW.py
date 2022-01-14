'''
Desaturation Algorithm
Gray = ( Max(Red, Green, Blue) + Min(Red, Green, Blue) ) / 2
'''

def Desaturation_BW(i,j):
  pixels = i.load() 
  width, height = i.size
  for x in range(width):
      for y in range(height):
        cpixel = pixels[x, y]
        #cpixel[0] contains red value   cpixel[1] contains green value
        #cpixel[2] contains blue value  cpixel[3] contains alpha value
        Gray = int( max(cpixel[0],cpixel[1],cpixel[2]) +min(cpixel[0],cpixel[1],cpixel[2]) ) / 2
        j.putpixel((x,y),(Gray,Gray,Gray))
  return j
