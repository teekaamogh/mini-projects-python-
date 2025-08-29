# News app

import requests

query=input("What topic do you want to read:")
total_articles=int(input("How many articles do you want to read:"))

api="a6b490d453a247d893e82ede9190db59"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-07-29&sortBy=publishedAt&apiKey={api}"
#print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]

if total_articles>len(articles):
  print(f"Only {len(articles)} articles are available, showing those instead.\n")
  total_articles = len(articles)  

for index, article in enumerate(articles[:total_articles]):
  print("\n",index+1,article["title"],article["url"])
  print("\n\------------------------/\n")
  


  