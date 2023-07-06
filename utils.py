from bs4 import BeautifulSoup

def parse_html(content):
    """
    Function to parse HTML content using BeautifulSoup
    """
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def extract_data(soup, element_id):
    """
    Function to extract data from a specific HTML element using its ID
    """
    element = soup.find(id=element_id)
    if element:
        return element.text.strip()
    return None

def log_message(message):
    """
    Function to log messages
    """
    print(message)
```
