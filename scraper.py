from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import utils

class QuizletScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def scrape_quizlet(self):
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return self.parse_quizlet(soup)

    def parse_quizlet(self, soup):
        quizlet_data = {}
        cards = soup.find_all(class_='quizlet-card')
        for card in cards:
            question = card.find(class_='quizlet-question').text
            answer = card.find(class_='quizlet-answer').text
            quizlet_data[question] = answer
        return quizlet_data

    def close(self):
        self.driver.quit()

def scrape_quizlet(url):
    scraper = QuizletScraper(url)
    try:
        quizlet_data = scraper.scrape_quizlet()
        utils.save_data(quizlet_data)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        scraper.close()