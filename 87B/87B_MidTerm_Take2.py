# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:33:16 2022


Here we go for Take 2.
Thanks again for giving me a second chance.

after working on this problem here are the main areas where I struggled:
Again if you think of any practice I can do I will try to make some time and increase my coding logic and reflexes when it comes to code "on a white board"
HARD    
    1. in Def cleanUp: change 'invalid' to 0 in the dictionary. Eventually found it was enumerate.
    2. In Def fileToDict: appending multiple values to the same key.
    3. Drawing graph in a function and returning the graph to main() is still very annoying. The fact that plt.show() empty the axes took me a while to figure out.

MEDIUM (or: omg! of course this would work moment)
    4. In Def fileToDict: it took me a while to think about the "if >> pass  else >> do something" to change everything which is not a match to the regex


@author: oged
"""

import re
import matplotlib.pyplot as plt


def fileToDict(filename):
    emails = []
    nums   = []
    d      = {}
    
        
    with open (filename, 'r') as f: #no need to close the file after this block, it will automatically do it.
        lines = f.readlines()
        
        #creating 2 lists for emails and values using tab to split.
        for line in lines:
            email, num = line.strip().split("\t")
            emails.append(email) 
            nums.append(num)
        
        
    #replacing invalid emails and invalid values
    for i in range (len(emails)):
        if re.match('\S+@\S+', emails[i]) :#I am aware that this is not full proof and we can get a much more elaborated regex here, but I think this is enough for this context.
             pass
        else:
             emails[i] ='invalid@email.com'
     
    for i in range (len(nums)):
        if re.match('[0-9]', nums[i]):
            pass
        else:
            nums[i] ='invalid'
    
       
    #creating the dictionary, appending multiple values to unique keys
    for i in emails:
        d[i] = []

    for i in range (0,len(emails)):
        d[emails[i]].append(nums[i])

    
    return d
  
      
    
def cleanUp(d1):
    d2    = {}
    dirty = 'invalid'
    
    #copy of the dirty dictionary.
    for i in d1:
        d2[i] = d1[i]
         
    #replacing invalids with string 0 in the clean dictionary.
    for k,v in d2.items():
        for i, s in enumerate(v):
            if dirty in s:
                v[i] = s.replace (dirty, '0')
  
    
    # string to int conversion and sum of values.
    for key, value in d2.items():
        d2[key]= sum([int(item)for item in value])
    
    return d2

    
def myPlot(data):
    
    #creating list for X and Y axis data.
    emails = list(data.keys())
    nums = list(data.values())
    
    #object to pass back to main.
    fig = plt.gcf()
    
    #the graph itself with some labels and some light formating.
    plt.bar(emails, nums)
    plt.title("sum of value(s) per email address")
    plt.xlabel("emails")
    plt.ylabel("value")
    plt.xticks(rotation = 90) #vertical label for readibility
    plt.tight_layout()   # with vertical label, this is necessary to not crop them.
    
    plt.show() #display the plot to the user, but clear the graph.
               #I have search a long time for a better solution...but for now I am redrawing the graph a second time (below)
               #Another solution I have consider is not drawing twice but recalling the function after the plt.show() in  main() after the user Y/N choice.
    
    plt.bar(emails, nums)
    plt.title("sum of value(s) per email address")
    plt.xlabel("emails")
    plt.ylabel("value")
    plt.xticks(rotation = 90)
    plt.tight_layout()
    
    
    return (fig)




def main():

    #gathering the filename from the user.
    file = input("what is your file name, including the extension?: \n")
    
    #passing the file to the dictionary factory function
    filetoclean = fileToDict(file)
    
    #passing the dirty dictionary to the cleaning station
    filetograph = cleanUp(filetoclean)
    
    #passing the clean data to the plotter
    myPlot(filetograph)
    
            
    #final offer to save the graph and quit or just quit the program
    choice= input("do you want to save that graph? (Y/N)\n")
    
    if choice.lower() == "y": #accepting both Y and y for better user's experience.
        savename = input("what would you like to name the saved graph file?\n")
        plt.savefig(savename +'.png')
    
     
    
    
main()