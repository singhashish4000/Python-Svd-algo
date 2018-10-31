import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns  
sns.set_style('dark')  


''' list of movies ratings'''
ratings_data = pd.read_csv("ratings.csv")  
'''print (ratings_data.head())  '''


''' list  of movies '''
movie_names = pd.read_csv("movies.csv")  
movie_names.head()  
'''print (movie_names.head())'''

'''  merge above two '''
movie_data = pd.merge(ratings_data, movie_names, on='movieId')  
'''print (movie_data.head());'''


''' Sort Assending '''
m = movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head()  
'''print(m)'''

'''total number of ratings for a movie:'''
t = movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()  
'''print(t)'''


'''Execute the following script to create ratings_mean_count dataframe and first add the average rating of each movie to this dataframe:'''

ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())  
'''print(ratings_mean_count);'''

'''number of ratings for a movie to the ratings_mean_count dataframe. '''
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
'''print(ratings_mean_count)'''

# plt.figure(figsize=(8,6))  
# plt.rcParams['patch.force_edgecolor'] = True  
# n = ratings_mean_count['rating_counts'].hist(bins=50)  
# print(n)

user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating') 
u = user_movie_rating.head()  

a = forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']  

movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])  
corr_forrest_gump.dropna(inplace=True)  
corr_forrest_gump.sort_values('Correlation', ascending=False).head(10) 



corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])  
corr_forrest_gump.head()  

c = corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head()  
print(c)