import unittest
from selenium import webdriver

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # Launch your Flask app first
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')

    def test_add_and_delete_item(self):
        # Add a new item
        self.driver.find_element_by_name('item').send_keys('New E2E Item')
        self.driver.find_element_by_name('item').submit()

        # Assert that the added item is present on the page
        self.assertIn('New E2E Item', self.driver.page_source)

        # Delete the item
        self.driver.find_element_by_xpath('//a[contains(@href, "/delete/0")]').click()

        # Assert that the deleted item is no longer present on the page
        self.assertNotIn('New E2E Item', self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
