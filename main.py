import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

email = LinkedIn EMAIL
my_password = LinkedIn PASSWORD
my_phone_number = Phone Number

chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("link")

time.sleep(5)

sign_in = driver.find_element_by_css_selector(".cta-modal__primary-btn")
sign_in.click()

eMail = driver.find_element_by_name("session_key")
eMail.send_keys(email)
time.sleep(1)

password = driver.find_element_by_name("session_password")
password.send_keys(my_password)
time.sleep(1)

signIn = driver.find_element_by_css_selector(".from__button--floating")
signIn.click()

all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in all_jobs:
    print("called")
    job.click()
    time.sleep(2)

    try:
        apply = driver.find_element_by_css_selector(".jobs-apply-button")
        apply.click()
        time.sleep(5)

        phone_number_input = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone_number_input.text == "":
            phone_number_input.send_keys(my_phone_number)
            time.sleep(1)

        submit_button = driver.find_element_by_css_selector("footer div .artdeco-button--2")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(1)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("complex application skipped")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped")
        continue

time.sleep(5)
driver.quit()
