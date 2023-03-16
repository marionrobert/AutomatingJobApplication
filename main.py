from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

LINKEDIN_JOBS_SEARCH_URL = "https://www.linkedin.com/jobs/"
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]
LINKEDIN_USERNAME = os.environ["LINKEDIN_USERNAME"]

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

# click on sign in
buttons_sign = driver.find_elements(By.CSS_SELECTOR, ".nav__cta-container a")
button_sign_in = buttons_sign[1]
button_sign_in.click()

# enter my sign_in data
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(LINKEDIN_USERNAME)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(LINKEDIN_PASSWORD)
button_submit = driver.find_element(By.CSS_SELECTOR, "form.login__form button")
button_submit.click()

# enter the job i'm looking for
time.sleep(10)
job_input = driver.find_element(By.ID, "jobs-search-box-keyword-id-ember24")
# print(job_input.get_attribute("placeholder"))
job_input.send_keys("Développeur junior")
job_input.send_keys(Keys.ENTER)

