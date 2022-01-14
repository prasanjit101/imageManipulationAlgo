# ImageManipulationAlgorithms

A collection of implementation of image manipulation algorithms in python.

List of algos -
1. Color Inversion
2. Color Shading
3. Decomposition MAX BW
4. Decomposition MIN BW
5. Desaturation BW
6. Gamma Correction
7. Luminance 
8. Mean Filter
9. Median Filter
10. Mirror Image
11. Rotation BY 90 Degree
12. Sepia Algo
13. Single Color Inversion
14. Solarisation

## Requirements

Python 3

## Usage
In your file import the required module and implement
```from PIL import Image
from ColorShading import ColourShading

i = Image.open("input.png")
j=Image.new(i.mode,i.size)

ColourShading(i,j).save('output.png')
```