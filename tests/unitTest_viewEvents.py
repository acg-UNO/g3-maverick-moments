import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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
        driver.get("http://127.0.0.1:8000")  # Redirect to homepage
        time.sleep(3)

        # Find and click the "Events" link
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/a/div/h2").click()
        time.sleep(5)

        try:
            # Verify that the events page exists by checking for an element
            elem = driver.find_element(By.XPATH, "/html/body/h1")  # Example XPath for events title
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Events page does not appear when 'Events' is clicked")

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
