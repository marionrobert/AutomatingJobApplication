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
time.sleep(3)
buttons_cookies = driver.find_elements(By.CSS_SELECTOR, ".artdeco-global-alert-action__wrapper button")
button_accept_cookies = buttons_cookies[0]
button_accept_cookies.click()

# click on sign in
time.sleep(3)
buttons_sign = driver.find_elements(By.CSS_SELECTOR, ".nav__cta-container a")
button_sign_in = buttons_sign[1]
button_sign_in.click()

# enter my sign_in data
time.sleep(3)
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(LINKEDIN_USERNAME)
time.sleep(5)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(LINKEDIN_PASSWORD)
time.sleep(5)
button_submit = driver.find_element(By.CSS_SELECTOR, "form.login__form button")
button_submit.click()

# enter the job i'm looking for
time.sleep(20)
print("Im' looking for the input job keyword")
job_input = driver.find_element(By.CSS_SELECTOR, "div.jobs-search-box__input--keyword input")
job_input.send_keys("Développeur junior")

# enter the area for the search
time.sleep(5)
print("Im' looking for the input job location")
location_input = driver.find_element(By.CSS_SELECTOR, "div.jobs-search-box__input.jobs-search-box__input--location input")
location_input.send_keys("Ile-de-France, France")
time.sleep(5)
location_input.send_keys(Keys.ENTER)

# # click on button "see all"
# time.sleep(5)
# see_all_button = driver.find_element(By.CSS_SELECTOR, "div.jobs-job-board-list__footer a")
# see_all_button.click()

# # Scrolls down job list pane to load all listings and then returns to the top
# job_list_scroll = driver.find_element_by_class_name("jobs-search-results-list")
# job_list_scroll.click()
# html = driver.find_element_by_tag_name("html")
# html.send_keys(Keys.END)
# time.sleep(3)
# html.send_keys(Keys.HOME)

# get all the jobs offers in a list
time.sleep(5)
all_job_offers = driver.find_elements(By.CSS_SELECTOR, "ul.scaffold-layout__list-container li a")
print(len(all_job_offers))


# get all the link to the offers job
all_link_offers = [job.get_attribute("href") for job in all_job_offers]
print(all_link_offers)

for link in all_link_offers:
    driver.get(link)
    time.sleep(5)
    apply_button = driver.find_element(By.CSS_SELECTOR, "div.jobs-apply-button--top-card span.artdeco-button__text")
    time.sleep(2)
    if apply_button.get_attribute("innerText") == "Candidature simplifiée":
        print("it's supposed to be a simplified application")
        apply_button.click()
        time.sleep(3)
        all_buttons_easy_apply_form = driver.find_elements(By.CSS_SELECTOR, "div.jobs-easy-apply-modal button span.artdeco-button__text")
        send_application_button = all_buttons_easy_apply_form[-1]
        if send_application_button.get_attribute("innerHTML").replace("\n", "").strip() == "Envoyer la candidature":
            print("it's a simplified application. I can validate my CV.")
            select_cv_button = driver.find_element(By.CSS_SELECTOR, "div.jobs-resume-picker__resume-btn-container button")
            select_cv_button.click()
            time.sleep(5)
            print("I have validated my CV. Now, I just have to click on the 'Envoyer la candidature' button.")
        else:
            print("it's finally not a simplified application: there are more steps needed. Next application.")
    else:
        print("it's not a simplified application")

