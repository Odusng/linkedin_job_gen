from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🔐 Your LinkedIn login details (change this!)
LINKEDIN_EMAIL = "your-email@example.com"
LINKEDIN_PASSWORD = "your-password"

def setup_driver():
    """Set up Chrome driver for Selenium"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login_to_linkedin(driver):
    """Log into LinkedIn"""
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)

    email_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    email_field.send_keys(LINKEDIN_EMAIL)
    password_field.send_keys(LINKEDIN_PASSWORD)
    password_field.send_keys(Keys.RETURN)

    time.sleep(5)

def search_jobs(driver):
    """Search for Remote Python Jobs"""
    driver.get("https://www.linkedin.com/jobs/search/?keywords=Remote%20Python")
    time.sleep(5)

    job_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

    print("\n🔹🔹 Remote Python Jobs on LinkedIn 🔹🔹\n")
    for job in job_listings[:5]:  # Get first 5 jobs
        try:
            title = job.find_element(By.CSS_SELECTOR, "h3").text.strip()
            company = job.find_element(By.CSS_SELECTOR, "h4").text.strip()
            link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

            print(f"🔹 **{title}**")
            print(f"🏢 **Company:** {company}")
            print(f"🔗 **Apply Here:** {link}")
            print("-" * 50)
        except:
            continue

# 🚀 Run the automation
driver = setup_driver()
login_to_linkedin(driver)
search_jobs(driver)
driver.quit()
