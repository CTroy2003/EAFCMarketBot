from flask import Flask, request, jsonify
from flask_cors import CORS
import time

import marketpull  

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  


EMAIL = "your_email@example.com"
PASSWORD = "your_password"

app = Flask(__name__)
CORS(app)  

@app.route('/search', methods=['POST'])
def search():
    filters = request.get_json()
    print("Received filter data:", filters)
    
 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        
        if "twoFactorCode" not in filters:
            marketpull.startLoginToTransferMarket(driver, EMAIL, PASSWORD)
            return jsonify({
                "status": "pending",
                "message": "Verification code sent. Please provide the 2FA code in the next request."
            })
        else:
           
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
        print("Error in automation:", e)
        return jsonify({"status": "error", "message": str(e)})
    finally:
        time.sleep(3)  
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True, port=5000)