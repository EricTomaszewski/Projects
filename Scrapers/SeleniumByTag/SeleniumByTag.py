# https://youtu.be/2kEg4I6pmrE?si=FgqfbR3cRxQY7fFY&t=212

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://platform.openai.com/docs/assistants/overview")

# Wait for the page to load
time.sleep(2)

# Find the elements you want to scrape
# Here, we'll pretend we want to scrape all paragraphs
elements = driver.find_elements(By.TAG_NAME, 'p')

# Open a text file to save the data
with open("scraped_content.txt", 'w') as file:
    for element in elements:
        file.write(element.text + "\n")

# Close the WebDriver
driver.quit()

print("Scraping complete. Content saved to scraped_content.txt")