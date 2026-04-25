import requests
from bs4 import BeautifulSoup

website_link = "https://news.ycombinator.com/news"

response = requests.get(url=website_link)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.prettify())
# title = soup.select(selector=".titleline a")
# print(title[0].getText())
# title_text = title.getText()
# title_link = title.get("href")
# title_upvote = soup.select("#up_47890799")

# crate list title_texts, title_links and title_upvotes to print max score number index with text
title_texts = [text.getText() for text in soup.select(selector=".titleline a")]
title_links = [link.get("href") for link in soup.select(selector=".titleline a")]
title_upvotes = [int(score.getText().split()[0]) for score in soup.select(selector=".score")]

large_score = max(title_upvotes)
large_score_index = title_upvotes.index(large_score)

print(title_texts[large_score_index])
print(title_links[large_score_index])
    