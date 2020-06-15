from django.test import TestCase


class HeroesHomepageTest(TestCase):

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/heroes')
		self.assertTemplateUsed(response, 'heroes.html')

class JesterPageTest(TestCase):

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/hero/jester')
		self.assertTemplateUsed(response, 'detail_jester.html')
