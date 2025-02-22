from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os

import marketpull  # Your Selenium automation functions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__)
CORS(app)

# Global dictionary to hold driver sessions (using a single key)
driver_sessions = {}

# Stored credentials (adjust as needed)
EMAIL = "colintroy1@gmail.com"
PASSWORD = "345Edward2003"

@app.route('/')
def home():
    return jsonify({"status": "running", "message": "Flask server is up and running!"})

@app.route('/login', methods=['POST'])
def login():
    """
    When the user clicks the login button:
    - Launch Selenium with stored credentials.
    - Open the EAFC website.
    - Enter email and password.
    - Click the Send Code button.
    - Keep the browser session open.
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        # For local (or manual) testing, do not run headless.
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        marketpull.startLoginToTransferMarket(driver, EMAIL, PASSWORD)
        driver_sessions["default"] = driver
        return jsonify({
            "status": "pending",
            "message": "Login initiated. Email and password entered; 2FA code sent. When ready, submit search with the 2FA code and filters."
        })
    except Exception as e:
        try:
            driver.quit()
        except Exception:
            pass
        return jsonify({"status": "error", "message": str(e)})

@app.route('/search', methods=['POST'])
def search():
    """
    Completes the process:
    - Expects a JSON payload that includes the 2FA code and filter details.
    - Retrieves the stored driver.
    - Completes login by entering the provided 2FA code.
    - Applies filters (rarity, position, etc.), clicks search, and attempts a purchase.
    - Returns the result and then quits the driver.
    """
    data = request.get_json()
    print("Received search data:", data)
    
    if "default" not in driver_sessions:
        return jsonify({"status": "error", "message": "No active login session. Please log in first."}), 400

    driver = driver_sessions["default"]

    # Check that 2FA code is provided
    if "twoFactorCode" not in data:
        return jsonify({"status": "error", "message": "Two-factor code required."}), 400

    try:
        # Complete the login with the 2FA code
        marketpull.continueLoginToTransferMarket(driver, data["twoFactorCode"])

        # Process filter details
        if data.get("rarity"):
            marketpull.select_rarity(driver, data["rarity"])
        if data.get("position"):
            marketpull.select_position(driver, data["position"])
        if data.get("chemistryStyle"):
            marketpull.select_chemistry_style(driver, data["chemistryStyle"])
        if data.get("country"):
            marketpull.select_nationality(driver, data["country"])
        if data.get("maxPrice"):
            price_inputs = driver.find_elements(By.CSS_SELECTOR, ".ut-number-input-control")
            if price_inputs:
                buy_now_max_input = price_inputs[-1]
                buy_now_max_input.clear()
                buy_now_max_input.send_keys(data["maxPrice"])
                print(f"Entered Buy Now Price Max: {data['maxPrice']}")

        marketpull.click_search_button(driver)
        purchase_success = marketpull.attempt_buy_card(driver, max_attempts=4)
        result_msg = "Purchase successful!" if purchase_success else "Purchase not successful."
        return jsonify({"status": "success", "message": result_msg})
    except Exception as e:
        print("Error in /search:", e)
        return jsonify({"status": "error", "message": str(e)})
    finally:
        time.sleep(3)
        driver.quit()
        driver_sessions.pop("default", None)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)