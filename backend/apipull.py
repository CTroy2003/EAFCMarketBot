from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os

import marketpull  # Your automation functions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__)
CORS(app)

# Global dictionary to hold driver sessions (for simplicity, we use a single key)
driver_sessions = {}

# Set your login credentials (replace with your actual values)
EMAIL = "colintroy1@gmail.com"
PASSWORD = "345Edward2003"

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "running", "message": "Flask server is up and running!"})

@app.route('/search', methods=['POST'])
def search():
    filters = request.get_json()
    print("Received filter data:", filters)

    # If twoFactorCode is not provided, perform the first half of login.
    if "twoFactorCode" not in filters:
        try:
            options = webdriver.ChromeOptions()
            # Add these options for hosting on Render:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            # Optional: still try to maximize and disable notifications if needed.
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            marketpull.startLoginToTransferMarket(driver, EMAIL, PASSWORD)
            # Store the driver session for later use.
            driver_sessions["default"] = driver
            return jsonify({
                "status": "pending",
                "message": "Verification code sent. Please provide the 2FA code in the next request."
            })
        except Exception as e:
            print("Error in starting login process:", e)
            try:
                driver.quit()
            except Exception:
                pass
            return jsonify({"status": "error", "message": str(e)})
    else:
        # TwoFactorCode provided: retrieve the stored driver and complete the login.
        if "default" not in driver_sessions:
            return jsonify({"status": "error", "message": "No active login session found. Please start login again."})
        driver = driver_sessions["default"]
        try:
            marketpull.continueLoginToTransferMarket(driver, filters["twoFactorCode"])
            if filters.get("rarity"):
                marketpull.select_rarity(driver, filters["rarity"])
            if filters.get("position"):
                marketpull.select_position(driver, filters["position"])
            if filters.get("chemistryStyle"):
                marketpull.select_chemistry_style(driver, filters["chemistryStyle"])
            if filters.get("country"):
                marketpull.select_nationality(driver, filters["country"])
            if filters.get("maxPrice"):
                price_inputs = driver.find_elements(By.CSS_SELECTOR, ".ut-number-input-control")
                if price_inputs:
                    buy_now_max_input = price_inputs[-1]
                    buy_now_max_input.clear()
                    buy_now_max_input.send_keys(filters["maxPrice"])
                    print(f"Entered Buy Now Price Max: {filters['maxPrice']}")
            marketpull.click_search_button(driver)
            purchase_success = marketpull.attempt_buy_card(driver, max_attempts=4)
            result_msg = "Purchase successful!" if purchase_success else "Purchase not successful."
            return jsonify({"status": "success", "message": result_msg})
        except Exception as e:
            print("Error in continuing login process:", e)
            return jsonify({"status": "error", "message": str(e)})
        finally:
            time.sleep(3)
            driver.quit()
            del driver_sessions["default"]

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)