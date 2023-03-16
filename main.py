from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

LINKEDIN_JOBS_SEARCH_URL = "https://www.linkedin.com/jobs/"

chrome_driver_path = r"C:\Users\Utilisateur1\Development\chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get(LINKEDIN_JOBS_SEARCH_URL)

# accept cookies
buttons_cookies = driver.find_elements(By.CSS_SELECTOR, ".artdeco-global-alert-action__wrapper button")
button_accept_cookies = buttons_cookies[0]
button_accept_cookies.click()


