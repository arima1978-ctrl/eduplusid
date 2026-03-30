
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
d = webdriver.Chrome(options=options)
d.get("https://www.google.com")
print("Selenium OK: " + d.title)
d.quit()
