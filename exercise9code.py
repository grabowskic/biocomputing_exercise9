# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:01:52 2018

@author: Cole
"""

# this code corresponds to exercise 9 for biocomputing on analysis and plotting

# 1) find some data on two variables you would expect to be related to one another
# picked ping pong ball mass vs number of ping pong balls from measurements lab
# entered them into a .txt file call pingpong.txt
# write a script to load the text file
# produce a scatter of the two variables that includes a trend line

import pandas
import numpy
from plotnine import *

pong=pandas.read_csv("pingpong.txt", sep=",", header=0)


# plot the data
a=ggplot(pong,aes(x="ball_count",y="mass_g"))+theme_classic()
a+geom_point(color='blue',size=3)+xlab("Number of Ping Pong Balls")+ylab("Mass (g)")+stat_smooth(method="lm")


## 2)
# given the data in "data.txt", write a script that generate two figures that summarize the data
# a) show a barplot of the means of the four populations
# b) show a scatter plot of all of the observations
# you may want to "jitter" the points (geom_jitter()) to make it easier to see
#  all of the observations within a population in your scatter plot
# alternatively, you could also try setting the alpha argument in geom_scatterplot() to 0.1

# do the bar and scatter plots tell different stories? Why?

data=pandas.read_csv("data.txt", sep=",", header=0)

# a) show a barplot of the means of the four populations
b=ggplot(data, aes(x="region",y="observations"))+theme_classic()+ylab("Mean Observations")+xlab("Region")
b+geom_bar(stat="summary",fun_y=numpy.mean)

# b) show a scatter plot of all of the observations
c=ggplot(data, aes(x="region",y="observations"))+theme_classic()+ylab("Observations")+xlab("Region")
c+geom_point()+geom_jitter()

# conclusions
# the barplot shows that there are about the same number of average observations for each of the populations, which may
# lead one to believe that the distributions for each of the regions is the same. 

# on the other hand, the jittered scatterplot shows that while the average number of observations is around the same,
# the distributions between the population regions vary widely.
# East is fairly bell curve shaped spanning a range from about 0-40 observations
# North is much more concentrated with most of its observations right around the mean
# south is bimodal with high concentrations both about 10 observations above and below the mean
# west is fairly evenly distributed through the full range from 0-30 observations

# essentially, this goes to show that visualizing data in different forms can lead to very different conclusions



