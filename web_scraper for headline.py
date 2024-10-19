import requests
from bs4 import BeautifulSoup

def headline(url):
    try:
        response = requests.get(url) 
        response.raise_for_status()  # Check for a successful request

       
        soup = BeautifulSoup(response.content, 'html.parser')

      
        headlines = soup.find_all('h1') 

        for headline in headlines:
            print(headline.get_text(strip=True))  # Clean up the text

    except requests.exceptions.RequestException as e: 
        print(f"Error: {e}")


if __name__ == "__main__":
    url = "https://www.icc-cricket.com/news/australia-make-it-14-in-a-row-with-thumping-win-in-leeds"  
    headline(url)
