import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url="https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")



def scrape_books(soup):
    books=[]
    for book in soup.find_all("li",class_="col-xs-6"):
        title=book.h3.a.attrs["title"]
        price = book.find("p",class_="price_color").text[2:]
        rating = book.find("p",class_="star-rating")["class"][1]
        books.append({
            "Title":title,
            "Price": float(price),
            "Rating":rating
            })
    return books

book_data = scrape_books(soup)
df = pd.DataFrame(book_data)
print(df.head())


# Export to CSV
df.to_csv('./data.csv', index=False)

# Export to Excel
df.to_excel('./data.xlsx', index=False)