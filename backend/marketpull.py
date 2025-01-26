from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


def loginToTransferMarket(driver, email, password):
    try:
        # Open the target website
        driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")  # Replace with your target URL
        print("Website loaded successfully!")

        # Locate and click the Login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-standard"))
        )
        login_button.click()
        print("Login button clicked successfully!")

        # Enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)
        print("Email entered.")

        # Click NEXT button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logInBtn"))
        )
        next_button.click()
        print("NEXT button clicked!")

        # Enter password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)
        print("Password entered.")

        # Click SIGN IN button
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logInBtn"))
        )
        sign_in_button.click()
        print("SIGN IN button clicked!")

        # Click Send Code button
        send_code_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSendCode"))
        )
        send_code_button.click()
        print("Send Code button clicked!")

        # Wait for user input for 2FA code
        user_code = input("Enter the 6-digit code from your email: ").strip()

        # Enter the two-factor authentication code
        two_factor_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "twoFactorCode"))
        )
        two_factor_input.send_keys(user_code)
        print("Verification code entered!")

        # Click Final Sign In button
        final_sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSubmit"))
        )
        final_sign_in_button.click()
        print("Final Sign In button clicked! Login process completed.")

        # Navigate to Transfers tab
        transfers_tab = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ut-tab-bar-item.icon-transfer"))
        )
        print("Transfers tab located!")

        # Use ActionChains to move to the element and click
        actions = ActionChains(driver)
        actions.move_to_element(transfers_tab).click().perform()
        print("Hovered and clicked on Transfers tab!")

        time.sleep(10)

        # Locate the Transfer Market tile
        transfer_market_tile = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ut-tile-transfer-market"))
        )
        print("Transfer Market tile located!")

        # Use ActionChains to move to the element and click
        actions.move_to_element(transfer_market_tile).click().perform()
        print("Hovered and clicked on Transfer Market tile!")

    except TimeoutException as e:
        print("Timeout Exception: Element not found within the given time.")
        print(f"Error: {e}")
    except NoSuchElementException as e:
        print("No Such Element Exception: The specified element does not exist.")
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main Execution
if __name__ == "__main__":
    # Setting up the WebDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Call the loginToTransferMarket function
        loginToTransferMarket(driver, "colintroy1@gmail.com", "345Edward2003")  # Replace with your email and password

        # Keep the browser open until user decides to close it
        while True:
            user_input = input("Enter '1' to close the browser: ")
            if user_input.strip() == "1":
                print("Closing the browser...")
                break

    finally:
        driver.quit()
        print("Browser closed.")