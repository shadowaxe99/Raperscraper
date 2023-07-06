import requests
from scraper import QuizletScraper, scrape_quizlet
import utils

Quizlet_URL = "https://quizlet.com"

def main():
    scraper = QuizletScraper(requests)
    print("Scraping started")
    try:
        scrape_quizlet(scraper, Quizlet_URL)
        print("Scraping completed")
    except Exception as e:
        print("Error occurred: ", e)
        utils.log_error(e)

if __name__ == "__main__":
    main()