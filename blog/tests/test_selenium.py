# from django.test import TestCase

# Create your tests here.

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AccountTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://localhost:8000/admin/')
        #find the form element
        time.sleep(0.2)
        id_username = selenium.find_element_by_id('id_username')
        time.sleep(0.2)
        id_password = selenium.find_element_by_id('id_password')
        time.sleep(0.2)
        
        submit = selenium.find_element_by_css_selector(".btn-primary")

        time.sleep(0.2)

        #Fill the form with data
        id_username.send_keys('admin')
        time.sleep(0.2)
        id_password.send_keys('blog@123')
        time.sleep(0.2)
        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(0.2)
        #check the returned result
        assert 'alert-danger' not in selenium.page_source
