# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:29:41 2020

@author: Dell
"""


# Python program to generate WordCloud 

# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import os

sourcepath = os.path.dirname(__file__)
relativepath=sourcepath+"\Youtube\Youtube04-Eminem.csv"

# Reads 'Youtube04-Eminem.csv' file 
df = pd.read_csv(relativepath, encoding ="latin-1") 

comment_words = '' 
stopwords = set(STOPWORDS) 

# iterate through the csv file 
for val in df.CONTENT: 
	
	# typecaste each val to string 
	val = str(val) 

	# split the value 
	tokens = val.split() 
	
	# Converts each token into lowercase 
	for i in range(len(tokens)): 
		tokens[i] = tokens[i].lower() 
	
	comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800, 
				background_color ='white', 
				stopwords = stopwords, 
				min_font_size = 10).generate(comment_words) 

# plot the WordCloud image					 
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 
