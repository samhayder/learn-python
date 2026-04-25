# Parse HTML Code in String by beautiful soup
from bs4 import BeautifulSoup

file_path = r"0_UDEMY_ANGELA_YU/1_lessions/day45_beautiful_soup/website.html"

with open(file_path, 'r') as file:
    html_docs = file.read()
    
soup = BeautifulSoup(html_docs, "html.parser")
# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# #Finding & Selecting particular element
find_all_tags = soup.find_all(name="a")
# print(find_all_tags)
for tag in find_all_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

# Select
name = soup.select("#name")
heading = soup.select_one(".heading")
print(name,"\n",heading)