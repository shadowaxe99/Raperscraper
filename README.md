# Quizlet Scraper

This repository contains a Python program that scrapes data from Quizlet, despite normal scrapers not working. 

## Installation

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Import the `QuizletScraper` class from `scraper.py` and the `utils` module from `utils.py` in your `main.py` file.
2. Define the Quizlet URL you want to scrape as `Quizlet_URL`.
3. Create an instance of `QuizletScraper` and call the `scrape_quizlet` function with `Quizlet_URL` as the argument.

Here is a sample usage:

```python
from scraper import QuizletScraper
import utils

Quizlet_URL = "https://quizlet.com/subject/sample-quiz/"

scraper = QuizletScraper()
scraper.scrape_quizlet(Quizlet_URL)
```

## Dependencies

This program uses the following Python libraries:

- requests
- BeautifulSoup
- selenium
- webdriver_manager

These dependencies are listed in the `requirements.txt` file.

## Contributing

Please read through our contributing guidelines. Included are directions for opening issues, coding standards, and notes on development.

## License

This project is licensed under the MIT License.