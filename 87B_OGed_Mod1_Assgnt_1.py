
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:18:42 2022 (in a flight to Espana)
Rev 3/12/2022
we promt the user about the size of the petals and their quantity.
Turtle then draw a flower.
@author: oged
"""
import turtle
       
       
def drawFlower (t, sideLength, numOfSquares):
    
     arcLength = 2 * 3.1415 * sideLength / 360 # Getting the size of the arc, for 1 degree
     arcSize   = int(360/numOfSquares) # getting the angle for the arc, need to convert to int to loop it: 1 deg = 1 loop
     
     for i in range (numOfSquares): #this loop for each "petal" square and a rotation
         t.begin_fill()
         for i in range(4): 
             t.forward(sideLength)
             t.right(90)
             
         for i in range (arcSize): #drawing the arc between each square...it feelsthat there is a better way to do that, but I can't figure it out.
             t.forward(arcLength)
             t.right(1)     
         t.end_fill()                  
    
        
def main():
    
   sqSize = int(input("How big would you like the petals to be? "))
   numOfPetals = int(input("How many petals should the flower has? "))
   
   
   t = turtle.Turtle()
   drawFlower (t,sqSize, numOfPetals)
main()