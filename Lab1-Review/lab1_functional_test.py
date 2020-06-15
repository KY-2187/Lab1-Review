import unittest
import time

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_can_display_a_heroes_list_and_more_information_per_hero(self):
		# Widget has heard about a new wiki app for the game called The Will of the Wisps. 
		# She goes to check out its homepage
		self.browser.get('http://localhost:8000/heroes')

		# She notices the page title and header mention 
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage 
		hero_list = self.browser.find_element_by_id('hero_list')
		self.assertEqual(
				'ul',
				hero_list.tag_name
		)

		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		hero = self.browser.find_element_by_id('hero_jester')
		hero.click()
		time.sleep(1)

		self.assertEqual(
				'http://localhost:8000/hero/jester',
				self.browser.getCurrentUrl()
		)

		# She spots the page title and header mentions the name of the hero she selected.
		self.asstertIn('Jester', self.beowster.title)

		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.	
		back_button = self.browser.find_element_by_id('back_button')
		self.assertEqual(
			'Back to Heroes List'
			back_button.text
		)
		back_button.click()
		time.sleep(1)

		self.assertEqual(
			'http://localhost:8000/heroes',
			self.browser.getCurrentUrl()
		)

		self.fail('Finish the test!')