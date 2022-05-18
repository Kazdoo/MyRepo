# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:00:29 2022

@author: oged

We are making any image more Red and doubling its size.


"""

from image import *


#this increase every red value by 50 in every pixel to a 255 maximum
def redPixel (oldPixel):
    newRed = oldPixel.getRed() + 50
    if newRed > 255:
        newRed = 255
    else:
        newRed = newRed
        
    newPixel = Pixel(newRed,oldPixel.getGreen(),oldPixel.getBlue())
    return newPixel


#function from Module 3 that allow any pixel modification.
def pixelMapper (fileImage, rgbFunction):
    width = fileImage.getWidth()
    height = fileImage.getHeight()
    newIm = EmptyImage(width, height)
    
    for row in range(height):
        for col in range (width):
            oldPixel = fileImage.getPixel(col, row)
            newPixel = rgbFunction(oldPixel)
            newIm.setPixel(col, row, newPixel)
    
    return newIm


# using the double the size function from module 3
def double(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()
    
    newIm = EmptyImage(oldW*2, oldH*2)

    for row in range (newIm.getHeight()):
        for col in range(newIm.getWidth()):
            
            originalCol = col // 2
            originalRow = row // 2
            oldPixel = oldImage.getPixel(originalCol, originalRow)
            
            newIm.setPixel(col, row, oldPixel)
    return newIm


#another function from module 3 to create a window, draw and save the different transformations
def generalTransform (oldImage):
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    #creating the Window and drawing the original image
    myImageWindow = ImageWin(width*4, height*2, "result")
    oldImage.draw(myImageWindow)

    newImage = pixelMapper(oldImage, redPixel)
    newImage2 = double(newImage)
    
    #Drawing the 1st transformation
    newImage.setPosition(oldImage.getWidth() + 1 ,0)
    newImage.draw(myImageWindow)
    
    #Drawing the 2nd transformation
    newImage2.setPosition(0, oldImage.getHeight()+1)
    newImage2.draw(myImageWindow)
    
    #saving these transformations
    newImage.save('redresult.png')
    newImage2.save('bigredresult.png')
    
    
    myImageWindow.exitOnClick()


    
def main():
    
    oldImage = FileImage("Katie.png")     
    generalTransform(oldImage)
    
   
if __name__ == "__main__":
    main()