import requests
from bs4 import BeautifulSoup
import json

def scrapeui(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    elements = {
        "buttons": [btn.text.strip() for btn in soup.find_all('button')],
        "links": [{"text": a.text.strip(), "href": a.get('href')} for a in soup.find_all('a', href=True)],
        "input_fields": [
            {"type": inp.get('type', 'text'), "name": inp.get('name', '')} for inp in soup.find_all('input')
        ],
        "forms": [
            {"action": form.get('action', ''), "method": form.get('method', 'GET')} for form in soup.find_all('form')
        ]
    }
    
    with open("WEB SCRAPPING TASK\elements.json", "w", encoding="utf-8") as f:
        json.dump(elements, f, indent=4)

    print("UI elements extracted and saved to elements.json")

if __name__ == "__main__":
    url = "https://demoblaze.com/"
    scrapeui(url)