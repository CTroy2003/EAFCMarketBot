from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def startLoginToTransferMarket(driver, email, password):
    try:
        
        driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")
        print("Website loaded successfully!")

       
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-standard"))
        )
        login_button.click()
        print("Login button clicked successfully!")

        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)
        print("Email entered.")

       
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logInBtn"))
        )
        next_button.click()
        print("NEXT button clicked!")

        
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)
        print("Password entered.")

        
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logInBtn"))
        )
        sign_in_button.click()
        print("SIGN IN button clicked!")

        
        send_code_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSendCode"))
        )
        send_code_button.click()
        print("Send Code button clicked!")

    except Exception as e:
        print("Error in startLoginToTransferMarket:", e)

def continueLoginToTransferMarket(driver, two_factor_code):
    try:
        two_factor_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "twoFactorCode"))
        )
        two_factor_input.send_keys(two_factor_code)
        print("Verification code entered!")

       
        final_sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSubmit"))
        )
        final_sign_in_button.click()
        print("Final Sign In button clicked! Login process completed.")

        
        transfers_tab = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ut-tab-bar-item.icon-transfer"))
        )
        print("Transfers tab located!")

       
        actions = ActionChains(driver)
        actions.move_to_element(transfers_tab).click().perform()
        print("Hovered and clicked on Transfers tab!")

        time.sleep(10)

        
        transfer_market_tile = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ut-tile-transfer-market"))
        )
        print("Transfer Market tile located!")

       
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

def select_rarity(driver, rarity_choice):
    """
    Selects the Rarity filter option.
    """
    try:
       
        rarity_filter_container = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class, 'inline-list-select') and .//span[normalize-space(text())='Rarity']]"
            ))
        )
        rarity_filter_container.click()
        print("Clicked on the Rarity filter container.")

        
        li_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'with-icon')]"))
        )

        found = False
        for li in li_elements:
            li_text = li.text.strip()
            if li_text.lower() == rarity_choice.lower():
                li.click()
                print(f"Selected Rarity: {li_text}")
                found = True
                break

        if not found:
            print(f"Rarity '{rarity_choice}' not found in the list.")
    except TimeoutException as e:
        print("Timeout while waiting for elements related to the Rarity filter.")
        print(f"Error: {e}")
    except Exception as e:
        print("An error occurred while selecting Rarity:", e)

def select_position(driver, position_choice):
    """
    Selects the Position filter option.
    """
    try:
        
        position_filter_container = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class, 'inline-list-select') and .//span[normalize-space(text())='Position']]"
            ))
        )
        position_filter_container.click()
        print("Clicked on the Position filter container.")

        
        li_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'with-icon')]"))
        )

        found = False
        for li in li_elements:
            li_text = li.text.strip()
            if li_text.lower() == position_choice.lower():
                li.click()
                print(f"Selected Position: {li_text}")
                found = True
                break

        if not found:
            print(f"Position '{position_choice}' not found in the list.")
    except TimeoutException as e:
        print("Timeout while waiting for elements related to the Position filter.")
        print(f"Error: {e}")
    except Exception as e:
        print("An error occurred while selecting Position:", e)

def select_chemistry_style(driver, style_choice):
    """
    Selects the Chemistry Style filter option.
    """
    try:
        
        style_filter_container = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class, 'inline-list-select') and .//span[normalize-space(text())='Chemistry Style']]"
            ))
        )
        style_filter_container.click()
        print("Clicked on the Chemistry Style filter container.")

        
        li_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'with-icon')]"))
        )

        found = False
        for li in li_elements:
            li_text = li.text.strip()
            if li_text.lower() == style_choice.lower():
                li.click()
                print(f"Selected Chemistry Style: {li_text}")
                found = True
                break

        if not found:
            print(f"Chemistry Style '{style_choice}' not found in the list.")
    except TimeoutException as e:
        print("Timeout while waiting for elements related to the Chemistry Style filter.")
        print(f"Error: {e}")
    except Exception as e:
        print("An error occurred while selecting Chemistry Style:", e)

def select_nationality(driver, nationality_choice):
    """
    Selects the Nationality filter option.
    """
    try:
        
        nationality_filter_container = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class, 'inline-list-select') and .//span[normalize-space(text())='Nationality']]"
            ))
        )
        nationality_filter_container.click()
        print("Clicked on the Nationality filter container.")

        
        li_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'with-icon')]"))
        )

        found = False
        for li in li_elements:
            li_text = li.text.strip()
            if li_text.lower() == nationality_choice.lower():
                li.click()
                print(f"Selected Nationality: {li_text}")
                found = True
                break

        if not found:
            print(f"Nationality '{nationality_choice}' not found in the list.")
    except TimeoutException as e:
        print("Timeout while waiting for elements related to the Nationality filter.")
        print(f"Error: {e}")
    except Exception as e:
        print("An error occurred while selecting Nationality:", e)

