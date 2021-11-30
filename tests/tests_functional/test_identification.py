from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestIdentification(StaticLiveServerTestCase):
    def test_register(self):
        # Open the browser with webdrive
        self.browser = webdriver.Chrome("tests/tests_functional/chromedriver")
        self.browser.get(self.live_server_url + reverse("register"))

        id_username = self.browser.find_element_by_id("id_username")
        id_username.send_keys("user1")
        id_last_name = self.browser.find_element_by_id("id_last_name")
        id_last_name.send_keys("last_name_user1")
        id_email = self.browser.find_element_by_id("id_email")
        id_email.send_keys("user1@email.com")
        id_password1 = self.browser.find_element_by_id("id_password1")
        id_password1.send_keys("Password1!")
        id_password2 = self.browser.find_element_by_id("id_password2")
        id_password2.send_keys("Password1!")
        signup = self.browser.find_element_by_id("submit_register")
        signup.submit()

        self.assertEqual(self.browser.find_element_by_tag_name('h2').text,
                         "Créer son espace utilisateur")
        self.assertEqual(self.browser.current_url, self.live_server_url +
                         reverse("register"))
        # close the browser
        time.sleep(3)
        self.browser.close()
