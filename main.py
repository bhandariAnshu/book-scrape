import requests
from bs4 import BeautifulSoup
from functions import create_search_url
from bookstore import book_entry
search_term = input("What book do you want to search\n").lower()
search_in_url = create_search_url(search_term)
url = f"https://bookslandnepal.com/?s={search_term}&post_type=product"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
# print(response.content)

soup = BeautifulSoup(response.text, 'html.parser')
# print(response.content)
book_listings = soup.find_all('div', class_="product-wrapper")


if len(book_listings) < 1:
    print(f"Sorry, there is no book with keyword {search_term}")
else:
    print(f"I found the following books under the keyword {search_term}")
fetched_books = []

for book in book_listings:
    title_elem = book.find('h3', class_='wd-entities-title')
    title = title_elem.get_text(strip=True) if title_elem else "Default Title"
    print(title)
    price_elem = book.find('span', class_='woocommerce-Price-amount')
    price = price_elem.get_text(strip=True) if price_elem else "Default price"
    print(price)
    
    # add_to_cart_url = soup.find_all('a', class_='wd-entities-title',href=True)
    
    # print(f"{add_to_cart_url}")
    book_entry(title, price)

 
