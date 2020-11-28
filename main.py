
from selenium import webdriver
import os
import time
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

videos = ['https://www.youtube.com/watch?v=w-m5neJvbuo','https://www.youtube.com/watch?v=WkxO0q9fErI']

sleep_time = 0

for i in range(1000):
	print("Watching for {} time".format(i))
	random_video = random.randint(0,1)
	driver.get(videos[random_video])
	time.sleep(sleep_time) # Let the user actually see something!
	sleep_time = random.randint(500,600)

	time.sleep(5) # Let the user actually see something!
driver.quit()
