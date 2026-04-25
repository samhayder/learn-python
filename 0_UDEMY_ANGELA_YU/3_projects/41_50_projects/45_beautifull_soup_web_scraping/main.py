import requests
from bs4 import BeautifulSoup

web_scraping_link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(web_scraping_link)
movie_lists_html = response.text

soup = BeautifulSoup(movie_lists_html, "html.parser")

# movie_names = [title.getText() for title in soup.select(".article-title-description__text .title")]

movie_lists = [movie.getText() for movie in soup.select(selector=".article-title-description__text .title")]

movies = movie_lists[::-1]
list_path = r"0_UDEMY_ANGELA_YU/3_projects/41_50_projects/45_beautifull_soup_web_scraping/movie_lists.txt"
with open(list_path, mode='w', encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")

