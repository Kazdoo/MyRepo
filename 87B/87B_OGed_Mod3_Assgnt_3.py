# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:36:10 2022

@author: oged
"""
from image import *


def negativePixel (oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    newPixel = Pixel (newRed,newGreen,newBlue)
    return newPixel

def makeNegative(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myImageWindow = ImageWin(width*2, height, "negative")
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)
    
    for row in range (height):
        for col in range (width):
            oldPixel = oldImage.getPixel (col,row)
            newPixel = negativePixel(oldPixel)
            newIm.setPixel (col,row, newPixel)
            
    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()
    
def grayPixel (oldPixel):
    intensitySum = oldPixel.getRed()+oldPixel.getGreen()+oldPixel.getBlue()
    aveRGB = intensitySum // 3
    newPixel = Pixel(aveRGB,aveRGB,aveRGB)
    return newPixel

def makeGrayScale(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myImageWindow = ImageWin(width*2, height, "grayscale")
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)
    
    for row in range (height):
        for col in range (width):
            oldPixel = oldImage.getPixel (col,row)
            newPixel = grayPixel(oldPixel)
            newIm.setPixel (col,row, newPixel)
            
    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()
    
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

def generalTransform (imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myImageWindow = ImageWin(width*2, height, "grayscale")
    oldImage.draw(myImageWindow)

    newImage = pixelMapper(oldImage, negativePixel)
    
    newImage.setPosition(oldImage.getWidth() + 1 ,0)
    newImage.draw(myImageWindow)
    myImageWindow.exitOnClick()
   


def doubleImage (oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()
    
    newIm = EmptyImage(oldW*2, oldH *2)
    
    for row in range(oldH):
        for col in range (oldW):
            oldPixel = oldImage.getPixel (col,row)
            
            newIm.setPixel (2*col, 2*row,oldPixel)
            newIm.setPixel (2*col+1, 2*row,oldPixel)
            newIm.setPixel (2*col, 2*row+1,oldPixel)
            newIm.setPixel (2*col+1, 2*row+1,oldPixel)

    return newIm

def makeDoubleImage(imageFile):
    
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myImageWindow = ImageWin(width*2, height*3, "double")
    oldImage.draw(myImageWindow)
    
    newImage = doubleImage(oldImage)
    newImage.setPosition (0, oldImage.getHeight() +1)
    newImage.draw(myImageWindow)
    
    myImageWindow.exitOnClick()



def doubleImage2 (oldImage):
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



def main():

    #bfly = FileImage("butterfly.png")
    
    makeDoubleImage("butterfly.png")


if __name__ == "__main__":
    main()