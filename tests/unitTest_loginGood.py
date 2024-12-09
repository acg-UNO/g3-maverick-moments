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

        # finds and fills out user/password fields
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)  # Submit the form
        time.sleep(3)  # short rest at admin page

        # Waits for the page to load after login
        driver.get("http://127.0.0.1:8000")  # Redirect to the homepage
        time.sleep(3)

        try:
            # waits for the Logout button to become visible in nav bar using xpath for it
            logout_button = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/form/button"))
            )

            # ensures Logout button is displayed
            self.assertTrue(logout_button.is_displayed(), "Logout button not found!")

            driver.close()  # Close the browser after login
            print("Login successful!")
            assert True

        except NoSuchElementException:
            driver.close()  # close the browser
            self.fail("Login Failed - 'Logout' button not found")
            assert False

        except Exception as e:
            driver.close()  # Close the browser
            self.fail(f"Test failed due to an unexpected error: {e}")

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
