# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:54:39 2020

@author: saiteja
"""

######################## RECOMMENDATION SYSTEM #############################


# import pandas library 
import pandas as pd 
#pandas is used for data cleansing,analysis and manipulation
  
# Get the data 
movies=pd.read_csv("D://360digiTMG/unsupervised/mod16 recommendation/aispry/Archive (2)/Movie.csv",encoding='latin-1') 
  
# Check the head of the data 
movies.head() 

movie_titles = movies.movie
movie_titles.head() 

data = pd.merge(movies, movie_titles) 
data.head() 

data.groupby('movie')['rating'].mean().sort_values(ascending=False).head() 

data.groupby('movie')['rating'].count().sort_values(ascending=False).head() 

ratings = pd.DataFrame(data.groupby('movie')['rating'].mean())  
  
ratings['num of ratings'] = pd.DataFrame(data.groupby('movie')['rating'].count()) 
  
ratings.head() 

import matplotlib.pyplot as plt 
import seaborn as sns 
#used for data visualization  
sns.set_style('white') 
%matplotlib inline #used to plot under the code in the frontend 

# plot graph of 'num of ratings column' 
plt.figure(figsize =(10, 4)) 
  
ratings['num of ratings'].hist(bins = 70) 

# plot graph of 'ratings' column 
plt.figure(figsize =(10, 4)) 
  
ratings['rating'].hist(bins = 70) 

# Sorting values according to  
# the 'num of rating column' 
moviemat = data.pivot_table(index ='userId',columns ='movie', values ='rating') 
  
moviemat.head() 
print(moviemat)
remove_nan=moviemat.dropna()
print(remove_nan)

ratings.sort_values('num of ratings', ascending = False).head(10) 

# analysing correlation with similar movies 
GoldenEye_user_ratings = moviemat['GoldenEye (1995)'] 
Jumanji_user_ratings = moviemat['Jumanji (1995)'] 
  
GoldenEye_user_ratings.head()
Jumanji_user_ratings.head()

# analysing correlation with similar movies 
similar_to_GoldenEye = moviemat.corrwith(GoldenEye_user_ratings) 
similar_to_Jumanji = moviemat.corrwith(Jumanji_user_ratings) 
  
corr_GoldenEye= pd.DataFrame(similar_to_GoldenEye, columns =['Correlation']) 
corr_GoldenEye.dropna(inplace = True) 
  
corr_GoldenEye.head() 

corr_GoldenEye.sort_values('Correlation', ascending = False).head(10) 
corr_GoldenEye = corr_GoldenEye.join(ratings['num of ratings']) 
  
corr_GoldenEye.head() 
  
corr_GoldenEye[corr_GoldenEye['num of ratings']>100].sort_values('Correlation', ascending = False).head() 

# Similar movies as of Jumanji 
corr_Jumanji = pd.DataFrame(similar_to_Jumanji, columns =['Correlation']) 
corr_Jumanji.dropna(inplace = True) 
  
corr_Jumanji = corr_Jumanji.join(ratings['num of ratings']) 
corr_Jumanji[corr_Jumanji['num of ratings']>100].sort_values('Correlation', ascending = False).head() 
