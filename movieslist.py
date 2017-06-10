import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://www.imdb.com/search/title?at=0&start=1&title_type=feature&year=1950%2C2012&sort=num_votes%2Cdesc")

soup = BeautifulSoup(page.content,'lxml')

movie_list = soup.find(class_="lister-list")

title = movie_list.select('h3 a')



titles =[t.text for t in title]
print(titles)

runtime = movie_list.select(" .text-muted  .runtime")

runtimes = [r.text for r in runtime]
print(runtimes)

genre = movie_list.select(" .text-muted  .genre")
genres = [g.get_text() for g in genre]
print(genres)



metascore  = movie_list.find_all(True,{'class':["metascore favorable","metascore mixed"]})
metascores = [m.get_text() for m in metascore]
print(metascores)



top_movies = pd.DataFrame({
      "title" : titles,
      "time_duration" : runtimes,
      "genre" : genres,
      "metascore" : metascores


}

)
print(top_movies)
top_movies.to_csv('top_movies.csv', encoding='utf-8')
top_movies