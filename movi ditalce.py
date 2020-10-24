import imdb
hr = imdb.Imdb()
movie_name = input("enter the movie name : ")
movie = hr.search_movie(str(movie_name))
index = movie[0].getID()
movies = hr.get_movie(index)
title = movies["title"]
year = movies["year"]
cast = movies["cast"]
list_of_cast=",".join(map(str,cast))
print("title",title)
print("year of release :",year)
print("full cast :",list_of_cast)
