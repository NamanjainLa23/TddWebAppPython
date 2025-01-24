from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    #class TestCase - Tests are organised into classes
    def setUp(self):
        #runs before each test
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #runs after each test 
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #methods that start with test_ are recognized as test cases by the unittest framework
        # User has heard of a cool new online to-do app.
        #He goes to checkout it's homepage

        self.browser.get('http://localhost:8000')

        #verifies if the string to-do in in title, if not it fails the test
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #he is invited to enter a to-do item straightaway
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.getattribute('placeholder'), 'Enter a ro-do item')

        #he types "Buy Medicines" into a text box
        inputbox.send_keys('Buy Medicines')

        #when he presses enter, the page updates, and now the page lists
        #1: Buy Medicines" as an item in to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy Medcines' for row in rows))

	#there is still a textbox inviting him to add another item. He
	#enter "this medicine is for me"
        self.fail('Finish the test!')

	#the page updates again, and now shows both the items on his list

	#He wonders whether the site will remember the list. He sees that the site
	#has generated a unique URL for him

	#he visited that URL and sees his list

	#Satisfied and goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
