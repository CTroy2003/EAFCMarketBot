from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Paths to Chrome for Testing and ChromeDriver
chrome_binary_path = "/Users/colintroy/Documents/python/futmarket/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
chromedriver_path = "/Users/colintroy/Documents/python/futmarket/chromedriver-mac-x64/chromedriver"

# Configure Chrome Options
options = Options()
options.binary_location = chrome_binary_path

# Set up ChromeDriver service
service = Service(chromedriver_path)

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the sign-in page
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")

try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-standard"))
    )
    login_button.click()
    print("Login button clicked successfully!")
    
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_input.send_keys("...@gmail.com")  # Replace with your email
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logInBtn"))
    )
    next_button.click()
    print("Email entered and NEXT button clicked!")


    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("...")  # Replace with your password
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logInBtn"))
    )
    sign_in_button.click()
    print("Password entered and SIGN IN button clicked!")


    send_code_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnSendCode"))
    )
    send_code_button.click()
    print("Send Code button clicked!")

    user_code = input("Enter the 6-digit code from your email: ").strip()

    two_factor_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twoFactorCode"))
    )
    two_factor_input.send_keys(user_code)
    print("Verification code entered!")

    final_sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnSubmit"))
    )
    final_sign_in_button.click()
    print("Final Sign In button clicked! Login process completed.")

    while True:
        user_input = input("Enter '1' to close the browser: ")
        if user_input.strip() == "1":
            print("Closing the browser...")
            break

except Exception as e:
    print(f"Error: {e}")





driver.quit()