def set_buy_now_max(driver):

    max_price = input("Enter maximum Buy Now Price: ").strip()
    try:
        
        price_inputs = driver.find_elements(By.CSS_SELECTOR, ".ut-number-input-control")
        if not price_inputs:
            print("No price input fields found!")
            return

        
        buy_now_max_input = price_inputs[-1]
        buy_now_max_input.clear()
        buy_now_max_input.send_keys(max_price)
        print(f"Entered Buy Now Price Max: {max_price}")
    except Exception as e:
        print("Error while setting Buy Now Price Max:", e)

def click_search_button(driver):
    try:
        
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(@class, 'btn-standard') and contains(@class, 'call-to-action') and normalize-space(text())='Search']"
            ))
        )
        search_button.click()
        print("Search button clicked successfully.")
    except Exception as e:
        print("Error clicking the search button:", e)

def attempt_buy_card(driver, max_attempts=4):
    """
    Attempts to purchase a card by clicking a listing on the left,
    then using the Buy Now button from the details panel on the right.
    It will try up to 'max_attempts' times. If the listing is expired, it is skipped.
    After clicking 'Buy Now' and confirming, it checks if the listing's class includes 'won'.
    """
    attempts = 0
    
    listings = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.listFUTItem.has-auction-data"))
    )
    
    if not listings:
        print("No listings found on the page.")
        return False

    for listing in listings:
        if attempts >= max_attempts:
            print("Reached maximum purchase attempts.")
            break

        
        classes = listing.get_attribute("class")
        if "expired" in classes:
            print("Listing is expired; skipping to next listing.")
            continue

        try:
            
            listing.click()
            print("Clicked the listing to update details panel.")

            
            buy_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class, 'buyButton')]")
                )
            )
            buy_now_button.click()
            print("Clicked the 'Buy Now' button in the details panel.")

            
            ok_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[@class='btn-text' and normalize-space(text())='Ok']/ancestor::button")
                )
            )
            ok_button.click()
            print("Clicked the 'Ok' button in the confirmation dialog.")

           
            time.sleep(2)
            updated_classes = listing.get_attribute("class")
            if "won" in updated_classes:
                print("Purchase successful for this listing!")
                return True
            else:
                print("Purchase attempt unsuccessful; moving to the next listing.")
            attempts += 1

        except Exception as e:
            print("Error during purchase attempt:", e)
            attempts += 1
            continue

    print("No successful purchase after {} attempts.".format(attempts))
    return False

def go_back_to_filters(driver):
    """
    Clicks the navigation button to return from the listings page back to the filter page.
    """
    try:
        back_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ut-navigation-button-control"))
        )
        back_button.click()
        print("Returned to the filter page.")
    except Exception as e:
        print("Error returning to filter page:", e)



if __name__ == "__main__":
    
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        
        startLoginToTransferMarket(driver, "---", "---")
        print("Please check your email for the verification code.")
        
        # Prompt user to enter the verification code manually.
        two_factor_code = input("Enter the verification code: ")
        
        # Continue login using the provided 2FA code.
        continueLoginToTransferMarket(driver, two_factor_code)
        
        while True:
            
            user_rarity = input("Enter the Rarity you want to select (e.g., 'Common', 'Rare', etc.) or press Enter to skip: ").strip()
            if user_rarity:
                select_rarity(driver, user_rarity)
            else:
                print("No Rarity filter selected. Continuing...")

            user_position = input("Enter the Position you want to select (e.g., 'RB', 'GK', etc.) or press Enter to skip: ").strip()
            if user_position:
                select_position(driver, user_position)
            else:
                print("No Position filter selected. Continuing...")

            user_style = input("Enter the Chemistry Style you want to select (e.g., 'Finisher', 'Maestro', etc.) or press Enter to skip: ").strip()
            if user_style:
                select_chemistry_style(driver, user_style)
            else:
                print("No Chemistry Style filter selected. Continuing...")

            user_nationality = input("Enter the Nationality you want to select (e.g., 'England', 'Spain', etc.) or press Enter to skip: ").strip()
            if user_nationality:
                select_nationality(driver, user_nationality)
            else:
                print("No Nationality filter selected. Continuing...")

            set_buy_now_max(driver)
            click_search_button(driver)

            
            attempt_buy_card(driver, max_attempts=4)

            
            choice = input("Enter '1' to return to the filter menu and search again, or any other key to exit: ").strip()
            if choice == "1":
                go_back_to_filters(driver)
                
                continue
            else:
                print("Exiting the browser.")
                break

    finally:
        driver.quit()
        print("Browser closed.")
