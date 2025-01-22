from selenium import webdriver
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
        # User has heard of a cool new online to-do app.
        #He goes to checkout it's homepage
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        #he is invited to enter a to-do item straightaway

        #he types "Buy Medicines" into a text box

        #when he presses enter, the page updates, and now the page lists
        #1: Buy Medicines" as an item in to-do list

	#there is still a textbox inviting him to add another item. He
	#enter "this medicine is for me"

	#the page updates again, and now shows both the items on his list

	#He wonders whether the site will remember the list. He sees that the site
	#has generated a unique URL for him

	#he visited that URL and sees his list

	#Satisfied and goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
