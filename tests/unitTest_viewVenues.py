import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "testuser"
        pwd = "test123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")  # Go to the Django Admin page
        time.sleep(3)

        # Find and fill out the user/password fields
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)  # Submit the form
        time.sleep(3)  # short rest at the admin page

        # Wait for the page to load after login
        driver.get("http://127.0.0.1:8000")  # Redirect to the homepage
        time.sleep(3)

        # Find and click the "Venues" link
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/a[1]/div/h2").click()
        time.sleep(5)

        try:
            # Verify that the venue page exists by checking for an element
            elem = driver.find_element(By.XPATH, "/html/body/div[2]/h1")  # usable xpath in venues for success navigation
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Venue page does not appear when 'Venues' is clicked")

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
