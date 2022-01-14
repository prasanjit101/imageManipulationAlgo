'''
ColorShading = colorValue*correspondingShadingFactor
'''

def ColourShading(i,j):
     blueShade =  float(input("Enter the shading factor for blue( range:0 to 1)"))
     redShade =  float(input("Enter the shading factor for red (range:0 to 1)"))
     greenShade =  float(input("Enter the shading factor for green ( range:0 to 1)"))
     pixels = i.load()
     width, height = i.size
     for x in range(width):
          for y in range(height):
               cpixel = pixels[x, y]
               #cpixel[0] contains red value   cpixel[1] contains green value
               #cpixel[2] contains blue value  cpixel[3] contains alpha value
               blue = int(cpixel[2] * blueShade) 
               green = int(cpixel[1] * greenShade) 
               red = int(cpixel[0] * redShade)
               if(blue < 0): 
                    blue = 0  
               if(green < 0): 
                    green = 0  
               if(red < 0): 
                    red = 0
               j.putpixel((x,y),(red,green,blue))
     return j
