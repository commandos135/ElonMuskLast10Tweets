from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()

options.add_argument("profile-directory=Default")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    link = 'https://twitter.com/elonmusk'
    driver.get(link)

    tweet_text_elements = []


    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2) 

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        
        tweet_text_elements.extend(soup.find_all('div', {'data-testid': 'tweetText'}))


    for i, tweet_text_element in enumerate(tweet_text_elements[:10]):
        tweet_text = tweet_text_element.text.strip().replace("\n", "")
        print(f"This is the Tweet number {i+1}: {tweet_text}")

finally:
    driver.quit()
