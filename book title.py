import requests
from bs4 import BeautifulSoup

URL = "https://www.shakespeareandcompany.com/?srsltid=AfmBOoovHFJKWMt2QYHF9PT9NQoCpfQz8BNCFJwBEuAGDPdFPmDZP5ms"

# Send a request
response = requests.get(URL)

# Check the status code
if response.status_code == 200:
    content = response.text
else:
    print("Page not found")
    exit()  # Exit if the page is not found

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')


books = soup.find_all("div", class_="site-wrapper")


for book in books:
    # Use .get_text() only if the element is found to avoid errors
    book_title = book.find('h3').get_text() if book.find('h2') else 'No title found'
    author = book.find('p', class_="author").get_text() if book.find('p', class_="author") else 'No author found'

    # Properly format the print statement
    print(f"Title: {book_title}, Author: {author}")
