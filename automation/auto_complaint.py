#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Open the website
    driver.get("https://e-jagriti.gov.in/login")

    # Wait for the page to load
    time.sleep(5)

    try:
        # 2. Click on File case
        file_new_case_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='File New Case']"))
        )
        file_new_case_button.click()

        # 2.1 Select from Dropdownlist
        case_type_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "CaseType"))
        )
        case_type_input.clear()
        case_type_input.send_keys("Consumer Complaint")

        # Wait for dropdown and click
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 2.2 Click Next
        buttons = driver.find_elements(By.CLASS_NAME, "css-1mtw1g8")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[-1])
        time.sleep(1)
        buttons[-1].click()

        # 3. Case Details
        # 3.1 Paid as consideration
        input_field = driver.find_element(By.ID, "paidConsideration")
        input_field.clear()
        input_field.send_keys("5000")
        input_field.send_keys(Keys.ENTER)

        # 3.2 Claim Consideration
        input_field = driver.find_element(By.ID, "claimConsideration")
        input_field.clear()
        input_field.send_keys("5000")
        input_field.send_keys(Keys.ENTER)

        # 3.4 State of Cause of Action
        state_of_cause_of_action = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "stateOfCauseOfAction"))
        )
        state_of_cause_of_action.clear()
        state_of_cause_of_action.send_keys("Jharkhand")

        # Wait for dropdown and click
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 3.5 District of Cause of Action
        district_of_cause_of_action = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "districtOfCauseOfAction"))
        )
        district_of_cause_of_action.clear()
        district_of_cause_of_action.send_keys("Bokaro")

        # Wait for dropdown and click
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 3.6 Case category
        case_category = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "caseCategory"))
        )
        case_category.clear()
        case_category.send_keys("Automobiles")

        # Wait for dropdown and click
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 3.7 Sub category
        wait = WebDriverWait(driver, 10)
        input_field = wait.until(EC.element_to_be_clickable((By.ID, "subCategory")))
        input_field.click()

        option_list_xpath = "//ul[@id='subCategory-listbox']/li"
        wait.until(EC.presence_of_element_located((By.XPATH, option_list_xpath)))

        option_to_select = "subCategory-option-1"
        option = wait.until(EC.element_to_be_clickable((By.ID, option_to_select)))
        option.click()

        # 3.8 Click Next
        buttons = driver.find_elements(By.CLASS_NAME, "css-1mtw1g8")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[-1])
        time.sleep(1)
        buttons[-1].click()

        # 4. Complainant/Opposite Party
        # 4.1 Relation
        relation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "relation"))
        )
        relation.clear()
        relation.send_keys("S/o")

        # Wait for dropdown and click
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 4.2 Relative Name
        relative_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "relativeName"))
        )
        relative_name.clear()
        relative_name.send_keys("XYZ")

        # 4.3 Check box selection
        checkbox_options = {
            "senior_citizen": "complainant.isSeniorCitizen",
            "widow": "complainant.isWidow",
            "differently_abled": "complainant.isDifferentlyAbled",
            "serious_ailments": "complainant.seriousAilments"
        }
        selected_option = "senior_citizen"
        checkbox = driver.find_element(By.NAME, checkbox_options[selected_option])
        checkbox.click()

        # 4.4 Address
        # 4.4.1 Address Type
        address_type = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "AddressType"))
        )
        address_type.clear()
        address_type.send_keys("Present")

        # Wait for dropdown and click
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 4.4.2 Landmark
        landmark = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Landmark"))
        )
        landmark.clear()
        landmark.send_keys("river side")

        # 4.5 Opposite Party Details
        # 4.5.1 Name
        o_name_field = driver.find_element(By.NAME, "respondent.name")
        o_name_field.send_keys("John Doe")

        # 4.5.2 Relation
        relation_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='relation'])[2]"))
        )
        relation_2.clear()
        relation_2.send_keys("S/o")

        # Wait for dropdown and click
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 4.5.3 Relative name
        o_relative_name = driver.find_element(By.NAME, "respondent.relativeName")
        o_relative_name.send_keys("John Doe")

        # 4.5.4 Mobile Number
        o_mobile_number = driver.find_element(By.NAME, "respondent.mobileNumber")
        o_mobile_number.send_keys("8962349189")

        # 4.5.5 Email-id
        o_respondent_email = driver.find_element(By.NAME, "respondent.email")
        o_respondent_email.send_keys("btech60094.22@bitmesra.ac.in")

        # 4.5.6 Opponent address
        # 4.5.6.1 Address type
        address_type_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='AddressType'])[2]"))
        )
        address_type_2.clear()
        address_type_2.send_keys("Permanent")

        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 4.5.6.2 Opposite building number
        house_numbers = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "HouseNumber"))
        )
        house_numbers[1].clear()
        house_numbers[1].send_keys("Your Second Address Building No")

        # 4.5.6.3 Opposite Street/block
        street_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='street'])[2]"))
        )
        street_2.clear()
        street_2.send_keys("Your Second Street Name")

        # 4.5.6.4 Landmark
        landmark_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='Landmark'])[2]"))
        )
        landmark_2.clear()
        landmark_2.send_keys("Your Second Landmark")

        # 4.5.6.5 Pincode
        pincode_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='PinCode'])[2]"))
        )
        pincode_2.clear()
        pincode_2.send_keys("814112")

        # 4.5.6.6 Select opposite party district
        district_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='District'])[2]"))
        )
        district_2.clear()
        district_2.send_keys("Deoghar")

        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "base-Popper-root"))
        )
        dropdown_element.click()

        # 4.5.6.7 Opposite police station
        police_station_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='policeStation'])[2]"))
        )
        police_station_2.clear()
        police_station_2.send_keys("Jasidih")

        # 4.6 Click Next
        buttons = driver.find_elements(By.CLASS_NAME, "css-1mtw1g8")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[-1])
        time.sleep(1)
        buttons[-1].click()

        # 5. Additional complaint (Not required now)
        buttons = driver.find_elements(By.CLASS_NAME, "css-1mtw1g8")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[-1])
        time.sleep(1)
        buttons[-1].click()

        # 6. Additional Opposite Party (Not required now)
        buttons = driver.find_elements(By.CLASS_NAME, "css-1mtw1g8")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[-1])
        time.sleep(1)
        buttons[-1].click()

        print("Form submission completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Uncomment below line to close the browser when done
        # driver.quit()
        pass

if __name__ == "__main__":
    main()