# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:29:53 2022

Assignement:
Create a plot to show a comparison between the two sets.
Create a plot that shows each set separately (two plots) and highlight the max and min data items.
What other data visualization can we do on such data? (you will need to implement this).

How did I do it:
1. using Pandas manipulate the data to create a unique data set. I did that by adding a field: time.
2. using the Seaborn module creating a few graphs.

Problems:
In the FacetGrid, my x labels are slightly miss aligned toward the origin.

Note to pr. Darwiche:
I am not 100% confident about my management of the main() function.
I'll keep working on this topic in the coming weeks.


@author: oged
"""

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

#this function will be used to draw a horizontal line & annotate at max value of a set of data
def add_max_line(data, var=None, **kws):

    #Calculate max
    m = max(data[var])
    
    #Get current axis
    ax = plt.gca()
    
    #add line at max
    ax.axhline(m, color='maroon', lw=2, ls='--')
    
    #annotate group max
    x_pos=0.65
    ax.text(x_pos, 0.7, f'max={m:.0f}', 
            transform=ax.transAxes,   #transforms positions to range from (0,0) to (1,1)
            color='maroon', fontsize=12)
    
#this function will be used to draw a horizontal line & annotate at min value of a set of data
def add_min_line(data, var=None, **kws):

    #Calculate min
    m = min(data[var])
    
    #Get current axis
    ax = plt.gca()
    
    #add line at group min
    ax.axhline(m, color='blue', lw=2, ls='--')
    
    #annotate group min
    x_pos=0.65
    ax.text(x_pos, 0.5, f'min={m:.0f}', 
            transform=ax.transAxes,   #transforms positions to range from (0,0) to (1,1)
            color='blue', fontsize=12)


def main():

    df1 = pd.read_csv('rainfallISet1.txt',sep=' ',header=None, names=["city","rain_mm"])
    df2 = pd.read_csv('rainfallSet2.txt',sep=' ',header=None, names=["city","rain_mm"])
 
    #adding a new column with the folloing info to each data frame.
    df1['time']='old'
    df2['time']='recent'
    
    #merging the 2 dataframes
    df= df1.append(df2, ignore_index = True)

    #Scatter with all the data
    plt.subplot(1,2,1)
    sns.scatterplot(x="city", y="rain_mm", hue=('time'),data = df)
    plt.xticks(rotation = 90)
    plt.tight_layout()#so X axis labels are not "cut"


    #this vizualization shows the agregation of rain for both time period. 
    #it shows that a lot more rain was pouring in the old days.
    plt.subplot(1,2,2)
    sns.histplot(data=df,y='rain_mm', hue='time')
    plt.tight_layout()#so X axis labels are not "cut"
    
    plt.savefig('all_rain_data.png')
    

    #1 plot "time" or set of data, using the same Y axis for comparison.
    g = sns.FacetGrid(df, col='time',ylim=(0, 100))
    g.map_dataframe(add_max_line, var='rain_mm')
    g.map_dataframe(add_min_line, var='rain_mm')
    g.map_dataframe(sns.scatterplot, x='city',y='rain_mm');
    
    #change the direction of ALL X-axis label to vertical
    for axes in g.axes.flat:
        axes.set_xticklabels(axes.get_xticklabels(), rotation=90, horizontalalignment='right')
    plt.tight_layout() #so X axis labels are not "cut"
    plt.savefig('split_scatter.png')
    
   
main()

