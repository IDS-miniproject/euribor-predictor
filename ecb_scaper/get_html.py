from selenium import webdriver
import time

URLS = ["https://www.ecb.europa.eu/press/pressconf/html/index.en.html",
                "https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html"]
OUTPUT_FILES = ["conf.html", "mopo.html"]

# Initiate a web driver
driver = webdriver.Chrome()

for (url, file_name) in dict(zip(URLS, OUTPUT_FILES)).items():
  driver.get(url)

  # Wait for the initial page load
  time.sleep(3)

  page_height = driver.execute_script("return document.documentElement.scrollHeight")
  scroll_amount = driver.get_window_size()['height']
  scroll_position = scroll_amount

  # Scroll down the page to load all the lazy loading content
  while scroll_position <= page_height:
      scroll_options = f"window.scrollTo({{top: {scroll_position}, behavior: 'smooth'}})"

      driver.execute_script(scroll_options)
      time.sleep(1)

      # Update the height accordingly as the page height increases as new content is loaded 
      page_height = driver.execute_script("return document.documentElement.scrollHeight")
      scroll_position += scroll_amount

  # Output the html to a file
  html = driver.page_source
  with open('outputs/' + file_name, 'w') as f:
      f.write(str(html))


