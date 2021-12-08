from bs4 import BeautifulSoup
from selenium import webdriver

####################################
#  100 Movies that you must watch! #
####################################

url = "https://www.empireonline.com/movies/features/best-movies-2/"
driver = webdriver.Firefox()
driver.get(url)
response = driver.page_source
#
soup = BeautifulSoup(response, 'html.parser')
movies = soup.find_all(name="h3")
movie_list = []
for movie in movies:
    movie_list.append(movie.text)

movie_list = movie_list[::-1]
# Other option to sort the list 
# total_movies = len(movie_list)
# for i in range(total_movies):
#     i += 1
#     print(movie_list[total_movies - i])

with open("top100-movies.txt","w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
